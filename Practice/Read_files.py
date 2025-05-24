import csv
import json

file_path_txt = 'output.txt'
file_path_csv = 'CSV.csv'
file_path_json = 'JSON.json'

# try:
#     with open(file_path_txt, 'r') as file:
#         content_txt = file.read()
#         print(content_txt)
# except:
#     print('file kanum')

try:
    with open(file_path_csv, 'r') as file:
        content_csv = csv.reader(file)
        for line in content_csv:
            print(line)
except:
    print('file kanum')

# try:
#     with open(file_path_json, 'r') as file:
#         content_json = json.load(file)
#         print(content_json["Anush"])
# except:
#     print('file kanum')