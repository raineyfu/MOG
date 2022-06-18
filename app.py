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
                else:
                    person["login"] = "false"

        with open('login.json', 'w') as writeFile:
            json.dump(data, writeFile)
        return json.dumps("noUser")

@app.route('/getJournalEntry', methods = ['GET', 'POST'])
def getJournalEntry():
    output = ""
    username = ""
    if (request.method == "GET" or request.method == "POST"):
        date = request.get_json()["date"]
        with open("login.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["login"] == "true"):
                    username = person["username"]
        
        with open("journal.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["username"] == username):
                    for journal in person["journals"]:
                        if (journal["date"] == date):
                            return json.dumps(journal)
    return ({"title": "", "journal": ""})

@app.route('/saveJournalEntry', methods = ['POST'])
def saveJournalEntry():
    username = ""
    if (request.method == "POST"):
        journalInput = request.get_json()['input']
        title = request.get_json()['title']
        date = request.get_json()["date"]
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
                    for journal in person["journals"]:
                        if (journal["date"] == date):
                            journal["journal"] = journalInput
                            with open('journal.json', 'w') as writeFile:
                                json.dump(data, writeFile)
                                return json.dumps("")
                    person["journals"].append({"date": date, "journal": journalInput, "title": title})
                    with open('journal.json', 'w') as writeFile:
                                json.dump(data, writeFile)
                                return json.dumps("")
    return json.dumps("") 

@app.route('/saveJournalTitle', methods = ['POST'])
def saveJournalTitle():
    username = ""
    if (request.method == "POST"):
        journalInput = request.get_json()['input']
        title = request.get_json()["title"]
        date = request.get_json()["date"]
        with open("login.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["login"] == "true"):
                    username = person["username"]

        with open("journal.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["username"] == username):
                    for journal in person["journals"]:
                        if (journal["date"] == date):
                            journal["title"] = journalInput
                            with open('journal.json', 'w') as writeFile:
                                json.dump(data, writeFile)
                                return json.dumps("")
                    person["journals"].append({"date": date, "journal": journalInput, "title": title})
                    with open('journal.json', 'w') as writeFile:
                                json.dump(data, writeFile)
                                return json.dumps("")
    return json.dumps("") 

@app.route('/getJournalTitle', methods = ['GET', "POST"])
def getJournalTitle():
    output = ""
    username = ""
    if (request.method == "GET" or request.method == "POST"):
        date = request.get_json()["date"]
        with open("login.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["login"] == "true"):
                    username = person["username"]
        
        with open("journal.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["username"] == username):
                    for journal in person["journals"]:
                        if (journal["date"] == date):
                            output = journal["title"]
    return json.dumps(output)


@app.route('/getCurrentUser', methods=['GET', 'POST'])
def getCurrentUser():
    if (request.method == "GET" or request.method == "POST"):
        with open("login.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["login"] == "true"):
                    return json.dumps(person["username"])
    return json.dumps("")

@app.route('/logout', methods=['GET'])
def logout():
    if (request.method == "GET"):
        with open("login.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["login"] == "true"):
                    person["login"] = "false"
        
        return json.dumps("")
        
@app.route('/getJournalNames', methods=["GET"])
def getJournalNames():
    if (request.method == "GET"):
        with open("login.json") as json_file:
            data = json.load(json_file)
            for person in data:
                if (person["login"] == "true"):
                    return json.dumps(person["journals"])
    return json.dumps([])
if __name__ == "__main__":
  #initDetection()
  app.run()