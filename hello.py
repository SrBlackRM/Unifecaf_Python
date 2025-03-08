from flask import Flask, render_template, request

app = Flask(__name__)

class registerData():
    def __init__(self, nome, email, password):
        self.nome = nome
        self.email = email
        self.password = password


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    print(request.method)
    if request.method == "POST":
        data = request.json
        # sendToDB(data)
        print(f'nome: {data['nome']}\nemail: {data['email']}\npassword: {data['pass']}')
    return render_template('register.html', faculdade='FECAF')

@app.route('/listUser')
def listUser():
    aluno1 = registerData('Michel', 'michelrbm@gmail.com', 'teste')
    aluno2 = registerData('MichaelJack', 'jackfive@gmail.com', 'teste2')

    lista_alunos = [aluno1, aluno2]

    return render_template('list_user.html', faculdade='FECAF', alunos=lista_alunos)

def sendToDB():
    pass

app.run()