import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DispatcherOrders = () => {
    const [orders, setOrders] = useState([]);

    useEffect(() => {
        const fetchOrders = async () => {
            try {
                const response = await axios.get('YOUR_API_URL_FOR_DISPATCHER_ORDERS');
                setOrders(response.data);
            } catch (err) {
                console.error("Ошибка при загрузке заявок для диспетчера:", err);
            }
        };

        fetchOrders();
    }, []);

    const handleDecision = async (orderId, decision) => {
        try {
            // Здесь вы будете отправлять запрос на ваш API для обновления статуса заявки
            await axios.post('YOUR_API_URL_FOR_DECISION', {
                orderId, decision
            });
            // Обновите список заказов после принятия решения
            const updatedOrders = orders.filter(order => order.id !== orderId);
            setOrders(updatedOrders);
        } catch (err) {
            console.error("Ошибка при обновлении статуса заявки:", err);
        }
    };

    return (
        <div>
            <h2>Посмотреть заявки</h2>
            <ul>
                {orders.map(order => (
                    <li key={order.id}>
                        {order.date} - {order.equipment} - {order.reason}
                        <button onClick={() => handleDecision(order.id, 'На рассмотрении')}>На рассмотрение</button>
                        <button onClick={() => handleDecision(order.id, 'Отклонена')}>Отклонить</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default DispatcherOrders;