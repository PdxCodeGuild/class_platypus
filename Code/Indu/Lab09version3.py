#convert units to meter
#created by Indu Thekkemeppilly Sivakumar on 08/15/2018
inunit= input("What is the unit of your input? feet,meters,Kilometer,mile,yard,inch\n")
distance= float(input("What is the distace?"))
convert2meter = {'feet':0.3048, 'meters':1, 'kilometer':1000, 'mile':1609.34,'yard':0.9144,'inch':0.0254}
print(f"{distance} {inunit} is {distance*convert2meter[inunit]} meters ")



