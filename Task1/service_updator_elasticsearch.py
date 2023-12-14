from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from datetime import datetime
import json

app = Flask(__name__)
es = Elasticsearch([{'host': '127.0.0.1', 'port': 9200, 'scheme': 'http'}])  # Update with your Elasticsearch host and port

@app.route('/add', methods=['POST'])
def add_to_elasticsearch():
    try:
        data = request.get_json()
        es.index(index='application_status', body=data)
        return jsonify({'message': 'Data added to Elasticsearch successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/healthcheck', methods=['GET'])
def get_application_status():
    try:
        res = es.search(index='application_status', size=1, sort='@timestamp:desc', _source=['service_name', 'service_status', 'host_name'])
        if res['hits']['total']['value'] > 0:
            return jsonify(res['hits']['hits'][0]['_source'])
        else:
            return jsonify({'message': 'No application status found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/healthcheck/<service_name>', methods=['GET'])
def get_service_status(service_name):
    try:
        res = es.search(index='application_status', body={'query': {'match': {'service_name': service_name}}}, size=1, sort='@timestamp:desc', _source=['service_name', 'service_status', 'host_name'])
        if res['hits']['total']['value'] > 0:
            return jsonify(res['hits']['hits'][0]['_source'])
        else:
            return jsonify({'message': f'No status found for {service_name}'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
