@ECHO OFF
setlocal
set PYTHONPATH=%PYTHONPATH%;%cd%\src;%cd%\src\server;%cd%\src\gen-py;%cd%\src\thrift
python src/server/serverManager.py
endlocal
