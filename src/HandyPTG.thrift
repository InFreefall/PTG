struct HPTGEvent {
    1:i32 index,
    2:string type,
    3:i32 sender,
    4:list<string> data,
    5:string senderName
}

service HandyPTG
{
    list<HPTGEvent> HPTGgetEvents(1:i32 sinceIndex),
    void HPTGdrawCard(),
    void HPTGplayCard(1:string abbreviation, 2:string index),
    void HPTGlandCard(1:string abbreviation, 2:string index),
    void HPTGdiscardCard(1:string abbreviation, 2:string index),
    string HPTGgetCard(1:string abbreviation, 2:string index)
}
