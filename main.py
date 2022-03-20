import requests

print('***  Example: http://example.com/  ***')
url = input('Enter url: ')
admins = open('list.txt')
print('Searching...')
for i in admins:
    full_url = url + i
    status = requests.get(full_url)
    if status.status_code == 200:
        print(f'[*] ADMIN FOUND: {full_url}')