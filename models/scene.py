#!/usr/bin/env python3

"""
scene.py - scene model definition for SmartHomeHub
"""

class Scene:
    """
    Representation of a smart home scene.

    Attributes:
        name (str): The name of the scene.
        description (str): A brief description of the scene.
        action_sequence (list): List of actions to perform when this scene is activated.
    """

    def __init__(self, name: str, description: str, action_sequence: list):
        """
        Initialize a new Scene.

        Args:
            name (str): The name of the scene.
            description (str): A brief description of the scene.
            action_sequence (list): List of actions to perform when this scene is activated.

        Raises:
            ValueError: If `action_sequence` is not a list.
        """
        if not isinstance(action_sequence, list):
            raise ValueError("Action sequence must be a list.")

        self.name = name
        self.description = description
        self.action_sequence = action_sequence

    def __str__(self) -> str:
        """Return a string representation of the scene."""
        return f"Scene(name='{self.name}', description='{self.description}')"

    def activate(self):
        """
        Activate the scene by executing the defined action sequence.

        Returns:
            None
        """
        for action in self.action_sequence:
            if callable(action):
                action()
            else:
                print(f"Action {action} is not callable and will be skipped.")