import { useAuth } from "../../hooks/useAuth";

export default function Dashboard() {
    const { user, logout } = useAuth();

    return (
        <div className="min-h-screen p-8 bg-slate-50">
            <div className="max-w-4xl mx-auto bg-white p-6 rounded-xl shadow-sm">
                <h1 className="text-2xl font-bold text-slate-800 mb-4">
                    Welcome back, {user?.name}
                </h1>
            
                <button onClick={logout} 
                        className="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700">
                        logout
                </button>
            </div>
        </div>
    );
}