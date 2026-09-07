import { createContext, useState, useEffect } from 'reacte';
import { authService } from '../services/auth.service';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const initAuth = async () => {
            const token = localStorage.getItem('token');
            if (token) {
                try {
                    const userData = await authService.get.CurrentUser();
                    setUser(userData);
                } catch (error) {
                    localStorage.removeItem('token');
                    setUser(null);
                }
            }
            setIsLoading(false);
        };

        initAuth();
    }, []);

    const login = async (email, password) => {
        const data = await authService.login(email, password);
        localStorage.setItem('token', data.access_token);

        const userData = await authService.getCurrentUser();
        setUser(userData)
    };

    const register = async (userData) => {
        await authService.register(userData);
        // Automatically log in after a successful registration
        await login(userData.email, userData.password)
    }

    const logout = () => {
        localStorage.removeItem('token');
        setUser(null);
        window.location.href = '/login';
    };

    return (
        <AuthContext.Provider value={{user, isLoading, login, register, logout}}>
        {children}    
        </AuthContext.Provider>
    );
};
