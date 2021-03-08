# DBIS-1-Lab1

Програма завантажує інформацю з файлів Odata2019File.csv та Odata2020File.csv у базу даних, і за допомогою SELECT запиту генерує файл Result.csv, де 
записані найгірші бали з Історії України у кожному регіоні у 2020 та 2019 роках серед тих кому було зараховано тест.

Для під’єднаяння до бази даних необхідно відредагувати інформацію в файлі database.ini:
[postgresql]
host=localhost
database=%dbname%
user=%username%
password=%dbpass%
Де dbname - назва бази даних, dbpass - пароль від бази даних, а username - назва користувача бази даних

У програмі введена можливіть "вронити" базу даних для початку з чистого листа та можливість ввести вірогідність того, що зв’язок з базою даних перерветься, 
щоб симулювати помилку. Після помилки програма може бути запущена ще раз і в цьому випадку вона продовжить запис без дублікатів та втрати даних. 

У файлі upload_time.txt зберігаються записи того, скільки програма витратила часу на завантаження інформації з кожного .csv файлів.
Під час роботи програма створює файл log.txt. Цей файл необхідний для того, щоб відслідковувати прогрес завантаження інформації у базу даних та, у разі помилки, 
продовжити завантаження даних без втрати рядків та дублікатів
