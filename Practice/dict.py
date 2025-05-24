dict = {
         "Anush": {'phone':9345998417,'email':'anushmn2004@gmail.com'},
         "Preethi": {'phone':9677260179, 'email':'prenarsi2002@gmail.com'},
         "Narsi": {'phone':9940058378, 'email': 'narsivard@gmail.com'}
       }
for name in dict:
    print(f"{name}'s contact info:")
    print(f"email: {dict[name]['email']}")
    print(f"phone: {dict[name]['phone']}\n")