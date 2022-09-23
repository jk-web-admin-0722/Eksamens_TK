from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sakumlapa')
def sakumlapa():
    return render_template('sakumlapa.html')

@app.route('/pakalpojumi')
def pakalpojumi():
    return render_template('pakalpojumi.html')

@app.route('/specialisti')
def specialisti():
    return render_template('specialisti.html')

@app.route('/galerija')
def galerija():
    return render_template('galerija.html')

@app.route('/kontakti')
def kontakti():
    return render_template('kontakti.html')

if __name__ == '__main__':
    app.run(debug = True)

