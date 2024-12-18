# import required modules
import requests
import html_to_json
import json

# get URL
# page = requests.get("https://en.wikipedia.org/wiki/Main_Page")
page = requests.get("https://tommywestphall.fandom.com/wiki/List_of_television_series_in_the_Tommy_Westphall_Universe")

with open("fileDump/pageStatusCode.txt", "w") as f:
    f.write(str(page.status_code))

# with open("fileDump/pageContent.json", "rb") as f:
#     # html_to_json.convert(page.content)
#     json.dump(html_to_json.convert(page.content), f, indent=4)

with open("fileDump/pageContent.json", "w", encoding="utf-8") as file:
    json.dump(html_to_json.convert(page.content), file, indent=4)