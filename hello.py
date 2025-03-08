from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

class registerData():
    def __init__(self, nome, email, password):
        self.nome = nome
        self.email = email
        self.password = md5_string(password)

lista_alunos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    print(request.method)
    if request.method == "POST":
        data = request.json
        data = registerData(data['nome'], data['email'], data['pass'])
        lista_alunos.append(data)
        # sendToDB(data)
    return render_template('register.html', faculdade='FECAF')

@app.route('/listUser')
def listUser():

    return render_template('list_user.html', faculdade='FECAF', alunos=lista_alunos)

def sendToDB():
    pass

def md5_string(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

# app.run()