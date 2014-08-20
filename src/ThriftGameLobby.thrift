/** Event Format
  * - type
  *   0: data[0]
  *   1: data[1]
  *   ...
  *
  * - addGame
  *   0: gameID    (you can then look up the game itself)
  *
  * - gameStarted  (the game stays in the lobby so that players can rejoin)
  *   0: gameID
  *
  * - removeGame
  *   0: gameID
  *
  * - addPlayer
  *   1: playerName
  *
  * - removePlayer
  *
  * - playerJoinedGame
  *   0: gameID    (sender is player that joined)
  *
  * - playerLeftGame
  *   0: gameID    (so that gameLobby can adjust the players-in-game number appropriately)
  *
  * - expansionPassedTo
  *   0: expansion (string in format "abbreviation:index,abbreviation:index,..."
  *   1: newPlayer
  *   2: gameID 
  *
*/
struct GLEvent {
    1:i32 index,
    2:string type,
    3:i32 sender,
    4:list<string> data,
    5:string senderName
}

struct GLPlayer
{
    1:i32 playerID,
    2:string playerName,
    3:i32 currentGameID,
    4:i32 team
}

struct GLGame
{
    1:i32 gameID,
    2:string name,
    3:i32 owner,
    4:list<GLPlayer> players,
    5:string type,
    6:list<string> expansions,
    7:bool started
}

service TGameLobby
{
    i32 GLregisterPlayer(1:string playerName),
    oneway void GLunregisterPlayer(1:i32 playerID),
    GLGame GLgameWithID(1:i32 gameID),
    GLGame GLnewGame(1:i32 playerID, 2:string name, 3:string type, 4:list<string> expansions),
    bool GLrequestToJoinGame(1:i32 playerID, 2:i32 gameID),
    oneway void GLswitchToTeam(1:i32 playerID, 2:i32 gameID, 3:i32 team),
    oneway void GLcancelGame(1:i32 playerID, 2:GLGame game),
    list<GLPlayer> GLgetPlayersInLobby(),
    list<GLGame> GLgetGames(),
    list<GLPlayer> GLgetPlayersInGame(1:GLGame game),
    GLGame GLgetGame(1:i32 gameID),
    oneway void GLstartGame(1:i32 gameID),
    oneway void GLaddEvent(1:GLEvent event), // TODO: Find a way to use this

    // Patcher support
    string getFileChecksums(),
    binary getFile(1:string filename),
    
    // Draft functions
    oneway void GLpassExpansion(1:i32 gameID, 2:i32 playerID, 3:string expansion),
    
    i32 GLcurrentEventIndex(),
    list<GLEvent> GLgetEvents(1:i32 sinceIndex)
}