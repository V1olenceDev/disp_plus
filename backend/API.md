# Документация к API

## 1. Пользователи

### 1.1. Список пользователей и создание нового пользователя
- **URL**: /users/
- **Метод**: GET, POST
- **Описание**: Получение списка всех пользователей или создание нового пользователя.

#### Пример ответа GET:
```json
[
    {
        "id": 1,
        "first_name": "Иван",
        "last_name": "Иванов",
        "role": "Диспетчер",
        "department": "Отдел логистики",
        "phone_num": "+1234567890"
    }
]
```

#### Пример запроса POST:
```json
{
    "first_name": "Анна",
    "last_name": "Петрова",
    "role": "Водитель",
    "department": "Отдел транспорта",
    "phone_num": "+0987654321"
}
```

### Пример ответа POST:
```json
{
    "id": 2,
    "first_name": "Анна",
    "last_name": "Петрова",
    "role": "Водитель",
    "department": "Отдел транспорта",
    "phone_num": "+0987654321"
}
```

### 1.2. Детали пользователя
- **URL**: /users/<int:pk>/
- **Метод**: GET, PUT, DELETE
- **Описание**: Получение, обновление или удаление деталей конкретного пользователя.

#### Пример ответа GET:
```json
{
    "id": 1,
    "first_name": "Иван",
    "last_name": "Иванов",
    "role": "Диспетчер",
    "department": "Отдел логистики",
    "phone_num": "+1234567890"
}
```

#### Пример запроса PUT:
```json
{
    "phone_num": "+1111111111"
}
```

#### Пример ответа PUT:
```json
{
    "id": 1,
    "first_name": "Иван",
    "last_name": "Иванов",
    "role": "Диспетчер",
    "department": "Отдел логистики",
    "phone_num": "+1111111111"
}
```

#### Пример ответа DELETE:
```json
{
    "message": "Пользователь успешно удален"
}
```

## 2. Транспортные средства

### 2.1. Список транспортных средств и создание нового транспортного средства
- **URL**: /transports/
- **Метод**: GET, POST
- **Описание**: Получение списка всех транспортных средств или создание нового транспортного средства.

#### Пример ответа GET:
```json
[
    {
        "id": 1,
        "name": "Грузовик",
        "status": "Доступен"
    }
]
```

#### Пример запроса POST:
```json
{
    "name": "Легковой автомобиль",
    "status": "Доступен"
}
```

#### Пример ответа POST:
```json
{
    "id": 2,
    "name": "Легковой автомобиль",
    "status": "Доступен"
}
```

### 2.2. Детали транспортного средства
- **URL**: /transports/<int:pk>/
- **Метод**: GET, PUT, DELETE
- **Описание**: Получение, обновление или удаление деталей конкретного транспортного средства.

#### Пример ответа GET:
```json
{
    "id": 1,
    "name": "Грузовик",
    "status": "Доступен"
}
```

#### Пример запроса PUT:
```json
{
    "status": "В ремонте"
}
```

#### Пример ответа PUT:
```json
{
    "id": 1,
    "name": "Грузовик",
    "status": "В ремонте"
}
```

#### Пример ответа DELETE:
```json
{
    "message": "Транспортное средство успешно удалено"
}
```

## 3. Заказы

### 3.1. Список заказов и создание нового заказа
- **URL**: /orders/
- **Метод**: GET, POST
- **Описание**: Получение списка всех заказов или создание нового заказа.

#### Пример ответа GET:
```json
[
    {
        "id": 1,
        "creator": {
            "id": 1,
            "first_name": "Иван",
            "last_name": "Иванов",
            "role": "Диспетчер",
            "department": "Отдел логистики",
            "phone_num": "+1234567890"
        },
        "creation_date": "2023-10-10T10:10:10",
        "work_date": "2023-10-11",
        "work_time": "10:00:00",
        "reason": "Перевозка груза",
        "requested_vehicle": {
            "id": 1,
            "name": "Грузовик",
            "status": "Доступен"
        },
        "approved_vehicle": null,
        "assigned_driver": null,
        "status": "На рассмотрении"
    }
]
```

#### Пример запроса POST:
```json
{
    "work_date": "2023-10-11",
    "work_time": "10:00:00",
    "reason": "Перевозка груза",
    "requested_vehicle": 1
}
```

