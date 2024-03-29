from flask import Flask, jsonify, redirect, render_template
from flask_cors import CORS, cross_origin

app = Flask(
    __name__,
    template_folder="../frontend/build",
    static_folder="../frontend/build",
    static_url_path="/",
)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
@cross_origin()
def root():
    return render_template("index.html")


@app.errorhandler(404)
def not_found(_):
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
