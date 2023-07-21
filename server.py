import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/translate", methods=["POST"])
def translate():
    text = flask.request.json["text"]
    source_language = flask.request.json["source_language"]
    target_language = flask.request.json["target_language"]

    translated_text = translate(text, source_language, target_language)

    return {"translated_text": translated_text}

if __name__ == "__main__":
    app.run(debug=True)
