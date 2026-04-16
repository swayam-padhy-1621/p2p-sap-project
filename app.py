from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def db_connect():
    return sqlite3.connect("database.db")

@app.route('/')
def index():
    conn = db_connect()
    pr_data = conn.execute("SELECT * FROM pr").fetchall()
    po_data = conn.execute("SELECT * FROM po").fetchall()
    conn.close()
    return render_template('index.html', pr=pr_data, po=po_data)


@app.route('/pr', methods=['GET', 'POST'])
def pr():
    if request.method == 'POST':
        item = request.form['item']
        qty = request.form['qty']

        conn = db_connect()
        conn.execute("INSERT INTO pr (item, qty) VALUES (?, ?)", (item, qty))
        conn.commit()
        conn.close()

        return redirect('/')
    
    return render_template('pr.html')


@app.route('/po', methods=['GET', 'POST'])
def po():
    if request.method == 'POST':
        vendor = request.form['vendor']

        conn = db_connect()
        conn.execute("INSERT INTO po (vendor) VALUES (?)", (vendor,))
        conn.commit()
        conn.close()

        return redirect('/')
    
    return render_template('po.html')


@app.route('/gr')
def gr():
    return render_template('gr.html')


@app.route('/invoice')
def invoice():
    return render_template('invoice.html')


if __name__ == '__main__':
    app.run(debug=True)