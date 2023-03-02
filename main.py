from flask import Flask, redirect, render_template, session, url_for
app = Flask(__name__)

@app.route("/")
def home():

    return render_template(
        "index.html"
    )




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)