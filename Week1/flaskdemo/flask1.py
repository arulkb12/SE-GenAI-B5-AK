from flask import Flask

app = Flask(__name__)

@app.route('/')

def hellp():
    return("Hello this is my 1st project")

if __name__ == '__main__':
    app.run(debug=True)
