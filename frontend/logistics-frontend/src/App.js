import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginPage from './components/LoginPage';
import ProfilePage from './components/ProfilePage'; // Добавьте этот импорт
import { AuthProvider } from './components/AuthContext';
import CreateOrder from './components/CreateOrder';  // добавьте этот импорт
import MyOrders from './components/MyOrders';
import DispatcherOrders from './components/DispatcherOrders';  // добавьте этот импорт
import DispatcherOrderHistory from './components/DispatcherOrderHistory';
import ChiefReviewOrders from './components/ChiefReviewOrders';  
import ChiefOrderHistory from './components/ChiefOrderHistory';  
import ManageVehicles from './components/ManageVehicles';
import DriverSchedule from './components/DriverSchedule';

function App() {
    return (
        <Router>
            <AuthProvider>
                <Routes>
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/profile" element={<ProfilePage />} /> {/* Добавьте этот маршрут */}
                    <Route path="/create-order" element={<CreateOrder />} />
                    <Route path="/my-orders" element={<MyOrders />} />
                    <Route path="/dispatcher-orders" element={<DispatcherOrders />} />
                    <Route path="/dispatcher-order-history" element={<DispatcherOrderHistory />} />
                    <Route path="/chief-review-orders" element={<ChiefReviewOrders />} />
                    <Route path="/chief-order-history" element={<ChiefOrderHistory />} />
                    <Route path="/manage-vehicles" element={<ManageVehicles />} />
                    <Route path="/driver-schedule" element={<DriverSchedule />} />
                    {/* Другие маршруты будут добавлены позже */}
                </Routes>
            </AuthProvider>
        </Router>
    );
}

export default App;