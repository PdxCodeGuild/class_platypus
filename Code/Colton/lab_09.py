distance = input(f"What is the distance?>")
distance = float(distance)
in_units = input(f"What is the unit type feet, miles, meters or kilometers?>")
out_units = input(f"What do you want to turn that into feet, miles, meters or kilometers?>")
meter_distances = {'feet' : .3048, 'miles':1609.34, 'meters': 1, 'kilometers': 1000 }
out_1 = (distance * meter_distances[in_units])
out_2 = out_1 / meter_distances[out_units]
if out_units == "meters":
    print(f"{distance} {in_units} is {out_1} meters")
elif out_units == "miles" or "feet" or "kilometers":
    print(f"{distance} {in_units} is {out_2} {out_units}")