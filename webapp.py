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
            # we need to validate if model is empty or not if empty then we need to set it to base
            model = request.form["model"]
            if model == "":
                model = "base"
        except:
            errors += "<p>{!r} is not a valid link.</p>\n".format(request.form["link"])
        if link is not None:
            result = main(link,model)
            print(result)
            return render_template("result.html", result=result)
    return render_template("home.html", errors=errors)

if __name__ == "__main__":
    # Mmust use port 80 to work with Docker app feature.
    app.run(port=80, host="0.0.0.0")