#### Пример ответа POST:
```json
{
    "id": 2,
    "creator": {
        "id": 1,
        "first_name": "Иван",
        "last_name": "Иванов",
        "role": "Диспетчер",
        "department": "Отдел логистики",
        "phone_num": "+1234567890"
    },
    "creation_date": "2023-10-10T10:10:10",
    "work_date": "2023-10-11",
    "work_time": "10:00:00",
    "reason": "Перевозка груза",
    "requested_vehicle": {
        "id": 1,
        "name": "Грузовик",
        "status": "Доступен"
    },
    "approved_vehicle": null,
    "assigned_driver": null,
    "status": "На рассмотрении"
}
```

### 3.2. Детали заказа
- **URL**: /orders/<int:pk>/
- **Метод**: GET, PUT, DELETE
- **Описание**: Получение, обновление или удаление деталей конкретного заказа.

#### Пример ответа GET:
```json
{
    "id": 1,
    "creator": {
        "id": 1,
        "first_name": "Иван",
        "last_name": "Иванов",
        "role": "Диспетчер",
        "department": "Отдел логистики",
        "phone_num": "+1234567890"
    },
    "creation_date": "2023-10-10T10:10:10",
    "work_date": "2023-10-11",
    "work_time": "10:00:00",
    "reason": "Перевозка груза",
    "requested_vehicle": {
        "id": 1,
        "name": "Грузовик",
        "status": "Доступен"
    },
    "approved_vehicle": null,
    "assigned_driver": null,
    "status": "На рассмотрении"
}
```

#### Пример запроса PUT:
```json
{
    "work_date": "2023-10-12"
}
```

#### Пример ответа PUT:
```json
{
    "id": 1,
    "creator": {
        "id": 1,
        "first_name": "Иван",
        "last_name": "Иванов",
        "role": "Диспетчер",
        "department": "Отдел логистики",
        "phone_num": "+1234567890"
    },
    "creation_date": "2023-10-10T10:10:10",
    "work_date": "2023-10-12",
    "work_time": "10:00:00",
    "reason": "Перевозка груза",
    "requested_vehicle": {
        "id": 1,
        "name": "Грузовик",
        "status": "Доступен"
    },
    "approved_vehicle": null,
    "assigned_driver": null,
    "status": "На рассмотрении"
}
```

#### Пример ответа DELETE:
```json
{
    "message": "Заказ успешно удален"
}
```

### 3.3. Мои заказы
- **URL**: /my-orders/
- **Метод**: GET
- **Описание**: Получение списка заказов текущего пользователя.

#### Пример ответа GET:
```json
[
    {
        "id": 1,
        "creator": {
            "id": 1,
            "first_name": "Иван",
            "last_name": "Иванов",
            "role": "Диспетчер",
            "department": "Отдел логистики",
            "phone_num": "+1234567890"
        },
        "creation_date": "2023-10-10T10:10:10",
        "work_date": "2023-10-11",
        "work_time": "10:00:00",
        "reason": "Перевозка груза",
        "requested_vehicle": {
            "id": 1,
            "name": "Грузовик",
            "status": "Доступен"
        },
        "approved_vehicle": null,
        "assigned_driver": null,
        "status": "На рассмотрении"
    }
]
```

### 3.4. Заказы в процессе выполнения
- **URL**: /orders-in-progress/
- **Метод**: GET
- **Описание**: Получение списка заказов в процессе выполнения.

#### Пример ответа GET:
```json
[
    {
        "id": 1,
        "creator": {
            "id": 1,
            "first_name": "Иван",
            "last_name": "Иванов",
            "role": "Диспетчер",
            "department": "Отдел логистики",
            "phone_num": "+1234567890"
        },
        "creation_date": "2023-10-10T10:10:10",
        "work_date": "2023-10-11",
        "work_time": "10:00:00",
        "reason": "Перевозка груза",
        "requested_vehicle": {
            "id": 1,
            "name": "Грузовик",
            "status": "Доступен"
        },
        "approved_vehicle": {
            "id": 2,
            "name": "Фургон",
            "status": "Занят"
        },
        "assigned_driver": {
            "id": 2,
            "first_name": "Петр",
            "last_name": "Петров",
            "role": "Водитель",
            "department": "Отдел доставки",
            "phone_num": "+0987654321"
        },
        "status": "В процессе"
    }
]
```

## 4. Роли пользователей

### 4.1. Диспетчер

### 4.1.1. Заказы на рассмотрение
- **URL**: /dispatcher/orders-to-review/
- **Метод**: GET
- **Описание**: Получение списка заказов на рассмотрение диспетчером.

