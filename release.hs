#!runhaskell
{-# LANGUAGE OverloadedStrings #-}
import Data.Traversable
import Shelly
import System.Info (os)

requirements = ["pyinstaller.exe"
               ,"scp.exe"
               ,"ssh.exe"
               ]

-- Returns Nothing if all requirements are satisifed
-- if there are missing executables, returns a list containing their names
check_requirements :: Sh (Maybe [Shelly.FilePath])
check_requirements = do
  exists <- traverse test_px requirements
  let pairs = zip requirements exists
      filtered = filter (not.snd) pairs
  if null filtered
    then return Nothing
    else return $ Just (map fst filtered)

test_connection = do
  response <- run "ssh.exe" ["ptg.duckdns.org"
                            ,"echo Hello, world!"]
  return (response == "Hello, world!\n")

make_executable =
  run "pyinstaller.exe"
      ["src/gamelobby/gamelobby.py" -- main game file
      , "--paths=src/"              -- add src to PYTHONPATH
      , "--paths=src/gen-py/"       -- add thrift files
      , "-y"]                       -- overwrite dist directory

copy_database = do
  mkdir "dist/gamelobby/src"
  cp "src/statedb.sqlite3" "dist/gamelobby/src/statedb.sqlite3"

push_dist_to_server = do
  run "scp.exe" ["-r"
                ,"dist/gamelobby"
                ,"ptg.duckdns.org:."
                ]

update_server = do
  run "ssh.exe" ["ptg.duckdns.org"
                ,"cd PTG; git pull"
                ]

main = shelly $ do
  unless (os == "mingw32") $ error "Deployment must happen on Windows"
  missing_requirements <- check_requirements
  has_connection <- test_connection
  unless has_connection $ error "Could not connect to ptg.duckdns.org"
  case missing_requirements of
    Nothing -> return () -- Good to go
    Just reqs -> liftIO $ do
      error $ "Missing Requirements: " ++ (show reqs)
  make_executable
  copy_database
  push_dist_to_server
  update_server