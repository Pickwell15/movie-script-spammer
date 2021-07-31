# Movie Script Spammer

- This repo contains all the necessary code to send a movie script through a post request to a website.

- The default script (in script.txt) is the bee movie script.
- To change the script you need to change the contents of script-tmp.txt to the desired script and run script-to-file.py.

- The packet payload and headers have not been filled with any content as the variable names required for each scenario are different. 
- Usually headers can be left empty unless a site requires you to have a certain user agent to access. 
- The payload however will need to be filled in, the input you would like to be the line of the script should use the variable 'line' as set in main.py.
- I recommend using Burpsuite to find out the variable names you need to send in the payload and headers.
- More info is available in the headers of each .py file.
