from flask import Flask, render_template_string, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import matplotlib.pyplot as plt

from io import BytesIO
import base64
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

index_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Personal Finance Tracker</title>
</head>
<body>
    <h1>Welcome to Personal Finance Tracker</h1>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('add_transaction') }}">Add Transaction</a></li>
            <li><a href="{{ url_for('view_transactions') }}">View Transactions</a></li>
            <li><a href="{{ url_for('visualize') }}">Visualize Spending</a></li>
        </ul>
    </nav>
</body>
</html>
"""

add_transaction_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Add Transaction</title>
</head>
<body>
    <h1>Add Transaction</h1>
    <form method="POST" action="{{ url_for('add_transaction') }}">
        <label for="date">Date:</label>
        <input type="date" id="date" name="date" required><br>
        <label for="description">Description:</label>
        <input type="text" id="description" name="description" required><br>
        <label for="category">Category:</label>
        <input type="text" id="category" name="category" required><br>
        <label for="amount">Amount:</label>
        <input type="number" id="amount" name="amount" step="0.01" required><br>
        <button type="submit">Add</button>
    </form>
</body>
</html>
"""

view_transactions_html = """
<!DOCTYPE html>
<html>
<head>
    <title>View Transactions</title>
</head>
<body>
    <h1>Transactions</h1>
    <table>
        <tr>
            <th>Date</th>
            <th>Description</th>
            <th>Category</th>
            <th>Amount</th>
        </tr>
        {% for transaction in transactions %}
        <tr>
            <td>{{ transaction.date }}</td>
            <td>{{ transaction.description }}</td>
            <td>{{ transaction.category }}</td>
            <td>{{ transaction.amount }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

visualize_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Visualize Spending</title>
</head>
<body>
    <h1>Spending by Category</h1>
    <img src="data:image/png;base64,{{ plot_url }}" />
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(index_html)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        date = request.form['date']
        description = request.form['description']
        category = request.form['category']
        amount = request.form['amount']
        transaction = Transaction(date=datetime.datetime.strptime(date, '%Y-%m-%d'), 
                                  description=description, category=category, amount=amount)
        db.session.add(transaction)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template_string(add_transaction_html)

@app.route('/view')
def view_transactions():
    transactions = Transaction.query.all()
    return render_template_string(view_transactions_html, transactions=transactions)

@app.route('/visualize')
def visualize():
    transactions = Transaction.query.all()
    df = pd.DataFrame([(t.date, t.amount, t.category) for t in transactions], columns=['Date', 'Amount', 'Category'])
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    plot = df.groupby('Category').sum().plot(kind='pie', y='Amount', autopct='%1.1f%%', legend=False)
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return render_template_string(visualize_html, plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
##http://127.0.0.1:5000
