# ORIGINAL CREATOR: Luca Garofalo (KIA)
# AUTHOR: Luca Garofalo (KIA)
# Copyright (C) 2023 KIA <lukege287@gmail.com>
# License: GNU General Public License v3.0 

import random
from configparser import ConfigParser


class Select:
   
    nomefile = "Configuration/Configuration.ini"
    parser = ConfigParser()
    parser.read(nomefile)
    useragent_file = parser["Settings"]["useragent_List"]
    f = open(useragent_file, "r")
    value = f.readlines()
    f.close()
    agent = random.choice(value).replace("\n","")