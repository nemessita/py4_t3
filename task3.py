# Müştəriyə səyahətin ümumi dəyərini hesablamaq üçün nəqliyyat şirkətinə Python proqramı yazın. 
# İstifadəçidən səyahət məsafəsini və nəqliyyat vasitəsinin növünü 
# (məsələn, avtomobil, yük maşını, avtobus) daxil etməyi təklif edin. 
# Verilən məsafəyə və nəqliyyat vasitəsinin növünə əsaslanaraq ümumi dəyəri hesablayın 
# (avtomobillərin hər km üçün 0,50 dollar, yük maşınlarının hər km üçün 1,00 dollar, 
#  avtobusların hər km üçün qiyməti 2,00 dollar).

# Əhatə olunan biliklər: İnput, Variables, Float, Əsas Operatorlar, If...Else.


distance = int(input("Enter the distance: "))
vehicle = input("Enter the vehicle type: ")

motor = ("car", "bus", "truck")
price_list = {
    "car": 0.5,
    "bus": 1,
    "truck": 2
}

if vehicle in motor:
    total_price = distance * price_list[vehicle]
    print("Total price:", total_price)
else:
    print("Invalid vehicle type.")