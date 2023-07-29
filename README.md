# Тестовое задание для стажера на позицию «Программист на языке Python»

Ссылка на проект на gitbuh: (https://github.com/roki0601/Test_task)

Реализовать HTTP-сервер для предоставления информации по географическим объектам.
Данные взять из географической базы данных GeoNames, по ссылке:

(http://download.geonames.org/export/dump/RU.zip)

Описание формата данных можно найти по ссылке:

(http://download.geonames.org/export/dump/readme.txt)


## Содержание
- [Задание](#задание)
- [Использование](#использование)
- [API](#api)

## Задание
Реализованный сервер должен предоставлять REST API сервис со следующими методами:

1.	Метод принимает идентификатор geonameid и возвращает информацию о городе.
   
2.	Метод принимает страницу и количество отображаемых на странице городов и возвращает список городов с их информацией.
   
3.	Метод принимает названия двух городов (на русском языке) и получает информацию о найденных городах, а также дополнительно: какой из них расположен севернее и одинаковая ли у них временная зона (когда несколько городов имеют одно и то же название, разрешать неоднозначность выбирая город с большим населением; если население совпадает, брать первый попавшийся)


## Дополнительные задания:
Дополнительные задания не обязательны к исполнению, и будут учитываться если очень большое количество кандидатов выполнили основное задание на отлично. Вы можете выполнять любую комбинацию из предложенных заданий.

•	Для 3-его метода показывать пользователю не только факт различия временных зон, но и на сколько часов они различаются.

•	Реализовать метод, в котором пользователь вводит часть названия города и возвращает ему подсказку с возможными вариантами продолжений.


## Использование

1. Клонируйте репозиторий на свой компьютер.
2. Установите все необходимые зависимости, выполнив команду `pip install -r requirements.txt`.
3. Запустите приложение, выполнив команду `python script.py`.
4. Перейдите в браузер по адресу `127.0.0.1:8000` и напишите свой запрос 

## API

### `GET /city/<int:geonameid>`

Это API-эндпоинт, который позволяет получить информацию о городе по его идентификатору geonameid.

При запросе методом GET на /city/<int:geonameid>, сервер обращается к словарю data, где хранится информация о городах. Если город с указанным geonameid есть в словаре, сервер возвращает данные о городе в формате JSON. В случае отсутствия города с указанным geonameid, сервер возвращает сообщение "City not found" и код ответа 404.

Данные о городах хранятся в словаре city, который содержит следующие поля:

`geonameid`: уникальный идентификатор города

`name`: название города

`asciiname`: название города в ASCII-кодировке

`alternatenames`: альтернативные названия города

`latitude`: широта города

`longitude`: долгота города

`feature class`: класс объекта (город, поселок и т.д.)

`feature code`: код объекта (город, столица и т.д.)

`country code`: код страны, в которой находится город

`cc2`: дополнительный код страны

`admin1 code`: код области, в которой находится город

`admin2 code`: код района, в котором находится город

`admin3 code`: код подрайона

`admin4 code`: код еще более низкого уровня административного деления

`population`: население города

`elevation`: высота над уровнем моря

`dem`: высота над уровнем моря в метрах, полученная из цифровой модели рельефа

`timezone`: часовой пояс города

`modification date`: дата последнего изменения информации о городе.


Пример запроса `http://127.0.0.1:8000/city/451854`

Ответ по запросу: `{"geocodeid": "451854", "name": "Shchemelinino", "asciiname": "Shchemelinino", "alternatenames": "Shchemelinino,Shhemelinino,Щемелинино", "latitude": "56.82786", "longitude": "34.84024", "feature class": "P", "feature code": "PPL", "country code": "RU", "cc2": "", "admin1 code": "77", "admin2 code": "", "admin3 code": "", "admin4 code": "", "population": "0", "elevation": "", "dem": "166", "timezone": "Europe/Moscow", "modification date": "2012-01-16"}`

### `GET /city`

Это API-эндпоинт, который позволяет получить список городов с возможностью пагинации.

При запросе методом GET на /city, сервер обрабатывает параметры запроса page и per_page, чтобы определить, какие города нужно вернуть. Параметр page указывает номер страницы, а параметр per_page - количество городов на странице. Если параметры не указаны, используются значения по умолчанию: page=1 и per_page=10.

Затем сервер создает список cities, в котором хранятся данные о городах. Для этого сервер обращается к словарю data и выбирает города по их порядковому номеру в словаре, который вычисляется с помощью списка data_id.

Далее сервер возвращает выбранные города в формате JSON. В данном случае используется json.dumps(cities, ensure_ascii=False).encode('utf8'), что означает, что возвращаемый результат будет содержать все города, но в виде JSON-строки, закодированной в UTF-8.


Пример запроса `http://127.0.0.1:8000/city?page=5&per_page=5`

Ответ по запросу `[{"geocodeid": "451767", "name": "Yegor’ye", "asciiname": "Yegor'ye", "alternatenames": "", "latitude": "57.02174", "longitude": "34.29403", "feature class": "P", "feature code": "PPL", "country code": "RU", "cc2": "", "admin1 code": "77", "admin2 code": "", "admin3 code": "", "admin4 code": "", "population": "0", "elevation": "", "dem": "268", "timezone": "Europe/Moscow", "modification date": "2011-07-09"}, {"geocodeid": "451768", "name": "Yefremovo", "asciiname": "Yefremovo", "alternatenames": "", "latitude": "57.06001", "longitude": "34.74787", "feature class": "P", "feature code": "PPL", "country code": "RU", "cc2": "", "admin1 code": "77", "admin2 code": "", "admin3 code": "", "admin4 code": "", "population": "0", "elevation": "", "dem": "188", "timezone": "Europe/Moscow", "modification date": "2011-07-09"}, {"geocodeid": "451769", "name": "Yavidovo", "asciiname": "Yavidovo", "alternatenames": "Javidovo,Yavidovo,Явидово", "latitude": "56.87068", "longitude": "34.51994", "feature class": "P", "feature code": "PPL", "country code": "RU", "cc2": "", "admin1 code": "77", "admin2 code": "", "admin3 code": "", "admin4 code": "", "population": "0", "elevation": "", "dem": "217", "timezone": "Europe/Moscow", "modification date": "2012-01-16"}, {"geocodeid": "451770", "name": "Yasnaya Polyana", "asciiname": "Yasnaya Polyana", "alternatenames": "", "latitude": "56.93054", "longitude": "34.54696", "feature class": "P", "feature code": "PPL", "country code": "RU", "cc2": "", "admin1 code": "77", "admin2 code": "", "admin3 code": "", "admin4 code": "", "population": "0", "elevation": "", "dem": "214", "timezone": "Europe/Moscow", "modification date": "2011-07-09"}, {"geocodeid": "451771", "name": "Yasnaya Polyana", "asciiname": "Yasnaya Polyana", "alternatenames": "", "latitude": "56.90599", "longitude": "34.97555", "feature class": "P", "feature code": "PPL", "country code": "RU", "cc2": "", "admin1 code": "77", "admin2 code": "", "admin3 code": "", "admin4 code": "", "population": "0", "elevation": "", "dem": "185", "timezone": "Europe/Moscow", "modification date": "2011-07-09"}, {"geocodeid": "451772", "name": "Yakutino", "asciiname": "Yakutino", "alternatenames": "", "latitude": "56.99404", "longitude": "34.9857", "feature class": "P", "feature code": "PPL", "country code": "RU", "cc2": "", "admin1 code": "77", "admin2 code": "", "admin3 code": "", "admin4 code": "", "population": "0", "elevation": "", "dem": "159", "timezone": "Europe/Moscow", "modification date": "2011-07-09"}]`

### `GET /cities`

Это API-эндпоинт, который позволяет получить информацию о двух городах с возможностью сравнения.

При запросе методом GET на /cities, сервер обрабатывает параметры запроса city1_name и city2_name, которые содержат названия двух городов для сравнения. Названия городов передаются транслитом и извлекаются с помощью функции transliterate перед тем, как использоваться для поиска в словаре data.

Затем сервер ищет города с указанными названиями в словаре data. Для каждого города находится информация о населении и сохраняется в переменные population_city1 и population_city2, соответственно, для определения того, какой из городов является более населенным. При этом для каждого города создается словарь с помощью функции generate_dict_city, в котором хранится информация о городе.

Если один из городов не найден, сервер возвращает сообщение "City not found" и код ответа 404.

Затем сервер определяет, какой из городов находится севернее. Если города находятся на одной широте, возвращается сообщение "Both cities are on the same latitude."

Далее сервер сравнивает часовые пояса городов и вычисляет разницу во времени между ними, сохраняя результат в переменной same_timezone. Если у городов одинаковые часовые пояса, в переменной same_timezone сохраняется значение True.

Наконец, сервер возвращает результат в виде JSON-объекта, содержащего информацию о двух городах (city1 и city2), названии севернее расположенного города (north_city_name) и информации о разнице во времени между часовыми поясами (same_timezone). Возвращаемый результат закодирован в JSON-строку, закодированную в UTF-8.


Пример запроса `http://127.0.0.1:8000/cities?city1_name=Москва&city2_name=Уфа`

Ответ по запросу `{"city1": {"geonameid": "524894", "name": "Moskva", "asciiname": "Moskva", "alternatenames": "Maskva,Moscou,Moscow,Moscu,Moscú,Moskau,Moskou,Moskovu,Moskva,Məskeu,Москва,Мәскеу", "latitude": "55.76167", "longitude": "37.60667", "feature class": "A", "feature code": "ADM1", "country code": "RU", "cc2": "", "admin1 code": "48", "admin2 code": "", "admin3 code": "", "admin4 code": "", "population": "13010112", "elevation": "", "dem": "161", "timezone": "Europe/Moscow", "modification date": "2023-01-12"}, "city2": {"geonameid": "479561", "name": "Ufa", "asciiname": "Ufa", "alternatenames": "Ephu,Oefa,Oufa,Ouffa,Owfa,UFA,Uf,Ufa,Uffa,Ufà,Ufá,Ufа,Upo,awfa,ufa,upa,wu fa,Ĕпхӳ,Оуфа,Уфа,Үфі,Өфө,Ӱпӧ,Ուֆա,אופה,أوفا,اوفا,ऊफ़ा,უფა,ウファ,烏法,우파", "latitude": "54.74306", "longitude": "55.96779", "feature class": "P", "feature code": "PPLA", "country code": "RU", "cc2": "", "admin1 code": "08", "admin2 code": "", "admin3 code": "", "admin4 code": "", "population": "1120547", "elevation": "", "dem": "158", "timezone": "Asia/Yekaterinburg", "modification date": "2022-09-17"}, "north_city_name": "Moskva", "same_timezone": -2.0}`

### `GET /suggest-city`

Это API-эндпоинт, который предлагает варианты городов, которые начинаются с заданной подстроки.

При запросе методом GET на /suggest-city, сервер обрабатывает параметр запроса name, который содержит часть названия города. Название города передается транслитом и извлекается с помощью функции transliterate.

Затем сервер проходит по всем элементам словаря data и ищет города, название которых начинается с указанной подстроки. Если находится соответствующий город, его название добавляется в список suggestions. Также в список добавляются города, в названии которых указана подстрока, но перед ней стоит пробел.

Если подстрока name не была передана, сервер возвращает сообщение об ошибке.

Наконец, сервер возвращает результат в виде JSON-объекта, содержащего список предложенных городов (suggestions). Возвращаемый результат закодирован в JSON-строку, закодированную в UTF-8.

Пример запроса `http://127.0.0.1:8000/suggest-city?name=Уф`

Ответ на запрос `{"suggestions": ["Verkhnyaya Uftyuga", "Stantsiya Uftyuga", "Uftyuga", "Uftyuga", "Uftyuga", "Uftyuga", "Uftyuga", "Ufin'ya", "Ufimtsy", "Ufimskoye Plato", "Ufimskiy Rayon", "Sovkhoz Ufimskiy", "Ufimskiy", "Ufimskiy", "Ufimskiy", "Ufimskiy", "Ufimka", "Ufa-Shigiri", "Ufaleyka", "Ufa", "Ufa", "Nizhniy Ufaley", "Urochishche Ufimovka", "Uftyuga", "Ufimka", "Verkhniy Ufaley", "Ozero Ufimskoye", "Ufimka", "Ufimskiy", "Ufimskiy", "Ufaleyskiy Khrebet", "Stantsiya Verkhniy Ufaley", "Ufa", "Ufimtsevo", "Gorod Verkhniy Ufaley", "Novaya Ufa", "Ufina", "Prud Verkhniy Ufaleyskiy", "Ufaleyka", "Malaya Ufaleyka", "Ufimtsevo", "Ufimka", "Novaya Ufa", "Novaya Ufa", "Ufa International Airport", "Gora Ufimka", "Ufa longwave broadcasting mast", "Ostanovochnyy Punkt Pravaya Ufimka", "Lesnichestvo Ufimskoye", "Baza Ufaneft'", "Ufa", "Ufa Railway Station", "Rechnoy Vokzal Ufa-Dva", "Ufimovskiy", "Ufimshchina", "Ufimtsevo", "Ufa Maximovka Airport", "Ostanovochnyy Punkt Ufimka", "Ufimka", "Stantsiya Ufimka", "Ufa", "Malaya Uftyuga", "Bol'shaya Uftyuga", "Uftyuga", "Ufimskiy Kamennyy Kar'yer", "Ufa-Arena", "Pamyatnik Zhertvam Ufimskoy Katastrofy 1989 Goda", "President Hotel Ufa", "Bashkortostan Ufa", "Azimut Ufa", "Hostel Rusland Ufa", "Ufa Northwest", "Hampton by Hilton Ufa", "Hilton Garden Inn Ufa Riverside", "Ufimskiy (selo)"]}`
