GKS = 'ГКС'
LES = 'ЛЭС'
SHMTRISO = 'СХМТРиСО'
AIMO = 'АиМО'
HOSTEL = 'Общежитие'
VPO = 'ВПО'
EVS = 'ЭВС'
SS = 'Связь'
KZ = 'КЗ'
ZK = 'ЗК'

DEPARTMENT_CHOICES = (
    (GKS, 'ГКС'),
    (LES, 'ЛЭС'),
    (SHMTRISO, 'СХМТРиСО'),
    (HOSTEL, 'Общежитие'),
    (VPO, 'ВПО'),
    (EVS, 'ЭВС'),
    (SS, 'Связь'),
    (KZ, 'КЗ'),
    (ZK, 'ЗК')
)
CUSTOMER = 'Заказчик'
DISPATCHER = 'Диспетчер'
DRIVER = 'Водитель'
BOSS = 'Начальник'

ROLE_CHOICES = (
    (CUSTOMER, 'Заказчик'),
    (DISPATCHER, 'Диспетчер'),
    (DRIVER, 'Водитель'),
    (BOSS, 'Начальник')
)

NOT_CONSIDERED = 'Не рассматривалась'
UNDER_CONSIDERATION = 'Находится на рассмотрении'
REJECTED = 'Отклонена'
ACCEPTED = 'Принята'

ORDER_STATUS_CHOICES = (
    (NOT_CONSIDERED, 'Не рассматривалась'),
    (UNDER_CONSIDERATION, 'Находится на рассмотрении'),
    (REJECTED, 'Отклонена'),
    (ACCEPTED, 'Принята')
)

AVAILABLE = 'Доступно'
UNAVAILABLE = 'Недоступно'

TRANSPORT_STATUS_CHOICES = (
    (AVAILABLE, 'Доступно'),
    (UNAVAILABLE, 'Недоступно'),
)
