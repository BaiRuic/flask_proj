from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route("/")
def hello(name):
    return f"hell0"

@app.route("/user/<name>")
def user_page(name):
    return f"User:{name}"

@app.route("/test")
def test_url_for():
    print(url_for("hello"))

    print(url_for("user_page", name="Bairuic"))
    print(url_for("user_page", name="YangNa"))

    print(url_for("test_url_for", num=2))

    return "Test Page"