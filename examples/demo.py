from pyupload import Engine
import pyupload.auphonic as auphonic

import vault

engine = Engine()

print("Using PyUpload engine version {}", engine.version)

prod = auphonic.Production(preset = "JfM6rTYKfFoMVzh8bdYrZH", username = vault.username, password = vault.password)
prod.create()

