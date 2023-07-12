from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<name>")
def get_name(name):
    agify_url = f"https://api.agify.io?name={name}&country_id=US"
    agify_response = requests.get(agify_url)
    agify_data = agify_response.json()
    years_ago = agify_data["age"]

    genderize_url = f"https://api.genderize.io?name={name}"
    genderize_response = requests.get(genderize_url)
    genderize_data = genderize_response.json()
    gender = genderize_data["gender"]

    return render_template('name.html', name=name, years_ago=years_ago, gender=gender)

if __name__ == "__main__":
    app.run()