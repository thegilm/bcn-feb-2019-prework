well_height = 125
daily_advance = 30
night_retreat = 20
accumulated_distance = 0
days = 0
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]

# basic task
while accumulated_distance < well_height:
    accumulated_distance += daily_advance - night_retreat
    days += 1

print("Days = "+str(days))

# bonus 1
# reset
days = 0
accumulated_distance = 0

# calc
for x in advance_cm:
    days += 1
    accumulated_distance += x
    if accumulated_distance >= well_height: 
        break

#print(str(days)+" days to the top") 
print(days, " days to the top")
print(str(max(advance_cm))+" cm is the max displacement per day, "+str(min(advance_cm))+" cm is the minimum")

average_speed = 0
i = 0
for y in advance_cm:
    i += 1
    average_speed = average_speed + y

print(sum(advance_cm)/len(advance_cm), " cm per day") # schnelle Variante
#print("average speed is "+str(average_speed/i)+" cm per day")
print("actually average speed is "+str(30+21+22+77/4)+" while inside the well...")

mean_value = 0
for z in advance_cm:
    mean_value += z
mean_value = mean_value/len(advance_cm)

sigma = 0
for r in advance_cm:
    sigma += (r-mean_value)*(r-mean_value)/(len(advance_cm)-1)
sigma = sigma**-0.5

print("sigma for this data set is "+str(sigma))
