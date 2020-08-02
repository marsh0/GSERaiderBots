import requests
import re

URL = 'https://www.w3.org/services/html2txt?url=https://www.raidbots.com/reports/hJAhPuD2kizpKnaxnsSZK3/index.html'
response = requests.get(URL)

if response:
    raw_data = response.content.decode("utf-8")
    raw_data = raw_data[raw_data.find('Sample Sequence Table'):]
    raw_data = raw_data[:raw_data.find('Stats')]

    with open('output.txt', 'wt', encoding="utf-8") as the_file:
        lines = raw_data.splitlines()
        lastTimeMS = 0
        for line in lines:
            result = re.search(r'(\d):(\d\d)\.(\d\d\d) (\w+) (\w+) (\w+)', line)
            if result:
                minutes = result.group(1)
                seconds = result.group(2)
                milliseconds = result.group(3)
                identifier = result.group(4)
                ability = result.group(6)

                timeMS = (int(minutes) * 60 * 1000) + (int(seconds) * 1000) + int(milliseconds)

               # the_file.write(str(timeMS - lastTimeMS))
                #the_file.write(" ")
                #the_file.write(identifier)
               # the_file.write(" ")
                if "use_items" in ability :
                    the_file.write('/use [combat] 13\n/use [combat] 14')
                else:
                    the_file.write('/cast [combat] ' + ability.replace('_', ' '))

                the_file.write("\n")

                lastTimeMS = timeMS
#input("Press Enter to continue...")
