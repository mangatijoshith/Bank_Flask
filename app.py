from flask import Flask

app = Flask(__name__)

# simple in-memory account store for demo only
accounts = {
    1: {"name": "Ram", "balance": 1000},
    2: {"name": "Sita", "balance": 2500},
}

@app.route("/")
def home():
    return "🏦 Bank Home"

@app.route("/balance/<int:account_id>")
def get_balance(account_id):
    acc = accounts.get(account_id)
    if not acc:
        return f"Account {account_id} not found", 404
    return f"{acc['name']} balance: ₹{acc['balance']}"

@app.route("/deposit/<int:account_id>/<int:amount>")
def deposit(account_id, amount):
    acc = accounts.get(account_id)
    if not acc:
        return f"Account {account_id} not found", 404
    acc['balance'] += amount
    return f"Deposited ₹{amount}. New balance: ₹{acc['balance']}"

@app.route("/withdraw/<int:account_id>/<int:amount>")
def withdraw(account_id, amount):
    acc = accounts.get(account_id)
    if not acc:
        return f"Account {account_id} not found", 404
    if amount > acc['balance']:
        return f"Insufficient funds. Balance: ₹{acc['balance']}", 400
    acc['balance'] -= amount
    return f"Withdrew ₹{amount}. New balance: ₹{acc['balance']}"

if __name__ == "__main__":
    app.run(debug=True)
