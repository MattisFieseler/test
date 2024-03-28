import os, xml.etree.ElementTree as ET

print(os.listdir())
tree = ET.parse("core-items.xml")

root = tree.getroot()

itemtypes = root.find("itemtypes")
for itemtype in itemtypes:
    attributes = itemtype.find("attributes")
    with open("/docs/core.puml", "w+") as f:
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

print(os.listdir())
with open("/docs/core.puml", "r") as f:
    print(f.read())