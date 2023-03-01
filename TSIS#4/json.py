import json

with open('sample_data.json') as outfile:
    data = json.load(outfile)
    print("""
    Interface Status
    ================================================================================
    DN                                                 Description           Speed    MTU  
    -------------------------------------------------- --------------------  ------  ------""")
    imdata = data["imdata"]
for i in imdata:
    l1PhysIf = i["l1PhysIf"]
    attributes = l1PhysIf["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(dn + "                     " + speed + "   " + mtu)
