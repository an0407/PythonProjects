import csv

csv_data = [['Name', 'Age', 'Job'],['Bob', 5, 'Builder'],['Dhoni', 43, 'Cricketer'],['Oggy',20, 'Unemployed']]
file_path = 'CSV.csv'
with open(file_path, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
    print(f"File '{file_path}' was created.")