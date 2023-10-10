# ORIGINAL CREATOR: Luca Garofalo (KIA)
# AUTHOR: Luca Garofalo (KIA)
# Copyright (C) 2023 KIA <lukege287@gmail.com>
# License: GNU General Public License v3.0

from configparser import ConfigParser

class Check:

    @staticmethod 
    def WhoIs():
        api = "Configuration/Configuration.ini"
        Parser = ConfigParser()
        Parser.read(api)
        Key = Parser["Settings"]["Api_Key"]
        return Key