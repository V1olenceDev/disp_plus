import React, { useState } from 'react';
import axios from 'axios';
import { API_BASE_URL } from '../config';

const LoginPage = ({ onLoginSuccess }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(`${API_BASE_URL}/api/jwt-token-auth/`, {
                username,
                password
            });
            if (response.data.token) {
                onLoginSuccess(response.data.token);
            }
        } catch (err) {
            console.error(err);
            if (err.response && err.response.data) {
                setError(err.response.data.detail || 'Произошла ошибка при входе');
            } else {
                setError('Произошла ошибка при входе');
            }
        }
    };

    return (
        <div>
            <h2>Вход</h2>
            <form onSubmit={handleLogin}>
                <input
                    type="text"
                    placeholder="Логин"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input
                    type="password"
                    placeholder="Пароль"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit">Войти</button>
            </form>
            {error && <p>{error}</p>}
        </div>
    );
};

export default LoginPage;