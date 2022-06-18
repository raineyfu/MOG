from flask import Flask, render_template, request
import os
import base64
import json


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/journal')
def journal():
    return render_template('journal.html')

@app.route('/signupSubmit', methods = ['GET', 'POST'])
def signup():
    if (request.method == "POST" or request.method == "GET"):
        username = request.get_json()['username']
        password = request.get_json()['password']

        data = []
        with open("login.json") as json_file:
            data = json.load(json_file)
            for person in data: 
                print(person["username"])
                if (person["username"] == username):
                    return json.dumps("userTaken")
                else:
                    person["login"] = "false"
        
        newEntry = {
            "username": username,
            "password": password,
            "login": "true"}

        data.append(newEntry)

        with open('login.json', 'w') as writeFile:
            json.dump(data, writeFile)
        return json.dumps("success")
        
@app.route('/loginSubmit', methods = ['GET', 'POST'])
def loginSubmit():
    if (request.method == "POST" or request.method == "GET"):
        username = request.get_json()['username']
        password = request.get_json()['password']

        data = []
        with open("login.json") as json_file:
            data = json.load(json_file)
            for person in data: 
                if (person["username"] == username):
                    if (person["password"] == password):
                        person["login"] = "true"
                        with open('login.json', 'w') as writeFile:
                            json.dump(data, writeFile)
                        return json.dumps("loginSuccess")
                    else:
                        return json.dumps("loginFailure")
                person["login"] = "false"

        with open('login.json', 'w') as writeFile:
            json.dump(data, writeFile)
        return json.dumps("noUser")

@app.route('/getJournalEntry', methods = ['GET'])
def getJournalEntry():
    output = ""
    username = ""
    if (request.method == "GET"):
        with open("login.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["login"] == "true"):
                    username = person["username"]
        
        with open("journal.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["username"] == username):
                    output = person["journal"]
    return json.dumps(output)

@app.route('/saveJournalEntry', methods = ['POST'])
def saveJournalEntry():
    username = ""
    if (request.method == "POST"):
        journalInput = request.get_json()['input']
        with open("login.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["login"] == "true"):
                    username = person["username"]
        print("username")
        with open("journal.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["username"] == username):
                    person['journal'] = journalInput
                    with open('journal.json', 'w') as writeFile:
                        json.dump(data, writeFile)
                        return json.dumps("")
    return json.dumps("") 

@app.route('/saveJournalTitle', methods = ['POST'])
def saveJournalTitle():
    username = ""
    if (request.method == "POST"):
        journalInput = request.get_json()['input']
        with open("login.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["login"] == "true"):
                    username = person["username"]
                    
        with open("journal.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["username"] == username):
                    person['title'] = journalInput
                    with open('journal.json', 'w') as writeFile:
                        json.dump(data, writeFile)
                        return json.dumps("")
    return json.dumps("") 

@app.route('/getJournalTitle', methods = ['GET'])
def getJournalTitle():
    output = ""
    username = ""
    if (request.method == "GET"):
        with open("login.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["login"] == "true"):
                    username = person["username"]
        
        with open("journal.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["username"] == username):
                    output = person["title"]
    return json.dumps(output)
if __name__ == "__main__":
  #initDetection()
  app.run()