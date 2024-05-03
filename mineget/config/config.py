import toml
import platform
import pathlib
import typing
import os

class Config:
    def __init__(self):
        self._config_path = self._get_config_path()
        self._config = self.reload_config(self._config_path)
        # TODO: create config file if it doesn't exist
        
    def __del__(self):
        with open(self._config_path, 'r+') as file:
            toml.dump(self._config, file)
        
    def _get_config_path(self) -> str:
        if platform.system() == 'Windows':
            return pathlib.WindowsPath('~\\.mineget.toml').expanduser()
        elif platform.system() == 'Linux': 
            return pathlib.Path('~/.config/mineget/mineget.toml').expanduser()
        elif platform.system() == 'Darwin':
            return pathlib.Path('~/.mineget.toml').expanduser()
        
    def reload_config(self, 
            path: pathlib.Path|pathlib.WindowsPath
        ) -> dict[str, typing.Any]:
        with open(path, 'r+') as file:
            return toml.load(file)
        
    def set_minecraft_home(self, path: pathlib.Path|pathlib.WindowsPath):
        self._config['minecraft_home'] = path.absolute()
 
    def get_minecraft_home(self) -> pathlib.Path|pathlib.WindowsPath:
        return self._config.get('minecraft_home')
    