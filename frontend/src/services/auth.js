import api from './api'

export const authService = {
    login: async (email, password) => {
        const formData = new URLSearchParams();
        formData.append('username', email);
        formData.append('password', password);

        const response = await api.post('/login', formData, {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        });
        return response.data;
    },

    register: async (userData) => {
        const response = await api.post('/users/', userData);
        return response.data;
    },

    getCurrentUser: async () => {
        const response = await api.get('/users/me');
        return response.data;
    }
};