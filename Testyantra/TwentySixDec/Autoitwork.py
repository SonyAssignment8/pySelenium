import autoit
import time
autoit.win_wait("open",3)
autoit.control_send("open","Edit1","filename")
time.sleep(20)
autoit.control_click("open","button1")
time.sleep(20)

