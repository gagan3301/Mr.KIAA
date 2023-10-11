# ORIGINAL CREATOR: Gagan (KIA)
# AUTHOR: Gagan (KIA)
#  KIA <rtg.gagan@gmail.com>
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