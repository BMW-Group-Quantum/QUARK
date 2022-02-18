#  Copyright 2021 The QUARK Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import configparser
from pathlib import Path
import os
import logging

"""
TODO check if this file is needed in this form!
"""
# load config if available
config = configparser.ConfigParser()

# check for file
if Path('local_config.ini').is_file():
    #print("Load local")
    config.read('local_config.ini')
elif Path(os.path.expanduser('~/local_config.ini')).is_file():
    #print("Load from ~")
    config.read(os.path.expanduser('~/local_config.ini'))
else:
    # we cant use logging because its not init yet
     logging.info("No local_config file found!")

if "BRAKET" not in config:
    config["BRAKET"] = {}
    #defaults
    config["BRAKET"]["BUCKET"] = 'amazon-braket-benchmark-framework'