import SettingsLoader
import WordManager as wm
class SettingsController:
    """
    the controller of the model-view-controller design pattern
    """
    def __init__(self,word_manager : wm.WordManager):
        self.word_manager=word_manager
        self.settings=None

    def load_settings(self):
        loader=SettingsLoader.SettingsEditor()
        self.settings=loader.load_file()