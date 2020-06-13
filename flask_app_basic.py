from flask import Flask,jsonify

app=Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"
@app.route('/bye')
def bye():
    retjson = {
    'field1':'abc',
    'field2':'def'
    }
    return jsonify(retjson)

if __name__=="__main__":
    app.run(debug=True)