##### Пример ответа GET:
```json
[
    {
        "id": 1,
        "creator": {
            "id": 1,
            "first_name": "Иван",
            "last_name": "Иванов",
            "role": "Диспетчер",
            "department": "Отдел логистики",
            "phone_num": "+1234567890"
        },
        "creation_date": "2023-10-10T10:10:10",
        "work_date": "2023-10-11",
        "work_time": "10:00:00",
        "reason": "Перевозка груза",
        "requested_vehicle": {
            "id": 1,
            "name": "Грузовик",
            "status": "Доступен"
        },
        "approved_vehicle": null,
        "assigned_driver": null,
        "status": "На рассмотрении"
    }
]
```

### 4.1.2. История заказов диспетчера
- **URL**: /dispatcher/order-history/
- **Метод**: GET
- **Описание**: Получение истории заказов диспетчера.

#### Пример ответа GET:
```json
[
    {
        "id": 1,
        "creation_date": "2023-10-10T10:10:10",
        "work_date": "2023-10-11",
        "work_time": "10:00:00",
        "reason": "Перевозка груза",
        "status": "На рассмотрении",
        "requested_vehicle": {
            "id": 1,
            "name": "Грузовик",
            "status": "Доступен"
        }
    }
]
```

### 4.2. Начальник

### 4.2.1. Заказы на рассмотрение
- **URL**: /chief/orders-to-review/
- **Метод**: GET
- **Описание**: Получение списка заказов на рассмотрение начальником.

#### Пример ответа:
```json
[
    {
        "id": 2,
        "creation_date": "2023-10-11T11:11:11",
        "work_date": "2023-10-12",
        "work_time": "12:00:00",
        "reason": "Перевозка материалов",
        "status": "На рассмотрении",
        "requested_vehicle": {
            "id": 2,
            "name": "Фургон",
            "status": "Занят"
        }
    }
]
```

### 4.2.2. История заказов начальника
- **URL**: /chief/order-history/
- **Метод**: GET
- **Описание**: Получение истории заказов начальника.

#### Пример ответа:
```json
[
    {
        "id": 3,
        "creation_date": "2023-10-12T12:12:12",
        "work_date": "2023-10-13",
        "work_time": "13:00:00",
        "reason": "Транспортировка оборудования",
        "status": "Одобрено",
        "requested_vehicle": {
            "id": 3,
            "name": "Минивэн",
            "status": "Доступен"
        }
    }
]
```

### 4.3. Водитель

### 4.3.1. Расписание водителя
- **URL**: /driver/schedule/
- **Метод**: GET
- **Описание**: Получение расписания водителя.

#### Пример ответа:
```json
[
    {
        "id": 1,
        "creation_date": "2023-10-10T10:10:10",
        "work_date": "2023-10-11",
        "work_time": "10:00:00",
        "reason": "Перевозка груза",
        "status": "На рассмотрении",
        "requested_vehicle": {
            "id": 1,
            "name": "Грузовик",
            "status": "Доступен"
        },
        "approved_vehicle": null,
        "assigned_driver": {
            "id": 1,
            "first_name": "Иван",
            "last_name": "Иванов",
            "role": "Водитель",
            "department": "Отдел транспорта",
            "phone_num": "+1234567890"
        }
    }
]
```

## 5. Управление транспортными средствами

### 5.1. Управление транспортными средствами
- **URL**: /manage-vehicles/
- **Метод**: GET, PUT
- **Описание**: Получение списка и обновление транспортных средств.

#### Пример ответа GET:
```json
[
    {
        "id": 1,
        "name": "Грузовик",
        "status": "Доступен"
    },
    {
        "id": 2,
        "name": "Автобус",
        "status": "Занят"
    }
]
```

#### Пример запроса PUT:
```json
{
    "id": 2,
    "status": "Доступен"
}
```

#### Пример ответа PUT:
```json
{
    "id": 2,
    "name": "Автобус",
    "status": "Доступен"
}
```

## 6. Аутентификация

### 6.1. Получение JWT-токена
- **URL**: /jwt-token-auth/
- **Метод**: POST
- **Описание**: Получение JWT-токена для аутентификации.

#### Пример запроса POST:
```json
{
    "username": "user123",
    "password": "password123"
}
```

#### Пример ответа POST:
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 6.2. Обновление JWT-токена
- **URL**: /jwt-token-refresh/
- **Метод**: POST
- **Описание**: Обновление JWT-токена.

#### Пример запроса POST:
```json
{
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

#### Пример ответа POST:
```json
{
    "access_token": "new_access_token_value"
}
```