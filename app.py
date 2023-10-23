from flask import Flask, jsonify, request
import json
from function import all_products, stop_product

app=Flask(__name__)
@app.route("/mercadoLibre",methods=["GET"])
def mercadoLibre():
    data=json.loads(request.data)
    if "limite" not in data:
        titulos,precios,url=all_products(data["Producto"])
    else:
        titulos,precios,url=stop_product(data["Producto"],data["limite"])    
    return jsonify({"datos":{"Titulos":titulos,"Precios":precios,"Urls":url}})
if __name__=="__main__":
   app.run(host="0.0.0.0",debug=True)   
