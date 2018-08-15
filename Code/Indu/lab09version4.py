#convert units to meter
#created by Indu Thekkemeppilly Sivakumar on 08/15/2018
inunit= input("What is the unit of your input? feet,meters,Kilometer,mile,yard,inch\n")
outunit= input("what is the unit of your output? feet,meters,Kilometer,mile,yard,inch\n")
distance= float(input("What is the distace?"))
convert2meter = {'feet':0.3048, 'meters':1, 'kilometer':1000, 'mile':1609.34,'yard':0.9144,'inch':0.0254}
distanceinmeter= convert2meter[inunit]*distance

print(f"{distance} {inunit} is {distanceinmeter/convert2meter[outunit]} {outunit}")



