from flask import Flask 
#kolejnosć instrukcji ma znaczenie

app = Flask(__name__)

from app import views


if __name__ == "__main__":
    app.run(debug=True)