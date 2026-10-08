import { useAuth } from "../../hooks/useAuth";
import { useExpenses } from "../../hooks/useExpenses"

export default function Dashboard() {
    const { user, logout } = useAuth();
    const { expenses, summry, isLoading, error } = useExpenses();

    return (
        <div className="min-h-screen bg-slate-50 font-sans text-slate-900">
           <nav className="bg-white border-b border-slate-200 sticky top-0 z-10">
             <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between items-center h-16">
                    <h1 className="text-xl font-bold text-blue-600 tracking-tight">
                        ExpenseAnalyzer
                    </h1>
                    <div className="flex items-center space-x-4">
                        <span className-="text-sm font-medium text-slate-500">
                            {user?.email}
                        </span>
                        <button
                        onClick={logout}
                        className="cursor-pointer text-sm font-medium text-slate-600 hover:text-red-600 transition-colors"
                        >
                            Log out
                        </button>
                    </div>
                </div> 
             </div>
           </nav>

           <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
                <div>
                    <h2 className="text-3xl font-bold tracking-tight text-slate-900">
                        Welcome back, {user?.name.split(' ')[0]}
                    </h2>
                    <p className="text-slate-500 mt-1">
                        Here is your financial overview.
                    </p>
                </div>

                {isLoading ? (
                    <div className="flex justify-center py-20">
                        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
                    </div>
                ) : error ? (
                  <div classNAme="p-4 bg-red-50 border border-red-200 text-red-600 rounded-xl">
                    {error}
                  </div>
                ) : expenses.length === 0 ? (
                    <div className="bg-white border border-slate-200 rounded-2xl p-12 text-crnter shadow-sm">
                        <div className="mx-auto h-16 bg-blue-50 rounded-full flex items-center justify-center mb-4">
                            <svg className="h-8 w-8 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={4} d="M12 6v6m0-6h6m-6 0H6" />
                            </svg>
                        </div>
                        <h3 className="text-lg font-bold text-slate-900 mb-1"> No expenses yet</h3>
                        <p className="text-slate-500 mb-6">Get started by adding your first transaction</p>
                        <button className="cursor-pointer px-5 py-2.5 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 shadow-sm transition-all hover:scale-105">
                            Add Expense
                        </button>
                    </div>
                ) : (
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div className="md:col-span-2 bg-white rounded-2xl shadow-sm border border-slate-200 p-6">
                        <h3 className="text-lg font-bold mb-4">Recent Transactions</h3>
                        <p className="text-slate-500">List...</p>
                    </div>
                    <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6">
                        <h3 className="text-lg font-bold mb-4">Category Summary</h3>
                        <p className="text-slate-500">Analytics...</p>
                    </div>
                  </div>
                )}
           </main>
        </div>
    );
}