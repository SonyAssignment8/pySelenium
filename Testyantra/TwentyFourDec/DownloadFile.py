# file Download
import autoit
autoit.win_wait_active("[CLASS:ApplicationFrameInputSinkWindow],3")
autoit.send("!s")  # !+s is used for click on save
