#!/bin/bash
chmod -R 755 .
rsync --delete -azv --exclude ".git" --exclude "cards" --exclude "userdata" -e ssh ./ mitchell@maxthelizard.dyndns.org:PlamannTheGathering
