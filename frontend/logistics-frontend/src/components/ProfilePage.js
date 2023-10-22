import React from 'react';
import { useAuth } from './AuthContext';

const ProfilePage = () => {
    const { currentUser } = useAuth();

    if (!currentUser) {
        return <div>Пожалуйста, войдите в систему.</div>;
    }

    return (
        <div>
            <h2>Профиль</h2>
            <p><strong>Логин:</strong> {currentUser.username}</p>
            {/* Добавьте другие данные пользователя, если они есть */}
        </div>
    );
};

export default ProfilePage;