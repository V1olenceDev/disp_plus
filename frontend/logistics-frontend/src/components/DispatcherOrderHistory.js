import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DispatcherOrderHistory = () => {
    const [orders, setOrders] = useState([]);

    useEffect(() => {
        const fetchOrders = async () => {
            try {
                const response = await axios.get('YOUR_API_URL_FOR_DISPATCHER_ORDER_HISTORY');
                setOrders(response.data);
            } catch (err) {
                console.error("Ошибка при загрузке истории заявок для диспетчера:", err);
            }
        };

        fetchOrders();
    }, []);

    return (
        <div>
            <h2>История заявок</h2>
            <ul>
                {orders.map(order => (
                    <li key={order.id}>
                        {order.date} - {order.equipment} - {order.status}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default DispatcherOrderHistory;