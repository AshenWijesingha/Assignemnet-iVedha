import json
import subprocess
import socket
from datetime import datetime

def check_service_status(service_name):
    try:
        subprocess.run(['systemctl', 'is-active', service_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "UP"
    except subprocess.CalledProcessError:
        return "DOWN"

def create_json_object(service_name, service_status, host_name):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    json_data = {
        "service_name": service_name,
        "service_status": service_status,
        "host_name": host_name
    }
    with open(f"{service_name}-status-{timestamp}.json", 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

def main():
    services = ["httpd", "rabbitmq", "postgresql"]
    host_name = socket.gethostname()

    for service in services:
        service_status = check_service_status(service)
        create_json_object(service, service_status, host_name)

if __name__ == "__main__":
    main()
