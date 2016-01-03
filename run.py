from flask import *
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():

    txt = request.form['district']
    txt2 = request.form['rate']
    txt3 = request.form['type']
    results(txt,txt2,txt3)
    return results(txt, txt2, txt3)

@app.route('/')
def results(area, rating, food):
    conn = sqlite3.connect('SRG.db')
    c = conn.cursor()
    results = c.execute('SELECT * FROM restaurants WHERE address LIKE "%%%s%%" \
		AND rating > %s-1 AND type LIKE "%%%s%%" ORDER BY rating DESC' \
		% (area, rating, food,))
    return render_template('results.html',
                           results=results)

if __name__ == '__main__':
    app.run(debug=True)