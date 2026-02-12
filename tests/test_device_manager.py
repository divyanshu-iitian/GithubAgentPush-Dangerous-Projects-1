import unittest
from core.device_manager import DeviceManager

class TestDeviceManager(unittest.TestCase):
    def setUp(self):
        self.device_manager = DeviceManager()

    def test_list_devices(self):
        devices = self.device_manager.list_devices()
        self.assertIsInstance(devices, list)
        self.assertGreater(len(devices), 0)

    def test_add_device(self):
        device_id = "testDevice"
        result = self.device_manager.add_device(device_id, {"type": "light", "state": "off"})
        self.assertTrue(result)
        
    def test_remove_device(self):
        device_id = "testDevice"
        result = self.device_manager.remove_device(device_id)
        self.assertTrue(result)
    
    def test_update_device_state(self):
        device_id = "testDevice"
        state = "on"
        result = self.device_manager.update_device_state(device_id, state)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()