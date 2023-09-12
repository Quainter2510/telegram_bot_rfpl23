import json
from config_data import config

with open("settings.json", "r") as settings:
    config.ALL_FUNCTION_READY = json.load(settings)["all_func_ready"]