from flask import Flask, render_template, request
import requests

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

    if type(years_ago) == int:
        return render_template('name.html', name=name, years_ago=years_ago, gender=gender)
    else:
        return render_template('404.html')

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["feedback"])
        return render_template('feedback.html', msg_sent=True)
    return render_template('feedback.html', msg_sent=False)

if __name__ == "__main__":
    app.run()