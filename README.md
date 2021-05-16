# Лабораторна робота №4 студента групи КМ-81 Піткевича Іллі

Перед виконанням програми додайте в корневу папку файли **_Odata2019File.csv_**, **_Odata2020File.csv_**

## Запуск програми

Для того, щоб запустити треба локально мати MongoDB. Також треба створити змінні середовища, де треба прописати порт на якому працює MongoDB. Після цього треба зробити python середовище та інсталювати всі пакети з `requirements.txt`. Потім просто запустити файл `main.py`, наприклад в Ubunut це команада - `python main.py`.

### Індивідуальне завдання

Завдання: `Варіант 7: Порівняти найкращий бал з Математики у 2020 та 2019 роках серед тих комубуло зараховано тест`
Програма виконує запит відповідно до завдання і записує результат у форматі _csv_ в файл `resultQuery.csv`.
**Результат:**

- максимальний бал
- рік

#### Приклад вмісту `resultQuery.csv`

| \_id | maximum |
| ---- | ------- |
| 2019 | 200     |
| 2020 | 200     |

### Log

Протягом усієї роботи програма записує свої дії у файл work_logs.log. Також на початку і в
кінці запису даних фіксується час, тому останній запис у цьому файлі — час виконання запису усіх даних з файлів до
таблиць.

## Результати виконання

### Таблиця

#### Перший рядки та стовпці з колекції ZNO_TABLE

| \_id                                   | outid                                  | birth | sextypename | regname               |
| -------------------------------------- | -------------------------------------- | ----- | ----------- | --------------------- |
| "0000341b-1bda-4386-a148-3d9613bbe324" | "0000333b-1b93-4386-a148-3d9613bbe324" | 2002  | "жіноча"    | "Донецька область"... |

#### Приклад таблиці LastRowTable

| execution_time | rows  | year |
| -------------- | ----- | ---- |
| 191147838      | 67050 | 2020 |

### Logs example

Приклад логів при двох падіннях бази в разних файлах

```
05-16-2021 15:09:14 INFO at row #108 Start time 2021-05-16 15:09:14.415235
05-16-2021 15:09:14 INFO at row #26 Creating table
05-16-2021 15:09:14 INFO at row #38 Tables created
05-16-2021 15:09:14 INFO at row #122 Starting inserting from 0 row from file for 2019 year
05-16-2021 15:09:14 INFO at row #44 Inserting data from Odata2019File.csv
05-16-2021 15:09:26 ERROR at row #84 Connection with db is broken: interrupted at shutdown, full error: {'ok': 0.0, 'errmsg': 'interrupted at shutdown', 'code': 11600, 'codeName': 'InterruptedAtShutdown'}
05-16-2021 15:09:42 INFO at row #108 Start time 2021-05-16 15:09:42.793094
05-16-2021 15:09:42 INFO at row #26 Creating table
05-16-2021 15:09:42 INFO at row #38 Tables created
05-16-2021 15:09:42 INFO at row #122 Starting inserting from 128400 row from file for 2019 year
05-16-2021 15:09:42 INFO at row #44 Inserting data from Odata2019File.csv
05-16-2021 15:10:08 INFO at row #103 Inserting from Odata2019File.csv is finished
05-16-2021 15:10:08 INFO at row #44 Inserting data from Odata2020File.csv
05-16-2021 15:10:23 ERROR at row #84 Connection with db is broken: interrupted at shutdown, full error: {'ok': 0.0, 'errmsg': 'interrupted at shutdown', 'code': 11600, 'codeName': 'InterruptedAtShutdown'}
05-16-2021 15:10:38 INFO at row #108 Start time 2021-05-16 15:10:38.748878
05-16-2021 15:10:38 INFO at row #26 Creating table
05-16-2021 15:10:38 INFO at row #38 Tables created
05-16-2021 15:10:38 INFO at row #122 Starting inserting from 150000 row from file for 2020 year
05-16-2021 15:10:38 INFO at row #44 Inserting data from Odata2020File.csv
05-16-2021 15:11:03 INFO at row #103 Inserting from Odata2020File.csv is finished
05-16-2021 15:11:06 INFO at row #22 COPY TO CSV SUCCESSFUL
05-16-2021 15:11:06 INFO at row #142 End time 2021-05-16 15:11:06.343215
05-16-2021 15:11:06 INFO at row #143 Inserting executing time 0:01:11.745414
05-16-2021 15:11:06 INFO at row #146 Program is finished

```

**_Як видно час на виконання достатньо швидкий, імпортувалося 733112 рядків, тобто 100% csv файлу_**
