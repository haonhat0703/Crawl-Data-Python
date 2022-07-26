import requests
import json

links = 'https://goctruyentranhhay.com/api/comic/search/recent?p='

f = open("Data.txt", 'w', encoding = 'utf8')

for index in range(10):
    resp = requests.get(links + str(index))
    #soups = BeautifulSoup(resp.content, 'html.parser')
    #data = jsons.dump(soups)
    data = json.loads(resp.content)
    f.write ("PAGE " + str(index+1) + "\n")
    
    for name in data["result"]["data"]:
        f.write(name["name"] + "------" + name["chapterLatest"][0] + "\n")
    
    f.write("\n")        

f.close()    
