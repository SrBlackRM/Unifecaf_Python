from flask import Flask, render_template, request
from connection import mydb, mycursor
import hashlib

app = Flask(__name__)

class registerData():
    def __init__(self, nome, email, password):
        self.nome = nome
        self.email = email
        self.password = password
    
    def crypto_password(self, password):
        return md5_string(password)

# ROTAS
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == "POST":
        data = request.json
        print(f'nome: {data['nome']}\nemail: {data['email']}\nsenha: {data['pass']}')
        data = registerData(data['nome'], data['email'], data['pass'])
        sendRegisterDataToDB(data)
    return render_template('register.html', faculdade='FECAF')


@app.route('/listUser')
def listUser():
    lista_alunos = []
    lista_alunos_do_db = getUsersFromDB()
    for aluno in lista_alunos_do_db:
        aluno_formated = registerData(aluno[0], aluno[1], aluno[2])
        lista_alunos.append(aluno_formated)
    return render_template('list_user.html', faculdade='FECAF', alunos=lista_alunos)


# QUERIES
def sendRegisterDataToDB(data):
    sql = f"INSERT INTO alunoslogin (nome, email, senha) VALUES (%s, %s, %s)"
    val = (data.nome, data.email, data.crypto_password(data.password))
    mycursor.execute(sql, val)
    mydb.commit()

def getUsersFromDB():
    sql = f"SELECT nome, email, senha FROM alunoslogin"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result


# UTILS
def md5_string(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))

    return md5_hash.hexdigest()


# app.run()