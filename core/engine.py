from flask import Flask, request, jsonify
from utils.helpers import integrate_alexa, integrate_google_assistant
from core.device_manager import DeviceManager

app = Flask(__name__)

device_manager = DeviceManager()

@app.route('/devices', methods=['GET'])
def get_devices():
    try:
        devices = device_manager.get_all_devices()
        return jsonify(devices), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/devices/<device_id>', methods=['GET'])
def get_device(device_id):
    try:
        device = device_manager.get_device(device_id)
        return jsonify(device), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/devices', methods=['POST'])
def add_device():
    data = request.json
    try:
        new_device = device_manager.add_device(data)
        integrate_alexa(new_device.device_id)
        integrate_google_assistant(new_device.device_id)
        return jsonify(new_device), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/devices/<device_id>', methods=['PUT'])
def update_device(device_id):
    data = request.json
    try:
        updated_device = device_manager.update_device(device_id, data)
        return jsonify(updated_device), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/devices/<device_id>', methods=['DELETE'])
def delete_device(device_id):
    try:
        device_manager.delete_device(device_id)
        return jsonify({'message': 'Device deleted'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)