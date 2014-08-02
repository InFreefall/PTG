all:
	pyinstaller src/gamelobby/gamelobby.py --paths=src/ --paths=src/gen-py/
