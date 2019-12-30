import autoit
autoit.win_wait_active("open",3)
autoit.control_send("[CLASS:#32770]","Edit1","notes.txt")
autoit.control_click("[CLASS:#32770]","Button1")