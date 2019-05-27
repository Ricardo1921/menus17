from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/Registo')
def Registo():
    return render_template('Registo.html')


@app.route('/V')
def V():
    return render_template('V.html')

@app.route('/C')
def C():
    return render_template('C.html')

@app.route('/F')
def F():
    return render_template('F.html')

@app.route('/Galo')
def Galo():
    return render_template('Galo.html')


if __name__ == '__main__':
    app.run(debug=True)
