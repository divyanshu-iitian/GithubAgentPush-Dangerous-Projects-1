import unittest
from core.scene_automation import SceneAutomation


class TestSceneAutomation(unittest.TestCase):
    def setUp(self):
        self.scene_manager = SceneAutomation()

    def test_create_scene(self):
        scene_id = self.scene_manager.create_scene("Bedtime")
        self.assertIsNotNone(scene_id)
        self.assertIn(scene_id, self.scene_manager.scenes)

    def test_add_device_to_scene(self):
        scene_id = self.scene_manager.create_scene("Bedtime")
        device_id = "device123"
        success = self.scene_manager.add_device_to_scene(scene_id, device_id)
        self.assertTrue(success)
        self.assertIn(device_id, self.scene_manager.scenes[scene_id]["devices"])

    def test_remove_device_from_scene(self):
        scene_id = self.scene_manager.create_scene("Bedtime")
        device_id = "device123"
        self.scene_manager.add_device_to_scene(scene_id, device_id)
        success = self.scene_manager.remove_device_from_scene(scene_id, device_id)
        self.assertTrue(success)
        self.assertNotIn(device_id, self.scene_manager.scenes[scene_id]["devices"])

    def test_execute_scene(self):
        scene_id = self.scene_manager.create_scene("Bedtime")
        self.scene_manager.add_device_to_scene(scene_id, "device123")
        self.scene_manager.add_device_to_scene(scene_id, "device456")
        result = self.scene_manager.execute_scene(scene_id)
        self.assertTrue(result)

    def test_get_scenes(self):
        scenes = self.scene_manager.get_scenes()
        self.assertIsInstance(scenes, list)
        self.assertGreater(len(scenes), 0)


if __name__ == "__main__":
    unittest.main()