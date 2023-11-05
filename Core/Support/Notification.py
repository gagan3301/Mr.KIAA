# ORIGINAL CREATOR: Gagan, Nand and Irtika
# AUTHOR: Gagan, Nand and Irtika
#  KIA <>
# 

import os

class Notifier:

    @staticmethod
    def Start(Mode):
        if Mode == "Desktop":
            if os.name == "nt":
                pass
            else:
                os.system("java Core/Support/Notification/Notification.java")
        else:
            pass