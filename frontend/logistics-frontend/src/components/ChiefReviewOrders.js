import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { API_BASE_URL } from '../config';

const ChiefReviewOrders = () => {
    const [orders, setOrders] = useState([]);

    useEffect(() => {
        const fetchOrders = async () => {
            try {
                const response = await axios.get(`${API_BASE_URL}/chief-orders-to-review`);
                setOrders(response.data);
            } catch (err) {
                console.error("Ошибка при загрузке заявок для рассмотрения:", err);
            }
        };

        fetchOrders();
    }, []);

    const handleDecision = async (orderId, decision) => {
        try {
            await axios.post('YOUR_API_URL_FOR_CHIEF_DECISION', {
                orderId, decision
            });
            const updatedOrders = orders.filter(order => order.id !== orderId);
            setOrders(updatedOrders);
        } catch (err) {
            console.error("Ошибка при обновлении статуса заявки:", err);
        }
    };

    return (
        <div>
            <h2>Заявки на рассмотрение</h2>
            <ul>
                {orders.map(order => (
                    <li key={order.id}>
                        {order.date} - {order.equipment} - {order.reason}
                        <button onClick={() => handleDecision(order.id, 'Принята')}>Принять</button>
                        <button onClick={() => handleDecision(order.id, 'Отклонена')}>Отклонить</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ChiefReviewOrders;