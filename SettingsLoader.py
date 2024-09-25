import json
FILE_NAME='Setting.json'

class SettingsEditor:
    """
    class for editing the settings of the program
    """
    def __init__(self):
        self.data=None

    def load_file(self):
        with open(FILE_NAME, 'r') as json_file:
            self.data = json.load(json_file)
    def save_file(self):
        with open(FILE_NAME, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)

    def init_file(self):
        self.data={"quiz Timer": 0,"quiz time interval":30, "Number words basic quiz":5,
                   "dark mode":0}
