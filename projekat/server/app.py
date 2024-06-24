from flask import Flask, request, jsonify
import consul
import json
import redis

app = Flask(__name__)

# Initialize Consul client
consul_client = consul.Consul(host='localhost', port=8500)
redis_client = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/namespace/<key>', methods=['POST'])
def write_to_consul(key):
    try:
        # Extract JSON data from the request
        data = request.get_json()
        # key = data.get('key')
        # value = data.get('value')

        if not key or data is None:
            return jsonify({'error': 'Key and value are required'}), 400

        # Convert value to JSON string and write to Consul
        value_str = json.dumps(data)
        consul_client.kv.put(key, value_str)

        return jsonify({'message': 'Data written to Consul successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/consul/read/<key>', methods=['GET'])
def read_from_consul(key):
    try:
        # Read data from Consul
        index, data = consul_client.kv.get(key)

        if data is None:
            return jsonify({'error': 'Key not found'}), 404

        # Convert data from JSON string
        value = json.loads(data['Value'].decode('utf-8'))

        return jsonify({'key': key, 'value': value}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/acl', methods=['POST'])
def write_to_redis():
    try:
        # Extract JSON data from the request
        data = request.get_json()
        doc = data.get('object')
        relation = data.get('relation')
        user = data.get('user')
        key = doc + '#' + relation + '@' + user
        value = 9

        if not key or value is None:
            return jsonify({'error': 'Key and value are required'}), 400

        # Write to Redis
        redis_client.set(key, json.dumps(value))

        return jsonify({'message': 'Data written to Redis successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
