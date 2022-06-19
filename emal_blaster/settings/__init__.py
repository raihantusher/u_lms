import os
import json

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_FILE =  BASE_DIR / 'config.json'

try:
    with open(CONFIG_FILE) as config_file:
        config = json.load(config_file)
        config['PROD']
    from .prod import *


except KeyError:
    from .dev import *

SECRET_KEY = config['SECRET_KEY']