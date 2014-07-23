set RSYNC_PASSWORD=plamannthegathering
rsync -azv --exclude ".git" --exclude "*.pyc" --exclude "userdata" --exclude "installers" --exclude "src/server" --exclude "reindentBak" --delete ptg@maxthelizard.doesntexist.com::PlamannTheGathering ..
pause
