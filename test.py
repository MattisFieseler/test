import os, xml.etree.ElementTree as ET, requests

print(os.listdir())
tree = ET.parse("core-items.xml")

root = tree.getroot()

itemtypes = root.find("itemtypes")
os.makedirs("./docs", exist_ok=True)
for itemtype in itemtypes:
    attributes = itemtype.find("attributes")
    with open("./docs/core.puml", "a+") as f:
        f.write("@startuml\n")
        f.write("skinparam class {\n")
        f.write("    BackgroundColor White\n")
        f.write("    BorderColor Black\n")
        f.write("    ArrowColor Black\n")
        f.write("}\n")
        f.write(f"package core" + " {\n")
        f.write(f"    class {itemtype.get('code')}" + " {\n")
        for attribute in attributes:
            f.write(f"        {attribute.get('qualifier')}: {attribute.get('type')}\n")
        f.write("    }\n")
        f.write("}\n")
        f.write("@enduml\n")

print(os.listdir("./docs"))
with open("./docs/core.puml", "r") as f:
    print(f.read())

response = requests.post("http://test_plantuml_1:8080/svg", data={"plantuml": open("./docs/core.puml", "r").read()})
with open("./docs/core.svg", "w+") as f:
    f.write(response.content)