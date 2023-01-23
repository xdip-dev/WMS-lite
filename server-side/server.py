from flask import Flask, request, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import interaction as i

app = Flask(__name__)
CORS(app)


@app.route("/linkboxloc",methods=['POST'])
def link_box_loc():
    dataRecieved = request.json 
    return i.linkBoxToLocation(dataRecieved['barCodeBoxe'],dataRecieved['barcodeLocation'])
    

@app.route("/getlocation",methods=['POST','GET'])
def get_location():
    if request.method == 'POST':
        data= i.getLocationArticle(request.json)
    else:
        data=i.getLocationArticle('fake')
    
    return data.to_json(orient='table')

@app.route("/removestock",methods=['POST'])
def remove_stock():
    return i.removeBoxeFromLocation(request.json)

@app.route("/getqty",methods=['POST'])
def get_qty():
    return i.getQuantityStored(request.json)


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
