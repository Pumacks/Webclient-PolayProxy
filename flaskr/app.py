import subprocess
import threading
import json
from flask import Flask, render_template, Response, request

app = Flask(__name__)

container_id = ""
docker_mode = ""
pcap_over_ip = "127.0.0.1"

def stream_logs():
	if docker_mode:
		process = subprocess.Popen(
	        ["docker", "logs", "-f", container_id],
	        stdout=subprocess.PIPE,
	        stderr=subprocess.STDOUT,
	        text=True)
		if process.stdout is not None:
			for line in process.stdout:
				yield f"data: {line}\n\n"
	else:
		process = subprocess.Popen(["journalctl", "-t", "PolarProxy"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
		if process.stdout is not None:
			for line in process.stdout:
				yield f"data: {line}\n\n"

def run_polarproxy_with_wireshark():
    cmd = (
        f"wireshark -k -i TCP@{pcap_over_ip}:57012"
    )
    subprocess.run(cmd, shell=True)

def start_polarproxy():
	if docker_mode:
		cmd = (f"docker start {container_id}")
		subprocess.run(cmd, shell=True,capture_output=True,text=True)
	else:
		cmd = ("systemctl start PolarProxy.service")
		subprocess.run(cmd, shell=True,capture_output=True,text=True)

def stop_polarproxy():
	if docker_mode:
		cmd = (f"docker stop {container_id}")
		subprocess.run(cmd, shell=True,capture_output=True,text=True)
	else:
		cmd = ("systemctl stop PolarProxy.service")
		subprocess.run(cmd, shell=True,capture_output=True,text=True)

def load_settings():
	global container_id
	global docker_mode
	global pcap_directory
	try:
		with open('static/settings.json', 'r') as f:
			json_data = json.load(f)
			container_id = json_data.get("container_id", "")
			docker_mode = json_data.get("docker_mode", "")
			pcap_directory = json_data.get("pcap_directory", "")
	except (FileNotFoundError, json.JSONDecodeError):
		container_id = ""
		docker_mode = ""
		pcap_directory = "var/log/PolarProxy"

def write_into_json(name, data):
	try:
		with open('static/settings.json') as f:
			json_data = json.load(f)
	except:
		json_data = {}

	json_data[name] = data

	with open('static/settings.json', 'w') as f:
		json.dump(json_data, f, ensure_ascii=False, indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/logs/stream")
def log_stream():
    return Response(stream_logs(), mimetype="text/event-stream")

@app.route("/options")
def options():
    return render_template("options.html", container_id = container_id, docker_mode = docker_mode, pcap_directory = pcap_directory)

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

@app.route("/setPcapIP", methods=["POST"])
def setup_pcapoverip():
    global pcap_over_ip
    pcap_over_ip = request.data.decode("utf-8")
    write_into_json("pcap_over_ip", pcap_over_ip)
    return "OK"

@app.route("/set_mode", methods=["POST"])
def switch_mode():
	global docker_mode
	mode = request.data.decode("utf-8")
	docker_mode = mode == "docker"
	write_into_json("docker_mode", docker_mode)
	return "Switched Mode"

load_settings()

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
