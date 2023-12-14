## Service Monitoring Script README
-developed by Ashen Wijesingha

### Overview

This Python script monitors the status of specified services (httpd, rabbitMQ, and PostgreSQL) on a Linux machine. It creates a JSON object containing information about the service status and host name, and writes this object to a file with a timestamp in the filename.

### Instructions

1. **Clone the Repository:**
   ```bash 
    git clone https://github.com/yourusername/servicemonitor.git
    cd servicemonitor
    ```

2. **Install Dependencies:**
    - The script relies on Python 3. Ensure you have Python 3 installed on your system.
    - No additional Python packages are required.

3. **Run the Script:**
    - Execute the script using the following command:
      ```bash 
        python service_monitor.py
        ```
    - The script will check the status of each service and create a JSON file for each service with the format `{serviceName}-status-{timestamp}.json`.

4. **View Output Files:**
    - The generated JSON files will be located in the same directory as the script.

### Notes

- Ensure that you have the necessary permissions to run the `systemctl` command to check the service status. You may need to run the script with elevated privileges (e.g., using `sudo`).

- Modify the `services` list in the script if your environment uses different service names.

- This script assumes that all services are running on the same server. If services are distributed across multiple servers, additional modifications may be needed.

- For any issues or special configurations, refer to the script and modify accordingly.

- For more information on the script and its usage, contact [mailto:inbox.ashen@gmail.com].
