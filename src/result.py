import json
from pyOtus.files import JSON_FILE_PATH, CSV_FILE_PATH
from json_reader import json_reader
from json_writer import json_writer
from csv_reader import csv_reader

json_data_list = json_reader(JSON_FILE_PATH)
csv_data_list = csv_reader(CSV_FILE_PATH)

users_list = json_writer(json_data_list)
books_list = csv_data_list

num_users = len(users_list)
num_books = len(books_list)
book_index = 0
updated_users_list = []

while num_books > 0:
    for i, person in enumerate(users_list):
        if num_books == 0:
            break

        person["books"].append(books_list[book_index])
        book_index = (book_index + 1) % num_books
        num_books -= 1
        updated_users_list.append(person)


with open("result.json", "w") as outfile:
    json.dump(updated_users_list, outfile, indent=4)
