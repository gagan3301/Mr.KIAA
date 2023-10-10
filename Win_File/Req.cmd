::ORIGINAL CREATOR: Luca Garofalo (KIA)
::AUTHOR: Luca Garofalo (KIA)
::Copyright (C) 2021-2023 KIA <lukege287@gmail.com>
::License: GNU General Public License v3.0

@ECHO OFF

START /B pip3 install -r requirements.txt  2>NUL >NUL
echo INSTALLING REQUIREMENTS DO NOT CLOSE THIS WINDOW MANUALLY...
cd ../
echo path= %CD% >>Mr.kia/Configuration/Configuration.ini
echo Desktop>Mr.kia/Display/Display.txt