#Bai1
products = ["Áo", "Quần", "Giày", "Mũ"]
for i in range(len(products)):
    print(i, products[i])
#Bai2
prices = [100000, 200000, 150000]

total = 0
for i in range(len(prices)):
    total  = total + prices[i]
print("Tổng tiền:", total, "VND")
#Bai3
prices = [100000, 500000, 700000, 200000]

count = 0

for price in prices:
    if price > 300000:
        count += 1

print("Sản phẩm giá cao:", count)
#Bai4
prices = [100000, 500000, 700000, 200000]

max_price = 0

for price in prices:
    if max_price < price:
        max_price = price

print("Giá cao nhất:", max_price)
#Bai5
numbers = [1, 2, 3, 4, 5, 6]

total = 0

for num in numbers:
    if num % 2 == 0:  
        total = total + num

print("Tổng chẵn:", total)
#Bai6
for i in range(1, 6):        
    for j in range(1, 6):    
        print(f"{i} x {j} = {i*j}")
#Bai7
#         
n = 17

is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime == True:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")
#Bai8
orders = ["A", "B", "A", "C", "A"]

count = 0

for item in orders:
    if item == "A":
        count =  count + 1

print("Số lần xuất hiện của A:", count)
#Bai9
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(100, 3)

print("Tổng tiền:", total)
#Bai10
def check_login(is_logged_in):
    if is_logged_in:
        return "Đã đăng nhập"
    else:
        return "Chưa đăng nhập"
    #Sử dụng hàm
print(check_login(True))
#Bai11
def apply_discount(price, percent):
    new_price = price * (1 - percent / 100)
    return new_price
  
#Sử dụng hàm
print(apply_discount(200000, 30))
#Bai12
def is_free_shipping(order_value):
    if order_value >= 100000:
        return True
    else:
        return False

result = is_free_shipping(150000)
print("Free ship:", result)
#Bai13
def classify_customer(total_spent):
    if total_spent >= 2000000:
        return "VIP"
    elif total_spent >= 500000:
        return "Gold"
    else:
        return "Normal"

#Sử dụng hàm
print(classify_customer(2200000))  # Output: VIP
print(classify_customer(600000))   # Output: Gold
print(classify_customer(300000))   # Output: Normal
#Bai14
def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
    
print("Email hợp lệ" ,is_valid_email("user@example.com"))
#Bai15
def total_revenue(orders):
    total = 0
    
    for price in orders:
        total = total +  price
        
    return total
orders = [100000, 200000, 300000]

print(total_revenue(orders))
#Bai16
def filter_prices(prices):
    result = []
    
    for price in prices:
        if price > 300000:
            result.append(price)
    
    return result
prices = [100000, 500000, 700000, 200000]

print(filter_prices(prices))
#Bai17
def check_orders(orders):
    count = 0
    for order in orders:
        if order > 0:
            count += 1
            
    return count
orders = [100000, 0, 200000, -50000]
print(check_orders(orders))
#Bai18
def apply_discount(price):
    return price * 0.9 
prices = [100000, 200000, 300000]

total = 0

for price in prices:
    new_price = apply_discount(price)
    total += new_price

print("Tổng sau giảm:", total)
#Bai19
def vip_checker(cart):
    total = 0
    
    for price in cart:
        total = total + price
    if total >= 3000000:
        return True
    else:
        return False  
    cart = [200000, 1500000, 800000]
    print(vip_checker(cart))
    #Bai20
def checkout(cart, balance):
      total = 0
    
      for price in cart:
        total = total + price
    
      if balance >= total:
        return {
            "status": "Thanh toán thành công",
            "Số dư còn lại": balance - total
        }
      else:
        return {  "status": "Không đủ tiền",
            "Số dư còn lại": balance}
cart = [100000, 200000, 150000]    
balance = 500000

print(checkout(cart, balance))
