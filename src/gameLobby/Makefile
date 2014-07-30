all : UI_gameLobby.py UI_createGameWindow.py UI_inGameDialog.py
UI_gameLobby.py : gameLobby.ui
	pyuic4.bat gameLobby.ui > UI_gameLobby.py
UI_createGameWindow.py : createGameWindow.ui
	pyuic4.bat createGameWindow.ui > UI_createGameWindow.py
UI_inGameDialog.py : inGameDialog.ui
	pyuic4.bat inGameDialog.ui > UI_inGameDialog.py
clean:
	rm UI_*.py *.pyc
