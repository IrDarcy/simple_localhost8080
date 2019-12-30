from flask import Flask
app=Flask(__name__)
@app.route('/')
@app.route('/home')
@app.route('/index')
@app.route('/j')
def home():
  return "<h1>Loves contributing to ScoreLab</h1>"
if __name__ == '__main__':
  app.run(port=8080)

