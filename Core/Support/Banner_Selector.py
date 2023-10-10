# ORIGINAL CREATOR: Luca Garofalo (KIA)
# AUTHOR: Luca Garofalo (KIA)
# Copyright (C) 2021-2023 KIA <lukege287@gmail.com>
# License: GNU General Public License v3.0

import random
from Core.Support import Font
from Core.Support import Language

filename = Language.Translation.Get_Language()
filename


class Random:

    def Get_Banner(Folder, Mode):
        if Mode == "Desktop":
            List = ["Banner1.txt", "Banner2.txt", "Banner3.txt"]
        elif Mode == "Mobile":
            List = ["Banner4.txt", "Banner5.txt"]
        else:
            print(Font.Color.RED + "[!]" + Font.Color.WHITE + Language.Translation.Translate_Language(
                filename, "Default", "DisplayError", "None"))
            exit()
        choice = random.choice(List)
        f = open(Folder + "/" + choice, "r", newline=None)
        banner = f.read()
        f.close()
        print(Font.Color.GREEN + banner)
