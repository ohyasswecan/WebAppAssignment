// src/api/auth.js
import axiosInstance from './axiosInstance';
import { useContext } from 'react';
import UserContext from '../contexts/UserContext';

const useAuth = () => {
    const { login } = useContext(UserContext);

    const authenticate = async (username, password) => {
        try {
            const response = await axiosInstance.post('/app/api/token/', { username, password });
            const { access, refresh } = response.data;

            // Store tokens in local storage
            localStorage.setItem('access_token', access);
            localStorage.setItem('refresh_token', refresh);

            // Update axiosInstance headers with the new token
            axiosInstance.defaults.headers['Authorization'] = `Bearer ${access}`;

            // Fetch user info
            const userInfoResponse = await axiosInstance.get('/app/api/userinfo/');
            const userInfo = userInfoResponse.data;

            // Save user info in context
            login(userInfo);

            return userInfo;
        } catch (error) {
            console.error('Login failed', error);
            throw error;
        }
    };

    return { authenticate };
};

export default useAuth;
