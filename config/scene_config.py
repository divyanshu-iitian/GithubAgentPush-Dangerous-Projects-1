# scene_config.py

class SceneConfig:
    """
    Configuration settings for scenes in SmartHomeHub.

    Attributes:
        SCENES (dict): A dictionary of predefined scenes.
    """

    # Define scene configurations here
    SCENES = {
        "good_night": {
            "description": "Sets the home to a good night routine.",
            "actions": [
                {"device_id": "light_01", "action": "turn_off"},
                {"device_id": "tv_01", "action": "turn_off"},
                {"device_id": "thermostat_01", "action": "set_temperature", "value": 68}
            ]
        },
        "watch_movie": {
            "description": "Sets the home for movie watching.",
            "actions": [
                {"device_id": "light_02", "action": "set_brightness", "value": 30},
                {"device_id": "tv_01", "action": "turn_on"},
                {"device_id": "soundbar_01", "action": "turn_on"}
            ]
        },
        # Add more scenes as needed
    }