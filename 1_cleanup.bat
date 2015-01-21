@ECHO OFF

RMDIR /Q /S .\bin

RMDIR /Q /S .\build
RMDIR /Q /S .\dist
RMDIR /Q /S .\tmp
DEL /Q /F *.log
DEL /Q /F ver.txt