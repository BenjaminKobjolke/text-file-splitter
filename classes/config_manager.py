import configparser
import os

class ConfigManager:
    def __init__(self, config_file='settings.ini'):
        self.config = configparser.ConfigParser()
        self.config_file = config_file
        self._load_config()

    def _load_config(self):
        if os.path.exists(self.config_file):
            self.config.read(self.config_file)
        else:
            self._create_default_config()

    def _create_default_config(self):
        self.config['Settings'] = {'separator': '---'}
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def get_separator(self):
        return self.config.get('Settings', 'separator', fallback='---')
