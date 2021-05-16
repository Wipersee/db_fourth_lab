from pymongo import MongoClient
import csv
from datetime import datetime, timedelta
from utils.consts import *
from utils.log import log_func
from utils.utils import get_env


def get_user_query(collection):
    """Варіант 7: Порівняти найкращий бал з Математики у 2020 та 2019 роках серед тих кому було зараховано тест"""
    user_query = collection.aggregate(
        [
            {"$match": {"mathTestStatus": "Зараховано"}},
            {"$group": {"_id": "$TestYear", "maximum": {"$max": "$mathBall100"}}},
        ]
    )
    with open("resultQuery.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["_id", "maximum"])
        writer.writeheader()
        for data in user_query:
            writer.writerow(data)
    log_func.info("COPY TO CSV SUCCESSFUL")


def create_tables(conn):
    log_func.info("Creating table")
    connections = conn.list_collection_names()
    if "zno_table" in connections:
        col1 = conn.zno_table
    else:
        col1 = conn.zno_table
    if "last_row_table" in connections:
        col2 = conn.last_row_table
    else:
        col2 = conn.last_row_table
        col2.insert_one({"execution_time": 0, "rows": 0, "year": 2019})

    log_func.info("Tables created")
    return (col1, col2)


def insert_data(col1, col2, csv_filename, year, last_row_number, start_time):
    previous_stack_time = start_time
    log_func.info(f"Inserting data from {csv_filename}")
    with open(csv_filename, encoding="cp1251") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")

        i = 0
        arr = []
        col2.update_one({}, {"$set": {"year": year}})
        for row in csv_reader:
            i += 1

            if i <= last_row_number:
                continue

            try:
                row["TestYear"] = year
                arr.append(row)
            except Exception as e:
                log_func.error(f"Something went wrong details ->: {e}")
                return 1

            if i % 50 == 0:
                now = datetime.now()
                try:
                    col1.insert_many(arr)
                    col2.update_one(
                        {},
                        {
                            "$set": {
                                "rows": i,
                            },
                            "$inc": {
                                "execution_time": (
                                    now - previous_stack_time
                                ).microseconds
                            },
                        },
                    )
                    print(i)
                    arr = []
                except Exception as e:
                    log_func.error(f"Connection with db is broken: {e}")
                    raise Exception
                previous_stack_time = now
    try:
        col1.insert_many(arr)
        col2.update_one(
            {},
            {
                "$set": {
                    "rows": i,
                },
                "$inc": {"execution_time": (now - previous_stack_time).microseconds},
            },
        )
        print(i)
        arr = []
    except Exception as e:
        log_func.error(f"Connection with db is broken: {e}")
        raise Exception
    log_func.info(f"Inserting from {csv_filename} is finished")


def main():
    start_time = datetime.now()
    log_func.info(f"Start time {start_time}")
    client = MongoClient(port=int(get_env("PORT")))
    db = client["lab4"]
    col1, col2 = create_tables(db)

    try:
        last_row = col2.find_one()
        row_number = last_row["rows"]
        file_year = last_row["year"]
    except Exception as e:
        log_func.warning(f"Cannot get data from {LAST_ROW_TABLE}: {e}")
        file_year = YEARS[0]
        row_number = 0

    log_func.info(
        f"Starting inserting from {row_number} row from file for {file_year} year"
    )
    if file_year:
        index = YEARS.index(file_year)
        for year in YEARS[index:]:
            insert_data(
                col1, col2, f"Odata{year}File.csv", year, row_number, start_time
            )
            row_number = 0
    else:
        for year in YEARS:
            insert_data(
                col1, col2, f"Odata{year}File.csv", year, row_number, start_time
            )
            row_number = 0

    get_user_query(col1)
    inserting_time = col2.find_one()
    end_time = datetime.now()
    log_func.info(f"End time {end_time}")
    log_func.info(
        f"Inserting executing time {timedelta(microseconds=inserting_time['execution_time'])}"
    )
    log_func.info("Program is finished")


if __name__ == "__main__":
    main()
