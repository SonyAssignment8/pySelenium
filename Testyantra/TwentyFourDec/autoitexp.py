# for uploading,
# you have to follow same steps to open Gmail till dialog box open then follow below steps.
import autoit
# Upload
autoit.win_wait_active("[CLASS:#32770],3")
autoit.control_send("[CLASS:#32770]", "Edit1", "oopss concept.docx")
autoit.control_click("[CLASS:#32770]","Button1")