# ORIGINAL CREATOR: Gagan, Nand and Irtika
# AUTHOR: Gagan, Nand and Irtika
#  KIA <>
# 

import os

Windows = "nt"


class Screen:

    def Clear():
        os.system("cls" if os.name == Windows else "clear")
