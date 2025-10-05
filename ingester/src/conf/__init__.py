import importlib
from typing import Optional
from ingester.src.conf import global_settings

class Settings():
    def __init__(self, settings_module: Optional[str] = None):
        for setting in dir(global_settings):
            if setting.isupper():
                setattr(self, setting, getattr(global_settings, setting))

        self.SETTINGS_MODULE = settings_module

        if settings_module is not None:
            module = importlib.import_module(settings_module)
            
            for setting in dir(module):
                if setting.isupper():
                    setattr(self, setting, getattr(module, setting))


settings = Settings()

if __name__ == "__main__":
    print(settings.ROOT_PATH)