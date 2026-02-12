from flask import Flask, jsonify, request
from core.device_manager import DeviceManager

app = Flask(__name__)
device_manager = DeviceManager()

@app.route('/api/devices', methods=['GET'])
def get_devices():
    """Retrieve all devices."""
    try:
        devices = device_manager.get_all_devices()
        return jsonify(devices), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/devices/<int:device_id>', methods=['GET'])
def get_device(device_id):
    """Retrieve a specific device."""
    try:
        device = device_manager.get_device_by_id(device_id)
        if device is None:
            return jsonify({'error': 'Device not found'}), 404
        return jsonify(device), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/devices', methods=['POST'])
def add_device():
    """Add a new device."""
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'type' not in data:
            return jsonify({'error': 'Invalid request'}), 400
        device_manager.add_device(data['name'], data['type'])
        return jsonify({'message': 'Device added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    """Update a specific device."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
        device_manager.update_device(device_id, data)
        return jsonify({'message': 'Device updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    """Delete a specific device."""
    try:
        device_manager.delete_device(device_id)
        return jsonify({'message': 'Device deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500