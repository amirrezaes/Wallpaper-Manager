import platform
import OperationSystems
import api
import random
import json


config = json.load(open("config.json"))
image_map = json.load(open("image_map.json"))

system = None
api_mode = None

if config["image_folder_path"] != "default":
    OperationSystems.path = config["image_folder_path"]

if platform.system() == 'Windows':
    system = OperationSystems.Windows()
elif platform.system() == 'Linux':
    system = OperationSystems.Linux()
elif platform.system() == 'Darwin':
    system = OperationSystems.Mac()
else:
    system = OperationSystems.Operationsystem()

if config["api_mode"] == "weather":
    api_mode = api.Weather

elif config["api_mode"] == "time":
    api_mode = api.Time



#a = random.choice(image_map[config["api_mode"]][api.Time.day_part()])
b = random.choice(image_map[config["api_mode"]][api_mode.get_update()])
system.change_bg(b)
