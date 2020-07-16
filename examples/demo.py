from pyupload import Engine
import pyupload.auphonic as auphonic

engine = Engine()

print(engine.version)

prod1 = auphonic.Production(multitrack = True)
prod2 = auphonic.Production(id = "qwer-tzui-opas-dfgh-jkly")

