"""flask api module to handle requests from frontend"""
import user_handle as uh

from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route("/api/login", methods=["POST"])
def login():
    """login a user"""
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    user = uh.get_user(username)
    if user is None:
        return make_response("User not found", 404)
    if not user.check_password(password):
        return make_response("Wrong password", 403)
    return make_response("Login successful", 200)