import os, json
os.system("cls")

fayl=open("people.txt", 'r+')
people=[]
data=fayl.read().split("\n")
for i in range(len(data)):
    malumot=data[i].split(",")
    odam={
        'name': malumot[0],
        'fml': malumot[1],
        'jinsi': malumot[2],
        'yoshi': int(malumot[3]),
        'country': malumot[4]
    }
    people.append(odam)
    a=list(filter(odam['jinsi'] == 'male', people))
print(a)    
print(json.dumps(people, indent=5))
fayl.close()