from flask import Flask, request, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from interaction import Interaction

app = Flask(__name__)
CORS(app)

interaction=Interaction()


@app.route("/linkboxloc",methods=['POST'])
def link_box_loc():
    dataRecieved = request.json 
    return interaction.linkBoxToLocation(dataRecieved['barCodeBoxe'],dataRecieved['barcodeLocation'])


@app.route("/getlocation",methods=['POST','GET'])
def get_location():
    if request.method == 'POST':
        data= interaction.getLocationArticle(request.json)
    else:
        data=interaction.getLocationArticle('fake')
    
    return data.to_json(orient='table')

@app.route("/removestock",methods=['POST'])
def remove_stock():
    return interaction.removeBoxeFromLocation(request.json)

@app.route("/getqty",methods=['POST'])
def get_qty():
    return interaction.getQuantityStored(request.json)


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
