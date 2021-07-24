gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

vic_g = 0
vic_s = 0
battle = len(gandalf)-1

print("ROUND 1")
for i in range(battle):
    if gandalf[i] > saruman[i]:
        vic_g += 1
        #print("gandalf")
    else:
        vic_s += 1
        #print("saruman")

if vic_s > vic_g:
    print("The evil won!")
elif vic_g > vic_s:
    print("Good will always win!")
else:
    print("draw")


POWER = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

print("ROUND 2")
vic_s = vic_g = 0

for i in range(battle):
    if POWER[str(gandalf[i])] > POWER[str(saruman[i])]:
        vic_g += 1
        #print("gandalf")
    else:
        vic_s += 1
        #print("saruman")

if vic_s > vic_g:
    print("The evil won!")
elif vic_g > vic_s:
    print("Good will always win!")
else:
    print("draw")

avg_g = 0
avg_s = 0
for spell in gandalf:
    avg_g += POWER[str(spell)]
for spell in saruman:
    avg_s += POWER[str(spell)]

print("gandalf's average is "+str(avg_g/len(gandalf)))
print("sarumans's average is "+str(avg_s/len(saruman)))