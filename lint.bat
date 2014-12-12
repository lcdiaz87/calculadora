@echo off
rem Use pylint on the file passed as parameter %1
rem Using the conf file in the specified path
C:\Python27\Scripts\pylint.exe --rcfile=C:\EPD4\P1\pylint.conf %1
