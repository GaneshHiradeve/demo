from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my simple Flask app!"

if __name__ == "__main__":
    app.run(debug=True)
