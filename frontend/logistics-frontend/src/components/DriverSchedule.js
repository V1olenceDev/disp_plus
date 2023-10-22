import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { API_BASE_URL } from '../config';

const DriverSchedule = () => {
    const [orders, setOrders] = useState([]);
    const [selectedDate, setSelectedDate] = useState(new Date().toISOString().split('T')[0]);

    useEffect(() => {
        const fetchOrders = async () => {
            try {
                const response = await axios.get(`${API_BASE_URL}/driver-schedule?date=${selectedDate}`);
                setOrders(response.data);
            } catch (err) {
                console.error("Ошибка при загрузке разнарядки для водителя:", err);
            }
        };

        fetchOrders();
    }, [selectedDate]);

    return (
        <div>
            <h2>Разнарядка</h2>
            <label>
                Выберите дату: 
                <input type="date" value={selectedDate} onChange={e => setSelectedDate(e.target.value)} />
            </label>
            <ul>
                {orders.length === 0 
                    ? <li>На выбранную дату заявок нет</li> 
                    : orders.map(order => (
                        <li key={order.id}>
                            {order.date} - {order.equipment} - {order.reason}
                        </li>
                    ))
                }
            </ul>
        </div>
    );
};

export default DriverSchedule;