# Ransomware Defender

This is the second assignment in the cyber defence lab course. 
in this task we were asked to create a monitor that detects if files were encrypted 

In my monitor I check three things:
* If the file is locked 
* If the file's extantion is `.txt`
* If all the characters in the file are ASCII encoded

the file is detected as encrypted if one of the tests doesn't pass

the main program is `defender.py` and three txt files are added to the folder to demostrate the monitors work.
