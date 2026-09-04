import api from './api'

export const expenseService = {
    getExpenses: async (skip = 0, limit = 100) => {
        const response = await api.get('/expenses/?skip = ${skip}&limit=${limit}');
        return response.data;
    },

    createExpense: async (expenseData) => {
        const response = await api.post('/expenses/', expenseData);
        return response.data;
    },

    updateExpense: async (id, expenseData) => {
        const response = await api.put('/expenses/${id}', expenseData);
        return response.data;
    },

    deleteExpense: async (id) => {
        const response = await api.delete('/expenses/${id}');
        return response.data;
    },

    getSummary: async () => {
        const response = await api.get('/expenses/summary');
        return response.data;
    }
};