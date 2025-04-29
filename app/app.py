import subprocess
import threading
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def stream_logs():
    process = subprocess.Popen(
        ["docker", "logs", "-f", "polarproxy-pcap"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    if process.stdout is not None:
        for line in process.stdout:
            yield f"data: {line}\n\n"


def run_polarproxy_with_wireshark():
    cmd = (
        "wireshark -k -i TCP@127.0.0.1:57012"
    )
    subprocess.run(cmd, shell=True)


@app.route("/logs/stream")
def log_stream():
    return Response(stream_logs(), mimetype="text/event-stream")

@app.route("/logs")
def logs():
        return render_template("logs.html")

@app.route("/start-proxy")
def start_proxy():
    threading.Thread(target=run_polarproxy_with_wireshark, daemon=True).start()
    return "PolarProxy mit Wireshark gestartet"

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
