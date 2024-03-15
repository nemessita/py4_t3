# Onlayn mağaza üçün alış-veriş səbəti sistemini simulyasiya edən proqram hazırlayın. 
# İstifadəçilərə səbətinə əşyalar əlavə etməyə, vergilər(18% ədv ümumi qiymetin üzərinə gəlməlidir) 
# daxil olmaqla ümumi dəyəri hesablamağa kömək edir. əgər ümumi qiymət (ədv daxil) 50 azn dən çox olarsa 
# istifadəciyə ən sonra 10 azn lik kupon qazandınız mesajını verin. əgər ümumi qiymət (ədv daxil) 100 azn dən 
# çox olarsa istifadəciyə ən sonra 15 azn lik kupon qazandınız mesajını verin.
# İstifadəçi səbətə 5 dəfə məhsul əlavə edə bilər.
    
# Əhatə olunan biliklər: İnput, Variables, List, Float, Dictionaries, Əsas Operatorlar, If...Else.


product = ("Apple", "Banana", "Orange", "Mango", "Pineapple", "Strawberry", "Grape", "Watermelon", "Kiwi", "Pear")
prices_list = {
    "Apple": 5,
    "Banana": 3,
    "Orange": 2,
    "Mango": 10,
    "Pineapple": 15,
    "Strawberry": 12,
    "Grape": 1,
    "Watermelon": 2,
    "Kiwi": 10,
    "Pear": 4
}

product_name = input("Enter the product name: ")
weight = float(input("Enter the weight in kilograms: "))

if product_name in prices_list:
    total_price = prices_list[product_name] * weight * 1.18
    print("Total price for", product_name, ":", total_price )
    if total_price > 100:
        print("kupon 15")
    elif total_price > 50:
        print("kupon 10")
else:
    print("Product not found in the list.")


