import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { API_BASE_URL } from '../config';

const ManageVehicles = () => {
    const [vehicles, setVehicles] = useState([]);

    useEffect(() => {
        const fetchVehicles = async () => {
            try {
                const response = await axios.get(`${API_BASE_URL}/manage-vehicles`);
                setVehicles(response.data);
            } catch (err) {
                console.error("Ошибка при загрузке списка транспортных средств:", err);
            }
        };

        fetchVehicles();
    }, []);

    const toggleAvailability = async (vehicleId) => {
        try {
            await axios.post('YOUR_API_URL_FOR_TOGGLE_VEHICLE', {
                vehicleId
            });
            const updatedVehicles = vehicles.map(vehicle => 
                vehicle.id === vehicleId ? {...vehicle, available: !vehicle.available} : vehicle
            );
            setVehicles(updatedVehicles);
        } catch (err) {
            console.error("Ошибка при обновлении статуса техники:", err);
        }
    };

    return (
        <div>
            <h2>Управление техникой</h2>
            <ul>
                {vehicles.map(vehicle => (
                    <li key={vehicle.id}>
                        {vehicle.name} - {vehicle.available ? 'Доступно' : 'Недоступно'}
                        <button onClick={() => toggleAvailability(vehicle.id)}>
                            {vehicle.available ? 'Сделать недоступной' : 'Сделать доступной'}
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ManageVehicles;