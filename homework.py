import csv
import os

import httpx

# JSONPlaceholder API url
url = "https://jsonplaceholder.typicode.com/users"

# HTTP GET so'rovi
response = httpx.get(url)

# JSON javobi
users = response.json()

# Folder nomi
folder_name = "users"

# CSV fayllarini saqlash uchun folder yaratish
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Har bir foydalanuvchi uchun CSV faylini yaratish
for user in users:
    # Foydalanuvchi ma'lumotlari
    user_id = user['id']
    username = user['username']
    email = user['email']
    phone = user['phone']
    website = user['website']
    company_name = user['company']['name']

    # CSV fayl nomi
    csv_file_name = f"{folder_name}/{username}.csv"

    # CSV faylini yaratish va ma'lumotlarni yozish
    with open(csv_file_name, mode='w', newline='') as csv_file:
        fieldnames = ['ID', 'Username', 'Email', 'Phone', 'Website', 'Company Name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({
            'ID': user_id,
            'Username': username,
            'Email': email,
            'Phone': phone,
            'Website': website,
            'Company Name': company_name
        })

    print(f"{csv_file_name} fayli yaratildi.")
