from flask import Flask, jsonify, request
import sqlite3
import requests
import json



if __name__ == '__main__':

    # przykładowe dane zadania
    task = {
        'title': 'odebrac okulary',
        'description': 'odebrac okulary od optyka'
    }

    # dodawanie zadania do bazy danych
    #response = requests.post('http://127.0.0.1:5000/tasks', data=json.dumps(task), headers={'Content-Type': 'application/json'})
    response1 = requests.get('http://127.0.0.1:5000/tasks')

    if response1.status_code == 200:
        #print('Zadanie zostało pomyślnie dodane!')
        x = response1.text
        print(x)
    else:
        print('Nie udało się wykonać zadania.')