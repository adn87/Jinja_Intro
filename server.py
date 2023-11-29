from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    name = "Adnan Ghadieh"
    yr = datetime.datetime.now().year
    random_number = random.randint(0,10)
    return render_template("index.html", num=random_number, yr=yr, nm=name)


if __name__ == "__main__":
    app.run(debug=True)
