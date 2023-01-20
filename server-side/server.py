from flask import Flask
import interaction as i

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/linkboxloc",methods=['POST'])
def linkboxloc():
    
    pass

@app.route("/getlocation",methods=['POST'])
def getlocation():
    pass

@app.route("/getqty",methods=['POST'])
def getqty():
    pass


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")
