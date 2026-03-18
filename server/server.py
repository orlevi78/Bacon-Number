from bacon_number import bacon_distance

from flask import Flask
from flask_cors import CORS

app = Flask("BaconNumber")
CORS(app)  # Allows other browser to send requests. Not sure why it's necessary, havn't read much about it.


@app.get("/<name>")
def bacon_number(name: str):
    return str(bacon_distance.find_distance_from_bacon(name))


app.run(host="0.0.0.0", port=5000)
