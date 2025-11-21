# app.py (add or merge into your existing file)
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "devkey"   # needed for flash messages in dev

# For demo: keep user in-memory. Replace with DB logic later.
user = {"name": "Joshith", "balance": 5000, "transactions": ["+1000", "-200", "+500"]}

@app.route("/")
def home():
    return render_template("index.html", user=user)

# Deposit: show form (GET) and process (POST)
@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if request.method == "POST":
        try:
            amount = float(request.form.get("amount", 0))
            if amount <= 0:
                flash("Enter a positive amount", "error")
                return redirect(url_for("deposit"))
            user["balance"] += amount
            user["transactions"].insert(0, f"+{int(amount)}")
            flash(f"Deposited ₹{int(amount)}", "success")
            return redirect(url_for("home"))
        except ValueError:
            flash("Invalid amount", "error")
            return redirect(url_for("deposit"))
    # GET: show deposit form
    return render_template("deposit.html", user=user)

# Withdraw: similar flow
@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if request.method == "POST":
        try:
            amount = float(request.form.get("amount", 0))
            if amount <= 0:
                flash("Enter a positive amount", "error")
                return redirect(url_for("withdraw"))
            if amount > user["balance"]:
                flash("Insufficient balance", "error")
                return redirect(url_for("withdraw"))
            user["balance"] -= amount
            user["transactions"].insert(0, f"-{int(amount)}")
            flash(f"Withdrew ₹{int(amount)}", "success")
            return redirect(url_for("home"))
        except ValueError:
            flash("Invalid amount", "error")
            return redirect(url_for("withdraw"))
    return render_template("withdraw.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)
