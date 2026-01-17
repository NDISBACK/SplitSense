from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# -----------------------------
# In-memory storage
# -----------------------------
groups = {}
group_counter = 1


# -----------------------------
# Home
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")


# -----------------------------
# Create group
# -----------------------------
@app.route("/group", methods=["POST"])
def create_group():
    global group_counter

    group_name = request.form.get("group_name")
    members_json = request.form.get("members")

    members = json.loads(members_json) if members_json else []

    group_id = group_counter
    group_counter += 1

    groups[group_id] = {
        "id": group_id,
        "name": group_name,
        "members": members,
        "expenses": []
    }

    return redirect(url_for("group_page", group_id=group_id))


# -----------------------------
# Group dashboard
# -----------------------------
@app.route("/group/<int:group_id>")
def group_page(group_id):
    group = groups.get(group_id)

    balances = calculate_balances(group)
    settlements = simplify_balances(balances)

    return render_template(
        "group.html",
        group=group,
        balances=balances,
        settlements=settlements
    )


# -----------------------------
# Add expense
# -----------------------------
@app.route("/add-expense/<int:group_id>", methods=["POST"])
def add_expense(group_id):
    group = groups.get(group_id)

    title = request.form.get("title")
    amount = float(request.form.get("amount"))
    paid_by = request.form.get("paid_by")
    split_between = request.form.getlist("split_between")

    group["expenses"].append({
        "title": title,
        "amount": amount,
        "paid_by": paid_by,
        "split_between": split_between
    })

    return redirect(url_for("group_page", group_id=group_id))


# -----------------------------
# Logic
# -----------------------------
def calculate_balances(group):
    balances = {m: 0 for m in group["members"]}

    for expense in group["expenses"]:
        amount = expense["amount"]
        paid_by = expense["paid_by"]
        people = expense["split_between"]

        share = amount / len(people)

        for person in people:
            if person == paid_by:
                balances[person] += amount - share
            else:
                balances[person] -= share

    return balances


def simplify_balances(balances):
    debtors, creditors = [], []

    for person, amount in balances.items():
        if amount < 0:
            debtors.append([person, -amount])
        elif amount > 0:
            creditors.append([person, amount])

    settlements = []
    i = j = 0

    while i < len(debtors) and j < len(creditors):
        debtor, debt = debtors[i]
        creditor, credit = creditors[j]

        pay = min(debt, credit)
        settlements.append(f"{debtor} pays {creditor} ₹{pay:.2f}")

        debtors[i][1] -= pay
        creditors[j][1] -= pay

        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1

    return settlements


# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    app.run()
