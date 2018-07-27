# Made with love by Karlpy
import requests
import csv
import json
import time

set_url = 'https://servicios.set.gov.py/eset-publico/ciudadano/recuperar'

# loop through all URLs
start_id = 1
last_id = 100000
# set sleep time between reqs, otherwise set to 0
sleep_time = 0.800

with open ('datos.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['cedula', 'nombres', 'apellidoPaterno', 'apellidoMaterno', 'nombreCompleto'])
    for id in range(start_id, last_id+1):
        payload = {"cedula": id}
        result = requests. get(set_url, params=payload)
        res_json = result.json()
        if(res_json["presente"] == False):
            print("No existe el nro de cedula")
        else:
            print(res_json["resultado"])
            writer.writerow(res_json["resultado"].values())
        time.sleep(sleep_time)