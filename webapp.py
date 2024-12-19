from flask import Flask, request, render_template

from main import main

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def home():
    errors = ""
    if request.method == "POST":
        link = None
        try:
            link = request.form["link"]
            # Validate if model is empty or not; if empty, set it to "base"
            model = request.form.get("model", "base")
            if not model:
                model = "base"
        except KeyError:
            errors += "<p>{!r} is not a valid link.</p>\n".format(request.form.get("link", ""))
        if link is not None:
            result = main(link, model)
            print(result)
            return render_template("result.html", result=result)
    return render_template("home.html", errors=errors)

if __name__ == "__main__":
    # Must use port 3000 to work with Docker app feature.
    app.run(port=3000, host="0.0.0.0")
