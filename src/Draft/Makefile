all : UI_draftUI.py UI_expansionPickerUI.py
UI_draftUI.py : draftUI.ui
	pyuic4 draftUI.ui > UI_draftUI.py
UI_expansionPickerUI.py : expansionPicker.ui
	pyuic4 expansionPicker.ui > UI_expansionPickerUI.py
clean:
	rm UI_*.py *.pyc
