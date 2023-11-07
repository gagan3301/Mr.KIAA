::ORIGINAL CREATOR: Gagan, Nand and Irtika
::AUTHOR: Gagan, Nand and Irtika
:: KIA <>
::

@ECHO OFF

START /B pip3 install -r requirements.txt  2>NUL >NUL
echo INSTALLING REQUIREMENTS DO NOT CLOSE THIS WINDOW MANUALLY...
cd ../
echo path= %CD% >>Mr.kia/Configuration/Configuration.ini
echo Desktop>Mr.kia/Display/Display.txt