# device_config.py

"""Configuration settings for devices."""

from typing import Dict, Any

class DeviceConfig:
    """Class to hold configuration settings for devices."""
    
    def __init__(self):
        self.settings = {
            "Philips Hue": {
                "host": "philips_hue_bridge.local",
                "port": 80,
                "username": "abc123",
                "timeout": 5
            },
            "Nest": {
                "api_key": "xyz987",
                "client_id": "client_id_123",  # Fixed the missing comma here
                "client_secret": "client_secret_456"
            }
        }
    
    def get_device_settings(self, device_type: str) -> Dict[str, Any]:
        """Get configuration settings for a specific device type."""
        return self.settings.get(device_type, {})