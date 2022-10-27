
import csv
import json

arr = []
with open('process_cycles_very_light.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        obj = {
            'imageName': row[0],
            'imagePath': row[1],
            'osPid': row[2],
            'osParentPid': row[3],
            'timestampBegin': row[4],
            'timestampEnd': row[5],
            'cycles': row[6],
            'clockRate': row[7],
        }
        arr.append(obj)

jsonStr = json.dumps(arr)
with open('json_out.txt', "w", encoding='utf-8') as out:
    out.write(jsonStr)

choice = input('Send request to server? y/n: ')
if choice == 'y':
    import requests
    servAddr = 'http://127.0.0.1:8000/records/'

    response = requests.post(servAddr, data=jsonStr)
    with open('json_server_response.html', "w", encoding='utf-8') as rhtml: 
        rhtml.write(response.text)
    print("Server response was saved to json_server_response.html")