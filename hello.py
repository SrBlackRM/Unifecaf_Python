from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == "POST":
        print(str(request.data))
    return render_template('register.html')

@app.route('/listUser')
def listUser():
    return render_template('list_user.html')

app.run()