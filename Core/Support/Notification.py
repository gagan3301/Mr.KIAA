# ORIGINAL CREATOR: Luca Garofalo (KIA)
# AUTHOR: Luca Garofalo (KIA)
# Copyright (C) 2021-2023 KIA <lukege287@gmail.com>
# License: GNU General Public License v3.0

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