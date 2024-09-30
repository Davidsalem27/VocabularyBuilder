import SettingsEditor
import WordManager as wm
class SettingsController:
    """
    the controller of the model-view-controller design pattern
    """
    def __init__(self,word_manager : wm.WordManager):
        self._word_manager=word_manager
        self._settings=None

    def load_settings(self):
        loader=SettingsEditor.SettingsEditor()
        self._settings=loader.load_file()
