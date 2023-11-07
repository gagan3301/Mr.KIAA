# ORIGINAL CREATOR: Gagan, Nand and Irtika
# AUTHOR: Gagan, Nand and Irtika
# Copyright (C) 2023 KIA <>
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