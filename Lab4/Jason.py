import json

data = open('sample-file.json').read()
object = json.loads(data)

print("======================================================================================")
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<6}")
print("-------------------------------------------------- -------------------  -------  -----")

data = object.get("imdata", [])

for i in data:
    l1_Phys_If = i.get('l1PhysIf', {}).get('attributes', {})
    dn = l1_Phys_If.get('dn', '')
    desc = l1_Phys_If.get('descr', '')
    speed = l1_Phys_If.get('speed', '')
    mtu = l1_Phys_If.get('mtu', '')

    print(f"{dn:<50}{desc:<22}{speed:<10}{mtu:<6}")