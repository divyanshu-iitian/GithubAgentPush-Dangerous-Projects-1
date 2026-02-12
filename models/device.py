# device.py

class Device:
    """Class to represent a smart device."""

    def __init__(self, device_id, name, device_type):
        """
        Initialize a new device.

        Args:
            device_id (str): Unique identifier for the device.
            name (str): Human-readable name of the device.
            device_type (str): Type of the device (e.g., "light", "thermostat").
        """
        self.device_id = device_id
        self.name = name
        self.device_type = device_type
        self.status = "off"
        self.settings = {}

    def turn_on(self):
        """Turn on the device."""
        if self.status != "on":
            self.status = "on"
            print(f"{self.name} is now on.")
        else:
            print(f"{self.name} is already on.")

    def turn_off(self):
        """Turn off the device."""
        if self.status == "on":
            self.status = "off"
            print(f"{self.name} is now off.")
        else:
            print(f"{self.name} is already off.")

    def set_setting(self, setting_name, value):
        """Set a specific setting for the device."""
        if setting_name in self.settings:
            self.settings[setting_name] = value
            print(f"Setting {setting_name} to {value}.")
        else:
            print(f"Invalid setting: {setting_name}")

    def get_setting(self, setting_name):
        """Get a specific setting for the device."""
        return self.settings.get(setting_name, None)