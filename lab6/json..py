import json

with open('sample-data.json', 'r') as f:
    data = json.load(f)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU
-------------------------------------------------- --------------------  ------  ------""")

for entry in data["imdata"]:
    dn = entry["l1PhysIf"]["attributes"]["dn"]
    speed = entry["l1PhysIf"]["attributes"].get("speed", "inherit")
    mtu = entry["l1PhysIf"]["attributes"].get("mtu", "")

    print("{:<50} {:<20} {:<8} {:<6}".format(dn, "", speed, mtu))
