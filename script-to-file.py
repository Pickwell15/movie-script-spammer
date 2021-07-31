# use this to set up a new script (it removes blank / empty lines and formats correctly)
# replace the contents of script-tmp.txt with the new script and then run this file

from string import *

with open("./script-tmp.txt", "r") as f:
    for line in f:
        for char in line:  # this loop checks if the line is empty and if not appends to file
            if char in (ascii_lowercase + ascii_uppercase + digits + punctuation):
                with open("./script.txt", "a") as script:
                    script.write(line)
                break
