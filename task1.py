# İstifadəçidən boyu ilə bağlı məlumat alan və ona tövsiyə olunan ideal cəki aralığını göstərən proqram hazırlayın. 
 
# Əhatə olunan biliklər: İnput, Variables, Float, If...Else.

height = float(input("your height: "))

if height <= 120:
    print("lilliput")
elif height > 120 and height < 180:
    print("normal")
elif height >= 180:
    print("tall")
else:
    print("invalid")
   