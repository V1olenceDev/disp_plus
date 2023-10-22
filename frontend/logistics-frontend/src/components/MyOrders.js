import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MyOrders = () => {
    const [orders, setOrders] = useState([]);

    useEffect(() => {
        const fetchOrders = async () => {
            try {
                const response = await axios.get('YOUR_API_URL_FOR_MY_ORDERS');
                setOrders(response.data);
            } catch (err) {
                console.error("Ошибка при загрузке заявок:", err);
            }
        };

        fetchOrders();
    }, []);

    return (
        <div>
            <h2>Мои заказы</h2>
            <ul>
                {orders.map(order => (
                    <li key={order.id}>
                        {/* Отобразите здесь информацию о заказе */}
                        {order.date} - {order.equipment} - {order.status}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default MyOrders;