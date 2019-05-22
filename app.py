from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registo')
def registo():
    return render_template('registo.html')

@app.route('/V')
def V():
    return render_template('V.html')

@app.route('/C')
def C():
    return render_template('C.html')

@app.route('/F')
def F():
    return render_template('F.html')




if __name__ == '__main__':
    app.run(debug=True)
