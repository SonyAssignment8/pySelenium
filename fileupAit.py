import autoit

#file upload in gmail to compose a file
autoit.win_wait_active("[CLASS:#32770]",3)
autoit.control_send("[CLASS:#32770]","Edit1","bankslip.jpg")
autoit.control_click("[CLASS:#32770]","Button1")

#file download in IE
autoit.win_wait_active("[IEFrame]",3)
autoit.send("!s")

#calendar popups
