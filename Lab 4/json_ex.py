import json

print("Interface Status")
print("="*80)
print("\n")
print("DN                                                 Description           Speed    MTU ")
print("-"*80)

with open("sample-data.json", "r") as file:
    d = json.load(file)
    for i in d['imdata']:
        dn = i['l1PhysIf']['attributes']['dn']
        speed = i['l1PhysIf']['attributes']['speed']
        mtu = i['l1PhysIf']['attributes']['mtu']
        print(f"{dn}                          {speed}   {mtu}" )