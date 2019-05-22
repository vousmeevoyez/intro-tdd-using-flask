from flask import Flask
from flask import request, jsonify

from app.modules.converter import Converter

app = Flask(__name__)

@app.route("/convert/<string:types>", methods=["POST"])
def convert_gold_api(types):
    response = {
        "amount" : 0,
        "price"  : 0
    }

    # extract request payload
    payload = request.get_json()
    amount = payload["amount"]

    try:
        result = Converter(types).gram_to_idr(amount)
    except ValueError:
        return jsonify("amount cant be zero"), 400
    # set response
    response["amount"] = amount
    response["price"] = result

    return jsonify(response)


if __name__ == "__main__":
    app.run()
