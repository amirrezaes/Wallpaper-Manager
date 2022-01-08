import platform
import OperationSystems
import api
import random
import json
import time
import logging

logging.basicConfig(filename='event.log', level=logging.DEBUG)

config = json.load(open("config.json"))
image_map = json.load(open("image_map.json"))

system = None
api_mode = None

if config["image_folder_path"] != "default":
    OperationSystems.path = config["image_folder_path"]
    logging.info(f"default path to images changed to: {OperationSystems.path}")

if platform.system() == 'Windows':
    system = OperationSystems.Windows()
elif platform.system() == 'Linux':
    system = OperationSystems.Linux()
elif platform.system() == 'Darwin':
    system = OperationSystems.Mac()
else:
    system = OperationSystems.Operationsystem()

logging.info(f"operation system is: {type(system).__name__}")

if config["api_mode"] == "weather":
    api_mode = api.Weather

elif config["api_mode"] == "time":
    api_mode = api.Time

logging.info(f"api mode set to: {api_mode.__name__}")

while True:
    try:
        api_resp = api_mode.get_update()
        background = random.choice(image_map[config["api_mode"]][api_resp])
        system.change_bg(background)
        logging.info(f"api response: {api_resp}, background changed to {background}")
        time.sleep(60*30) # half an hour
    except KeyboardInterrupt:
        logging.info("process interrupted")
        exit()
    except Exception as e:
        logging.error(f"Error {e} occured while changing background")
        exit()
