from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment_result = None
    if request.method == "POST":
        user_text = request.form["user_text"]
        blob = TextBlob(user_text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        sentiment_result = {
            "text": user_text,
            "sentiment": sentiment,
            "polarity": polarity,
            "subjectivity": subjectivity
        }

    return render_template("index.html", result=sentiment_result)

if __name__ == "__main__":
    app.run(debug=True)
