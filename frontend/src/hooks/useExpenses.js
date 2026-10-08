import { useState, useEffect, useCallback } from 'react'
import { expenseService } from '../services/expense'

export const useExpenses = () => {
    const [expenses, setExpenses] = useState([]);
    const[summary, setSummary] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchAllData = useCallback(async () => {
        setIsLoading(true);
        try {
            const [expensesData, summaryData] = await Promise.all([
                expenseService.getExpenses(),
                expenseService.getSummary()
            ]);
            setExpenses(expensesData);
            setSummary(summaryData);
            setError(null);
        } 
        catch (err) {
            setError('Failed to load financial data. Please try again.');
        }
        finally {
            setIsLoading(false);
        }
    }, []);

    useEffect(() => {
        fetchAllData();
    }, [fetchAllData]);

    return {expenses, summary, isLoading, error, refreshData: fetchAllData};
};