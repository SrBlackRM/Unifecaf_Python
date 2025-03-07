from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == "POST":
        if valid_register(request.json['nome'],
                          request.json['email'],
                          request.json['pass']):
            return None;
    return render_template('register.html')

app.run()