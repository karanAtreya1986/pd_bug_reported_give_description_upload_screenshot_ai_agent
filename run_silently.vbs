Set WshShell = CreateObject("WScript.Shell")
' Get the directory of the current script to ensure portability
strPath = Left(WScript.ScriptFullName, Len(WScript.ScriptFullName) - Len(WScript.ScriptName))
WshShell.CurrentDirectory = strPath

' Start the server in the background (0 = hide window)
WshShell.Run "python server.py", 0, False
' Wait for server to initialize
WScript.Sleep 2000
' Open the browser
WshShell.Run "http://localhost:5000"
