from flask import Flask, render_template

app = Flask(__name__, static_folder='templates')

@app.route("/")
def hello_world():
  return render_template('login.html')

@app.route("/home")
def home():
  return render_template('home.html')

if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)