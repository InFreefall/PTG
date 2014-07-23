all: UI_MainPTG.py UI_player.py UI_deckPickerDialog.py UI_opponentInfo.py UI_deckEditor.py UI_settings.py UI_deckValidator.py UI_loadScreen.py

UI_%.py : %.ui
	pyuic4.bat $< > $@ 

clean:
	rm UI_*.py *.pyc
