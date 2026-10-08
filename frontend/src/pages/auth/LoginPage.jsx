import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../hooks/useAuth'

export default function LoginPage() {
    const [isLogin, setIsLogin] = useState(true);
    const [formData, setFormData] = useState({name: '', email: '', password: ''});
    const [error, setError] = useState('');
    const [isSubmitting, setIsSubmitting] = useState(false);

    const { user, login, register } = useAuth();
    const navigate = useNavigate();

    useEffect(() => {
        if(user) {
            navigate('/dashboard', {replace: true});
        }
    }, [user, navigate]);

    const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value});
        if(error)
            setError('')
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setIsSubmitting(true);

        try {
            if(isLogin) {
                await login(formData.email, formData.password);
            }
            else {
                await register(formData);
            }
        }
        catch (err) {
            setError(err.response?.data?.detail || 'An error occurred during authentication. please try again.');
        }
        finally {
            setIsSubmitting(false);
        }
    };


    return (
        <div className="min-h-screen flex items-center justify-center bg-slate-50 px-4">
            <div className="max-w-md w-full bg-white rounded-xl shadow-lg border border-slate-100 p-8 space-y-6">

                <div className="text-center space-y-2">
                    <h1 className="text-3xl font-bold text-slate-900 tracking-tight">
                    {isLogin ? 'Welcome back' : 'Create an account'}
                    </h1>
                    <p className="text-slate-500 font-medium">
                        {isLogin ? 'Enter your details to access your dashboard' : 'Start tracking your expenses today'}
                    </p>
                </div>

                {error && (
                    <div className="p-3 bg-red-50 border border-red-200 text-red-600 rounded-lg text-sm font-medium">
                        {error}
                    </div>
                )}
                <form onSubmit={handleSubmit} className="space-y-4">
                    {!isLogin && (
                        <div className="space-y-2">
                            <label className="text-sm font-semibold text-slate-700">Full Name</label>
                            <input
                            type="text"
                            name="name"
                            required
                            value={formData.name}
                            onChange={handleChange}
                            className="w-full px-4 py-2 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                            placeholder="You'r full name"
                            />
                        </div>
                    )}

                    <div className="space-y-2">
                        <label className="text-sm font-semibold text-slate-700">Email Address</label>
                        <input
                        type="email"
                        name="email"
                        required
                        value={formData.email}
                        onChange={handleChange}
                        className="w-full px-4 py-2 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                        placeholder="You'r email address"
                        />
                    </div>

                    <div className="space-y-2">
                        <label className="text-sm font-semibold text-slate-700">Password</label>
                        <input
                        type="password"
                        name="password"
                        required
                        value={formData.password}
                        onChange={handleChange}
                        className="w-full px-4 py-2 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                        placeholder="You'r password"
                        />
                    </div>

                    <button
                      type="submit"
                      disabled={isSubmitting}
                      className="cursor-pointer w-full py-2.5 px-4 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 focus:ring-4 focus:ring-blue-200 transition-all disabled:opacity-70 disabled:cursor-not-allowed flex justify-center items-center"
                    >
                      {isSubmitting ? (
                        <div className="h-5 w-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>

                      ) : (
                        isLogin ? 'Sign In' : 'Sign Up'
                      )}  
                    </button>
                </form>

                <div className="text-center text-sm text-slate-600 font-medium">
                    {isLogin ? "Don't have an account? " : "Already have an account? "}
                    <button
                      type="button"
                      onClick={() => {
                          setIsLogin(!isLogin);
                          setError('');
                      }}
                      className="cursor-pointer text-blue-600 hover:text-blue-800 hover:underline transition-all"
                    >
                    {isLogin ? 'Sign up' : 'Sign in'}
                    </button>
                </div>

            </div>
        </div>
    );
}