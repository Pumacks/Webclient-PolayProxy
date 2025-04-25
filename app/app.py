import subprocess
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def stream_logs():
    process = subprocess.Popen(
        ["docker", "logs", "-f", "polarproxy"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    for line in process.stdout:
        yield f"data: {line}\n\n"

@app.route("/logs/stream")
def log_stream():
    return Response(stream_logs(), mimetype="text/event-stream")

@app.route("/logs")
def logs():
        return render_template("logs.html")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)