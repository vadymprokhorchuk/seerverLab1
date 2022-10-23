from core import app
from flask import jsonify, request

USERS = [
    {
        "id": 1,
        "name": "John"
    }
]

CATEGORIES = [
    {
        "id": 1,
        "name": "Food"
    }
]

RECORDS = [
    {
        "id": 1,
        "user_id": 1,
        "category_id": 1,
        "created": 1666544270,
        "amount": 280
    }
]


@app.route("/users")
def get_users():
    user_id = request.args.get('id', default=None, type=int)
    if user_id:
        found_user = next((user for user in USERS if user["id"] == user_id), None)
        if found_user:
            return jsonify({"user": found_user})
        else:
            return jsonify({"error": "User not found."})
    else:
        return jsonify({"users": USERS})


@app.route("/categories")
def get_categories():
    category_id = request.args.get('id', default=None, type=int)
    if category_id:
        found_category = next((category for category in CATEGORIES if category["id"] == category_id), None)
        if found_category:
            return jsonify({"category": found_category})
        else:
            return jsonify({"error": "Category not found."})
    else:
        return jsonify({"categories": CATEGORIES})


@app.route("/records")
def get_records():
    record_id = request.args.get('id', default=None, type=int)
    user_id = request.args.get('user_id', default=None, type=int)
    if record_id:
        found_record = next((record for record in RECORDS if record["id"] == record_id), None)
        if found_record:
            return jsonify({"record": found_record})
        else:
            return jsonify({"error": "Record not found."})
    else:
        if user_id:
            records = list(filter(lambda record: record['user_id'] == user_id, RECORDS))
            if len(records) > 0:
                return jsonify({"records": records})
            else:
                return jsonify({"error": "Records from this user not found."})
        else:
            return jsonify({"records": RECORDS})


@app.route("/")
def index():
    return "Flask app"
