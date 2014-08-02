#!/bin/bash
rsync --delete -azv --exclude ".git" --exclude "cards" --exclude "userdata" -e ssh ./ mitchell@maxthelizard.doesntexist.com:PlamannTheGathering
