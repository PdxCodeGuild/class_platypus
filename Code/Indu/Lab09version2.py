inunit= input("What is the unit of your input? feet,meters,Kilometer,mile\n")
distance= float(input("What is the distace?"))
convert2meter = {'feet':0.3048, 'meters':1, 'kilometer':1000, 'mile':1609.34}
print(f"{distance} {inunit} is {distance*convert2meter[inunit]} meters ")


