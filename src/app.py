from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Path to JSON file for storing data
DATA_FILE = "expenses.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

@app.route("/")
def index():
    expenses = load_data()
    # Calculate summary
    total_expenses = len(expenses)
    total_amount = sum(expense["amount"] for expense in expenses)
    category_summary = {}
    for expense in expenses:
        category = expense["category"]
        category_summary[category] = category_summary.get(category, 0) + expense["amount"]

    return render_template("index.html", expenses=expenses, total_expenses=total_expenses,
                           total_amount=total_amount, category_summary=category_summary)

@app.route("/add", methods=["POST"])
def add_expense():
    expenses = load_data()
    new_expense = {
        "date": request.form.get("date", datetime.now().strftime("%Y-%m-%d")),
        "title": request.form["title"],
        "category": request.form["category"],
        "amount": float(request.form["amount"])
    }
    expenses.append(new_expense)
    save_data(expenses)
    return redirect(url_for("index"))

@app.route("/edit/<int:expense_id>", methods=["POST"])
def edit_expense(expense_id):
    expenses = load_data()
    if 0 <= expense_id < len(expenses):
        expenses[expense_id].update({
            "date": request.form.get("date", expenses[expense_id]["date"]),
            "title": request.form["title"],
            "category": request.form["category"],
            "amount": float(request.form["amount"])
        })
        save_data(expenses)
    return redirect(url_for("index"))

@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    expenses = load_data()
    if 0 <= expense_id < len(expenses):
        expenses.pop(expense_id)
        save_data(expenses)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5060,debug=True)
