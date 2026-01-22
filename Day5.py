#Lists --> Operators --> indexing

tfc = ["eat", "ride", "repeat"]
print(tfc)

'''
for i in tfc:
    print(i)
    if i == "ride":
        print("Sucessful")
    else:
        print("not a perfect task") 
'''

tfc.append("target")
print(tfc)
tfc.copy()
tfc.extend("walk")
tfc.index("eat")
tfc.insert(5, 7)
tfc.pop(3)
tfc.reverse()


print(tfc)

