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

if __name__ == "__main__":
  #initDetection()
  app.run()