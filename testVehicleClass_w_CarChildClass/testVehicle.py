'''test modVehicle'''
from modVehicle import *

v1 = Vehicle(2020, "purple")
print(v1)
print("The vehicle age is:", v1.calcVehicleAge())

numVehicles = v1.getNumVehicles()
vin = v1.getVIN()
newness = v1.getIsNew()
vAge = v1.getYearManufactured()
color = v1.getColor()
print("There are are", numVehicles, "vehicle/s.")
print("The VIN is:", vin)
print("The vehicle is new:", newness)
print("The vehicle was made in", vAge)
print("The color of the vehicle is:", color, "\n")

v2 = Vehicle(2019, "yellow")
print(v2)
print("The vehicle age is:", v1.calcVehicleAge())

numVehicles = v2.getNumVehicles()
vin = v2.getVIN()
newness = v2.getIsNew()
vAge = v2.getYearManufactured()
color = v2.getColor()
print("There are are", numVehicles, "vehicle/s.")
print("The VIN is:", vin)
print("The vehicle is new:", newness)
print("The vehicle is", vAge, "years old")
print("The color of the vehicle is:", color, "\n")
##v1.setYear(2021)
##v1.setColor("Orange")
numVehicles = v2.getNumVehicles()

print(v2)

c1 = Car(2020,"Grey", "Hyundai")
print(c1)
print("The vehicle age is:", c1.calcVehicleAge())

numVehicles = c1.getNumVehicles()
vin = c1.getVIN()
newness = c1.getIsNew()
vAge = c1.getYearManufactured()
color = c1.getColor()
make = c1.getMake()
numHondas = c1.getNumHondas()
print("There are are", numVehicles, "vehicle/s.")
print("The VIN is:", vin)
print("The vehicle is new:", newness)
print("The vehicle was made in", vAge)
print("The color of the vehicle is:", color, "\n")

c2 = Car(2020,"Cyan", "Honda")
print(c2)
print("The vehicle age is:", c2.calcVehicleAge())

numVehicles = c2.getNumVehicles()
vin = c2.getVIN()
newness = c2.getIsNew()
vAge = c2.getYearManufactured()
color = c2.getColor()
make = c2.getMake()
numHondas = c2.getNumHondas()
print("There are are", numVehicles, "vehicle/s.")
print("The VIN is:", vin)
print("The vehicle is new:", newness)
print("The vehicle was made in", vAge)
print("The color of the vehicle is:", color, "\n")

c3 = Car(2020,"Blue", "Honda")
print(c3)
print("The vehicle age is:", c3.calcVehicleAge())

numVehicles = c3.getNumVehicles()
vin = c3.getVIN()
newness = c3.getIsNew()
vAge = c3.getYearManufactured()
color = c3.getColor()
make = c3.getMake()
numHondas = c3.getNumHondas()
print("There are are", numVehicles, "vehicle/s.")
print("The VIN is:", vin)
print("The vehicle is new:", newness)
print("The vehicle was made in", vAge)
print("The color of the vehicle is:", color, "\n")



