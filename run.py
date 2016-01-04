from flask import *
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#Takes 3 variables from forms on index.html and returns them to results function
@app.route('/', methods=['POST'])
def my_form_post():
    txt  = request.form['district']
    txt2 = request.form['rate']
    txt3 = request.form['type']
    return results(txt, txt2, txt3)

#Connects to database and searches it using the variables from my_form_post
#Displays results on results.html
@app.route('/')
def results(area, rating, food):
    conn = sqlite3.connect('SRG.db')
    c = conn.cursor()
    results = c.execute('SELECT * FROM restaurants WHERE address LIKE "%%%s%%" \
		AND rating > %s-1 AND type LIKE "%%%s%%" ORDER BY rating DESC' \
		% (area, rating, food,))
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run()