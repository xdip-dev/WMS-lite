from flask import Flask, request, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import interaction as i

app = Flask(__name__)
CORS(app)


@app.route("/linkboxloc",methods=['POST'])
def linkboxloc():
    dataRecieved = request.json 
    return i.linkBoxToLocation(dataRecieved['barCodeBoxe'],dataRecieved['barcodeLocation'])
    

@app.route("/getlocation",methods=['POST'])
def getlocation(): 
    data= i.getLocationArticle(request.json)
    return data.to_json(orient='table')

@app.route("/getqty",methods=['GET'])
def getqty():
    pass


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
