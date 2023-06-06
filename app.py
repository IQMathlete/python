from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    apikey = ""
    response = requests.get("https://pokeapi.co/api/v2/pokemon/celebi")
    response = requests.get("https://pokeapi.co/api/v2/pokemon/celebi" + "?apikey="+apikey)
    data = response.json()
    img = data["sprites"]["front_shiny"]
    return render_template("index.html", props = {"poke_src": img, "name": data["forms"][0]["name"][1:-1]})

if __name__ == "__main__":
    app.run()