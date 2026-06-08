from flask import Flask, request
from analyzer import analyze_log

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":
        logs = request.form["logs"]
        result = analyze_log(logs)

    return f"""
    <h2>DevOps AI Log Analyzer</h2>

    <form method="POST">
        <textarea name="logs" rows="10" cols="80"></textarea>
        <br><br>
        <button type="submit">Analyze</button>
    </form>

    <pre>{result}</pre>
    """

if __name__ == "__main__":
    app.run(debug=True)
