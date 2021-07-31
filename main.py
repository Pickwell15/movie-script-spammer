# default script is bee movie, use script-to-file.py to change the script
# also in the payload dict add any values needed to be passed in that arent headers in the typical dictionary format ("key": "value")
# any additional required headers can be added in the headers dict and can be added in typical dictionary format as mentioned above ^

import requests  # requests module will need to be installed if not already
import json

if __name__ == "__main__":
    with open("./script.txt", "r") as f:
        count: int = 0

        for line in f:  # loops through each line of script.txt, line = line[count - 1] of script.txt
            count += 1

            payload: dict[any, any] = {  # packet data (e.g. username, password, etc.)
               # add data to send via POST in standard Python dictionary format
            }

            headers: dict[any, any] = {  # packet headers (incl. user agent)
                # add data to send in the headers of the packet in standard Python dictionary format
            }

            r = requests.post(url, data=json.dumps(payload), headers=headers)  # send request
            print(r.text)  # print returned data

            print(f"\n\nSuccess on line: {count}!\n\n")
        print("\n\n\n\n\nWebsite has been spammed with The Bee Movie Script!!")
