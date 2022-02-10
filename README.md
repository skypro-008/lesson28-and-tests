# Урок 28
Для начала работы скопируйте репозиторий на локальную машину:
c помощью команды в терминале

`https://github.com/skypro-008/lesson28-and-tests.git`

Откройте с клонированный репозиторий в PyCharm.

### Cоздайте виртуальное окружение:

#### Простой вариант:
Pycharm может предложить вам сделать это после того, как вы откроете папку с проектом.
В этом случае после открытия папки с проектом в PyCharm
Появляется всплывающее окно, Creating virtual envrironment c тремя полями.
В первом поле выбираем размещение папки с виртуальным окружением, как правило, это папка venv
в корне проекта
Во втором поле выбираем устанавливаемый интерпретатор по умолчанию (можно оставить без изменений)
В 3 поле выбираем список зависимостей (должен быть выбран файл requirements.txt, 
находящийся в корне папки проекта)

#### Если этого не произошло, тогда следует выполнить следующие действия вручную:
#### Установка виртуального окружения:
1. Во вкладке File выберите пункт Settings
2. В открывшемся окне, с левой стороны найдите вкладку с именем
вашего репозитория (Project: lesson28-and-tests)
3. В выбранной вкладке откройте настройку Python Interpreter
4. В открывшейся настройке кликните на значек ⚙ (шестеренки) 
расположенный сверху справа и выберите опцию Add
5. В открывшемся окне слева выберите Virtualenv Environment, 
а справа выберите New Environment и нажмите ОК

#### Установка зависимостей:
Для этого можно воспользоваться графическим интерфейсом PyCharm,
который вам предложит сделать это как только вы откроете файл с заданием.

Или же вы можете сделать это вручную, выполнив следующую команду в терминале:
`pip install -r requirements.txt`

#### Настройка виртуального окружения завершена!
### Подготовка проекта django
После того, как Вы установили все зависимости, необходимо подготовить django к работе:
для этого нам потребуется:

1. Иметь возможность запуска на локальной машине docker-контейнера 
(необходимо для запуска контейнера с базы данных):
- переходим в каталог `postgres_l28` и выполняем команду `docker-compose up`.

2. Выполнить необходимые команды для подготовки базы данных к работе:
Текущий проект уже содержит настроенную базу данных, но пока еще она 
пустая, не содержит таблиц, а всё её наполнение
находится в фикстурах (в django - файлы в формате json содержащие данные для наполнения БД).

Для начала нужно создать необходимые таблицы в базе данных с помощью команды:
python3 manage.py migrate (находясь в папке `my_project_part_1`)
а затем выполнить команду `python3 manage.py loadall` из этой же директории
   (для загрузки всех объектов в базу данных).
Если команда выполнена успешна вы увидите следующий текст:
```
Installed 2 object(s) from 1 fixture(s)
Installed 6 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 1 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 11 object(s) from 1 fixture(s)
```
После того как все подготовительные мероприятия выполнены - можно приступать к работе.

Первое, что необходимо сделать - изучите представленный проект.
Здесь одно джанго-приложение соответствует одному заданию тренажера
ознакомится с адресами преложений можно всё также в файле `my_project/urls.py`
*Обратите внимание, что часть адресов, представленных в заданиях ниже уже реализованы.
и здесь Вам требуется только дополнить их соответствующим образом.*


### Порядок выполнения заданий

## Часть 1. my_project_part_1

### Задание opinion ("Ваше мнение очень важно для нас")
Перейдите в файл tours/models.py и напишите модель в соответствии со спецификацией
указанной в TODO - комментариях

для проверки запустите: `python3 manage.py test tours` из директории `my_project_part_1`

### Задание edits ("Снова правки")
Перейдите в файл edits/models.py и напишите модель в соответствии со спецификацией
указанной в TODO - комментариях.

### Задание discounts ("Скидочки")
Дана следующая документация
#### GET /discount
```[
 {
     "id": 1,
     "tour": 1,
     "category": "promo",
     "discount": 10,
     "code": "SkyPro",
     "starts_at": "",
     "ends_at": ""
 },
 ...
]
```
#### GET /discount/1
```
{
   "id": 1,
   "tour": 1,
   "category": "promo",
   "discount": 10,
   "code": "SkyPro",
   "starts_at": "",
   "ends_at": ""
}
```
Внесите соответствующие изменения в модель Discounts приложения discounts,
а также напишите view-функции и настройте urls.py так,
чтобы возвращаемые данные соответcтвовали примерам, представленным выше.


### Задание along_neva_channels ("По каналам Невы")
Дана следующая документация:
#### GET /neva_tours/
```
[
 {
     "id": 1,
     "name": "По каналам Невы",
     "starts_at": "",
     "ends_at": "",
     "points": [
		name: “Канал Грибоедова”,
		name: "Синий мост"
		...
	]
 },
 ...
]
```
 
#### GET /neva_tours/1
```
 {
     "id": 1,
     "name": "По каналам Невы",
     "starts_at": "",
     "ends_at": "",
     "points": [
		name: “Канал Грибоедова”,
		name: "Синий мост"
		...
	]
 }
```
Внесите соответствующие изменения в модель Tour приложения along_neva_channels,
а также напишите view-функции и настройте urls.py так,
чтобы возвращаемые данные соответcтвовали примерам, представленным выше.


### Задание feedback ("Оставьте отзыв")
Ознакомьтесь с приложением feedback.
Используя знания из урока, напишите ручку для создания отзыва.
Ссылка на тур передается как число, и возвращаться должно тоже число. Дата публикации не обрабатывается.
Попробуйте добавить новый отзыв с помощью `POST` запроса на адрес `/feedback/ `
```
{
    "tour": 1,
    "author": "Я",
    "content": "Мне понравилось! Отличный тур",
    "rate": 4,
    "is_published": true
}
```

Если всё хорошо, Вы должны получить такой ответ:
```
{
    "id": 1,
    "author": "test",
    "tour": 1,
    "content": "Мне понравилось! Отличный тур",
    "rate": 4,
    "published_at": null,
    "is_published": true
}
```
(Доступные ID можно подсмотреть в фикстурах ("`fixtures/feedback_tours.json", "fixtures/feedback_cities.json`"))

### Задание forgotten ("Что-то забыли?")
Ознакомьтесь с приложением forgotten
Используя знания из урока, напишите эндпоинт для редактирования комментария. 
Редактировать можно только текст (content) и рейтинг (rate).
А вот возвращать надо все поля. 
Тур, как и раньше, возвращается целым числом — id соответствующей модели.
Если вы выполнили команду `python3 manage.py loadall` то в этом приложении в базе уже имеется одно ревью, которое
можно попробовать отредактировать. Для редактирования мы будем использовать url `feedback-update/<pk:int>`


### Задание moderation ("Модерация")
Ознакомьтесь с приложением moderation
Используя знания из урока, напишите эндпоинт, который удаляет отзыв.
Для удаления используйте, пожалуйста, url `feedback-delete/<pk:int>`
Для практики в базу данных залито 11 объектов (значения id с 1 по 11)
Если для эксперементов этого будет недостаточно - пополните базу с помощью команды
`python3 manage.py loadall`


## Часть 2
    в разработке


Переходите к запуску тестов только после выполнения всех заданий.
Для запуска тестов воспользуйтесь командой `python3 manage.py test` (находясь в папке `my_project_part_1`)
Также вы можете проверить правильность работы приложения - для этого используйте команду
`python3 manage.py test <app>`
