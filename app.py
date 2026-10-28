
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AI Personal Finance Advisor</h1>
    <p>Welcome to my project!</p>
    <p>My project is deployed successfully.</p>
    """

if __name__ == "__main__":
    app.run()
