from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    name = "adnan ghadieh"
    yr = datetime.datetime.now().year
    random_number = random.randint(0, 10)
    return render_template("index.html", num=random_number, yr=yr, nm=name.title())


@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]

    return render_template("guess.html", person_name=name, gender_type=gender, years_old=age)


@app.route('/blog')
def block():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response_url = requests.get(blog_url)
    blog_data = response_url.json()
    return render_template("blog.html", posts=blog_data)

if __name__ == "__main__":
    app.run(debug=True)
