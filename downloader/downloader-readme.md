# sheet-grab
GOAL:<br>
routinely collect and sort spreadsheets(or other files) chronologically

CURRENTLY:<br><br>
SheetHandler(name, url)

1.  if file extension snippet from EXT is in url:     
    * filename = name.extension<br>
2.  if not exists:
    * make directory  ./sheets/<br>
3.  if not exists:
    * make directory  ./sheets/[name]<br>
4.  if not exists file downloaded today:
    * download & save ./sheets/[name]/YYYY-MM-DD_[filename]<br>
