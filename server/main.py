from bacon_number import bacon_distance

from flask import Flask

app = Flask("BaconNumber")


@app.get("/<name>")
def bacon_number(name: str):
    print(name.upper())
    return str(bacon_distance.find_distance_from_bacon("Gal Gadot"))


app.run(debug=True)
