from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Anuradha Singh, 190!'
if __name__ == '__main__':
    app.run(port=5000)
