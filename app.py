from flask import Flask, render_template, request

# from linear regression model
coefficient = -50.6
y_intercept = 90.2

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/prediction", methods=["GET","POST"])
def prediction():
    q = float(request.form.get("q"))
    return(render_template("prediction.html", r=(q * coefficient) + y_intercept))

if __name__ == "__main__":
    app.run()