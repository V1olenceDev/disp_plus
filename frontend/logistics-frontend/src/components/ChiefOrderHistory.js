import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { API_BASE_URL } from '../config';

const ChiefOrderHistory = () => {
    const [orderHistory, setOrderHistory] = useState([]);

    useEffect(() => {
        const fetchOrderHistory = async () => {
            try {
                const response = await axios.get(`${API_BASE_URL}/chief-order-history`);
                setOrderHistory(response.data);
            } catch (err) {
                console.error("Ошибка при загрузке истории заявок:", err);
            }
        };

        fetchOrderHistory();
    }, []);

    return (
        <div>
            <h2>История заказов</h2>
            <ul>
                {orderHistory.map(order => (
                    <li key={order.id}>
                        {/* Здесь ваш код для отображения каждого заказа */}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ChiefOrderHistory;