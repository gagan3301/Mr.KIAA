# ORIGINAL CREATOR: Gagan (KIA)
# AUTHOR: Gagan (KIA)
# Copyright (C) 2023 KIA <rtg.gagan@gmail.com>
# 

from configparser import ConfigParser

class Check:

    @staticmethod 
    def WhoIs():
        api = "Configuration/Configuration.ini"
        Parser = ConfigParser()
        Parser.read(api)
        Key = Parser["Settings"]["Api_Key"]
        return Key