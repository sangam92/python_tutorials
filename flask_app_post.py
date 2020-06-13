from flask import Flask,jsonify,request

app=Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/add_two_num',methods=["POST","GET"])
def add_two_num():
    datadict=request.get_json()
    x=datadict["x"]
    y=datadict["y"]
    z= x+y

    retjson={
    "z":z
    }
    return jsonify(retjson)

@app.route('/bye')
def bye():
    age=10*3
    retjson = {
    'Name':'Sangam',
    'Age':age,
    'phones': [
    {
        "phonename":"Moto",
        "phonenumber":111111
    },
    {
    "phonename":"Xiomi",
    "phonenumber":22222
    }
    ]
    }
    return jsonify(retjson)

if __name__=="__main__":
    app.run()
