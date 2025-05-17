import subprocess
import threading
import json
from flask import Flask, render_template, Response, request

app = Flask(__name__)

container_id = ""
docker_mode = "failed to load settings"

def stream_logs():
    process = subprocess.Popen(
        ["docker", "logs", "-f", container_id],
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

def start_polarproxy():
    cmd = (
        f"docker start {container_id}"
    )
    subprocess.run(cmd, shell=True,capture_output=True,
            text=True)

def stop_polarproxy():
    cmd = (
        f"docker stop {container_id}"
    )
    subprocess.run(cmd, shell=True,capture_output=True,
            text=True)

def load_settings():
	global container_id
	global docker_mode
	try:
		with open('app/static/settings.json', 'r') as f:
			json_data = json.load(f)
			container_id = json_data.get("container_id", "")
			docker_mode = json_data.get("docker_mode", "")
	except (FileNotFoundError, json.JSONDecodeError):
		container_id = ""
		docker_mode = ""

def write_into_json(name, data):
	try:
		with open('app/static/settings.json') as f:
			json_data = json.load(f)
	except:
		json_data = {}

	json_data[name] = data

	with open('app/static/settings.json', 'w') as f:
		json.dump(json_data, f, ensure_ascii=False, indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/logs/stream")
def log_stream():
    return Response(stream_logs(), mimetype="text/event-stream")

@app.route("/logs")
def logs():
        return render_template("logs.html")

@app.route("/options")
def options():
        return render_template("options.html", container_id = container_id, docker_mode = docker_mode)

@app.route("/wireshark")
def start_wireshark():
    threading.Thread(target=run_polarproxy_with_wireshark, daemon=True).start()
    return "PolarProxy mit Wireshark gestartet"

@app.route("/start-proxy")
def start_proxy():
    threading.Thread(target=start_polarproxy, daemon=True).start()
    return "PolarProxy gestartet"

@app.route("/stop-proxy")
def stop_proxy():
    threading.Thread(target=stop_polarproxy, daemon=True).start()
    return "PolarProxy gestoppt"

@app.route("/dockerCredentials", methods=["POST"])
def setup_docker():
    global container_id
    container_id = request.data.decode("utf-8")
    write_into_json("container_id", container_id)
    return "OK"


@app.route("/set_mode", methods=["POST"])
def switch_mode():
    mode = request.data.decode("utf-8")
    is_docker = mode == "docker"
    write_into_json("docker_mode", is_docker)
    threading.Thread(target=stop_polarproxy, daemon=True).start()
    return "Switched Mode"

load_settings()

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
