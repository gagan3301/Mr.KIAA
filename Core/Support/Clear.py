# ORIGINAL CREATOR: Gagan (KIA)
# AUTHOR: Gagan (KIA)
#  KIA <rtg.gagan@gmail.com>
# 

import os

Windows = "nt"


class Screen:

    def Clear():
        os.system("cls" if os.name == Windows else "clear")
