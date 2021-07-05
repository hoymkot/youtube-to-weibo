; waite five seconds
  WinWait("[CLASS:#32770]","",5)

; put focus on edit
ControlFocus("File Upload", "","Edit1")

; get file name from param
IF $CmdLine[0] > 0 Then ;???
  $file = $CmdLine[1]


   ; set file path
  ControlSetText("File Upload", "", "Edit1", $file)

   ; sleep 1 seconds
   Sleep(1000)

   ; trigger upload
   ControlClick("File Upload", "","Button1");

EndIf