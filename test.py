import os, xml.etree.ElementTree as ET, requests
import time

print(os.listdir())
tree = ET.parse("core-items.xml")

root = tree.getroot()
itemtypes = root.find("itemtypes")
os.makedirs("./docs", exist_ok=True)
string = "@startuml\n"
for itemtype in itemtypes:
    attributes = itemtype.find("attributes")
    string +="skinparam class {\n"
    string +="    BackgroundColor White\n"
    string +="    BorderColor Black\n"
    string +="    ArrowColor Black\n"
    string +="}\n"
    string +=f"package core" + " {\n"
    string +=f"    class {itemtype.get('code')}" + " {\n"
    for attribute in attributes:
        string +=f"        {attribute.get('qualifier')}: {attribute.get('type')}\n"
    string +="    }\n"
    string +="}\n"
string +="@enduml\n"
with open("./docs/core.puml", "w+") as f:
    f.write(string)
#delay request to wait for plantuml server to start
time.sleep(5)
response = requests.post("http://test-plantuml-1:8080/svg", data=string)
with open("./docs/core.svg", "wb") as f:
    f.write(response.content)