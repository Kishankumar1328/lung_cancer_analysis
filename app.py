from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        age = int(request.form["age"])
        smokes = int(request.form["smokes"])
        areaq = int(request.form["areaq"])
        alkhol = int(request.form["alkhol"])

        features = np.array([[age, smokes, areaq, alkhol]])
        prediction = model.predict(features)[0]
        result = "Positive for Lung Cancer" if prediction == 1 else "Negative for Lung Cancer"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
