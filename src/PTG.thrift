struct Event {
    1:i32 index,
    2:string type,
    3:i32 sender,
    4:list<string> data,
    5:string senderName
}

struct Player
{
    1:i32 playerID,
    2:string playerName
}

service PTG {
    i32 registerPlayer(1:i32 gameID, 2:string playerName, 3:i32 team),
    oneway void unregisterPlayer(1:i32 gameID, 2:i32 playerID),
    oneway void setDeck(1:i32 gameID, 2:i32 playerID, 3:string deckName, 4:i32 deckSize),
    oneway void moveCard(1:i32 gameID, 2:i32 playerID, 3:string abbreviation, 4:string index, 5:i32 originalPosition, 6:i32 newPosition, 7:bool tapped),
    oneway void removeCardFrom(1:i32 gameID, 2:i32 playerID, 4:i32 zone, 5:i32 position),
    oneway void addCardTo(1:i32 gameID, 2:i32 playerID, 3:string cardString, 4:i32 zone, 5:i32 position),
    oneway void setCardTo(1:i32 gameID, 2:i32 playerID, 3:string cardString, 4:i32 zone, 5:i32 position),
    oneway void setLife(1:i32 gameID, 2:i32 playerID, 3:i32 life),
    oneway void setPoison(1:i32 gameID, 2:i32 playerID, 3:i32 posion),
    oneway void reveal(1:i32 gameID, 2:i32 playerID, 3:string abbreviation, 4:string index),
    oneway void event(1:string eventType, 2:i32 gameID, 3:i32 playerID, 4:list<string> data),
    list<Event> getEvents(1:i32 gameID, 2:i32 sinceIndex),
    list<string> listDecks(1:string directory),
    string getDeck(1:string directory, 2:string deckName),
    oneway void saveDeck(1:string deckName, 2:string deck, 3:string directory),
    string VERSION()
}
