from flask import multicloud

app = Flask(__name__)

@app.route("/")
def home():

 return "Hello, class"
 main

if __name__ == "__main__":
    app.run(debug=True)
