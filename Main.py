import requests
import time
import random
import pyfiglet

logo = pyfiglet.figlet_format("incress Probot xp By Ghalwash")
print(logo)
print('Old Version ==> V1.0')
print("")


choice = input('Choose an option:\n1. Enter data manually\n2. Import data from file\n')

if choice == '1':
    token = input('Enter your token: ')
    channel_id = input('Enter the channel ID: ')
    timeout = float(input('Enter your Timeout per Message (in seconds): '))
elif choice == '2':
    with open('Data.txt', 'r') as data_file:
        token = data_file.readline().strip()
        channel_id = data_file.readline().strip()
        timeout = float(data_file.readline().strip())
else:
    print('Invalid choice. Exiting...')
    exit()

# Open the file containing the strings
with open('x.txt', 'r') as f:
    # Read all lines from the file into a list
    lines = f.readlines()

c = 0
successful_attempts = 0
failed_attempts = 0

while True:
    # Select a random line from the list of lines
    random_line = random.choice(lines)
    
    payload = {
        'content': random_line
    }

    headers = {
        'Authorization': token
    }

    url = f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=50'
 
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f'[!] Message Num {c + 1} sent successfully')
        successful_attempts += 1
    else:
        print(f'[X] Failed to send message Num {c + 1}. Status code: {response.status_code}')
        failed_attempts += 1

    c += 1
    time.sleep(timeout)  # Wait for the specified seconds before sending the next message
