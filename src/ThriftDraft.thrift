/** Event Format
  * - type
  *   0: data[0]
  *   1: data[1]
  *   n: data[n]
  *   ...
  *
  * - expansionPassedTo
  *   0: expansion (string in format "abbreviation:index,abbreviation:index,..."
  *   1: newPlayer 
  *
  * - setExpansions
  *   0: exp1
  *   1: exp2
  *   2: exp3
  *   n: expn (if I really missed something)
  *
  * - draftStarted
*/
/*struct DEvent {
    1:i32 index,
    2:string type,
    3:i32 sender,
    4:list<string> data,
    5:string senderName
}*/
/*
struct DPlayer
{
    1:i32 playerID,
    2:string playerName,
    3:i32 currentGameID
}*/

service TDraft
{
   oneway void DsetUpDraft(1:i32 draftID, 2:i32 playersExpected, 3:list<string> packNames),
   i32 DregisterPlayer(1:i32 draftID, 2:string playerName),
   oneway void DunregisterPlayer(1:i32 draftID, 2:i32 playerID),
   list<string> DgetAllCards(1:i32 draftID),
   oneway void DsignalReady(1:i32 draftID, 2:i32 playerID),
   bool DeveryoneReady(1:i32 draftID),
   list<string> DgetCurrentPack(1:i32 draftID, 2:i32 playerID),
   oneway void DpickCard(1:i32 draftID, 2:i32 playerID, 3:string card)
}