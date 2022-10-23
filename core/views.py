from core import app


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


@app.route("/")
def index():
    return "Flask app"