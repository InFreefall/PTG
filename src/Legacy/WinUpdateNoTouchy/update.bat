set RSYNC_PASSWORD=plamannthegathering
rsync -azv --exclude ".git" --exclude "*.pyc" --exclude "cards" --include "cards/tokens" --exclude "userdata" --exclude "installers" --exclude "server" --exclude "reindentBak" --delete ptg@maxthelizard.doesntexist.com::PlamannTheGathering ..\..
