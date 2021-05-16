from pymongo import MongoClient

client = MongoClient(port=27017)
db = client["lab4"]
db.zno_table.drop()
db.last_row_table.drop()
