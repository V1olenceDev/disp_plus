import React, { useState } from 'react';
import axios from 'axios';

const CreateOrder = () => {
    const [date, setDate] = useState('');
    const [time, setTime] = useState('');
    const [equipment, setEquipment] = useState('');
    const [reason, setReason] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('YOUR_API_URL_FOR_ORDERS', {
                date, time, equipment, reason
            });
            if (response.data.success) {
                // Здесь можно добавить уведомление об успешном создании заявки или редирект
            }
        } catch (err) {
            console.error("Ошибка при создании заявки:", err);
        }
    };

    return (
        <div>
            <h2>Создать заявку</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="date"
                    value={date}
                    onChange={(e) => setDate(e.target.value)}
                    required
                />
                <input
                    type="time"
                    value={time}
                    onChange={(e) => setTime(e.target.value)}
                    required
                />
                <select value={equipment} onChange={(e) => setEquipment(e.target.value)}>
                    {/* Здесь нужно добавить опции для выбора техники */}
                    <option value="Техника1">Техника1</option>
                    <option value="Техника2">Техника2</option>
                </select>
                <textarea
                    value={reason}
                    onChange={(e) => setReason(e.target.value)}
                    placeholder="Причина заказа"
                    required
                />
                <button type="submit">Заказать</button>
            </form>
        </div>
    );
};

export default CreateOrder;