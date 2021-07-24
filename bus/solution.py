numberOfStops = 0
stops = [(10,0), (2,4), (5,2)]
for stop in stops:
    numberOfStops += 1

print("There are "+str(numberOfStops)+" stops")

pagsPerStop = []
currentPassengers = 0
for stop in stops:
    currentPassengers = currentPassengers + stop[0] - stop[1]
    pagsPerStop.append(currentPassengers)

#print("Passenger count per stop "+pagsPerStop)
print(pagsPerStop)

currentMax = 0
for stop in pagsPerStop:
    if stop > currentMax:
        currentMax = stop

print("Max occupation was "+str(currentMax))

average = 0
for stop in pagsPerStop:
    average += stop

print("Average accupation is "+str(average/len(pagsPerStop)))