# import required modules
import requests
import html_to_json
import json
from pathlib import Path


def orchestrator():
    with open('resources/sources.json', 'r') as file:
        sourceHash=json.load(file)
    for source in sourceHash:
        urlJsonCreater(source,sourceHash[source])

def urlJsonCreater(source,url):
    try:
        page = requests.get(url)
        page.raise_for_status()
        Path("fileDump/jsonDump/"+source).mkdir(parents=True, exist_ok=True)
        if int(str(page.status_code)[0])==2:
            with open("fileDump/jsonDump/"+source+"/pageContent.json", "w", encoding="utf-8") as file:
                json.dump(html_to_json.convert(page.content), file, indent=4)
    except requests.exceptions.HTTPError as e:
        print("ERROR: Recieved {} error code with trying to get page from {} at URL: {}".format(e.response.status_code,source,url))
    except Exception as e:
        print("ERROR: Unknown error seen with trying to get page from {} at URL: {}".format(source,url))
        print("ERROR: See stacktrace for more details: \n {}".format(e))
        

################################################################# TEST FUNCTIONS #################################################################

def orchestratorTest():
    urlJsonCreater("twWordPress1","https://thetommywestphallwordpress.com/themaster-list/")
    urlJsonCreater("twWordPress2","https://thetommywestphall.wordpress.com/themasterlist/")
    
##################################################################################################################################################

if __name__ == "__main__":
    orchestrator()

    # exception handling tests
    orchestratorTest()