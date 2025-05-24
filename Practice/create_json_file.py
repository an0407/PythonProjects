import json
file_path = 'JSON.json'
json_data = {
         "Anush": {'phone':9345998417,'email':'anushmn2004@gmail.com'},
         "Preethi": {'phone':9677260179, 'email':'prenarsi2002@gmail.com'},
         "Narsi": {'phone':9940058378, 'email': 'narsivard@gmail.com'}
       }

with open(file_path, 'a') as file:
    json.dump(json_data, file, indent=4)
    print(f"File '{file_path}' was created.")
