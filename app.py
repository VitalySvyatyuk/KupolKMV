from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def services():
    return render_template('services.html')


@app.route('/materials')
def materials():
    return render_template('materials.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/reviews')
def reviews():
    return render_template('reviews.html')


@app.route('/calc')
def calc():
    return render_template('calc.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
