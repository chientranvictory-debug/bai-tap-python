# Bài 1
price = 120000
quantity = 3
Total = price * quantity
print("Tổng tiền:", Total, "VND")

# Bài 2
price = 500000
chiet_khau = 10
sotien_chiet_khau = price * chiet_khau / 100
print("Số tiền chiết khấu:", sotien_chiet_khau, "VND")
gia_sau_chiet_khau = price - sotien_chiet_khau
print("Giá sau chiết khấu:", gia_sau_chiet_khau, "VND")
# Bài 3
salary_per_day = 300000
working_days = 22
tong_luong = salary_per_day * working_days
print("Tổng lương:", tong_luong, "VND")
# Bài 4
distance_km = 12
cost_per_km = 5000
tong_phi_van_chuyen = distance_km * cost_per_km
print("Tổng phí vận chuyển:", tong_phi_van_chuyen, "VND")
# Bài 5
total_storage = 256
used_storage = 180
dung_luong_con_lai = total_storage - used_storage
print("Dung lượng còn lại:", dung_luong_con_lai, "GB")
# Bài 6
balance = 200000
item_price = 150000
if balance >= item_price:
    print("Thanh toán thành công")
else:    print("Bạn không đủ tiền trong tài khoản")
# Bài 7
order_value = 250000

if order_value >= 200000:
    print("Bạn được miễn phí vận chuyển")
else:
    print("Bạn phải trả phí vận chuyển")
# Bài 8
is_logged_in = True
is_admin = False

if is_logged_in and is_admin:
    print("Người dùng có quyền admin")
else:
    print("Người dùng không có quyền admin")
# Bài 9
hour = 14
if 9 <= hour <= 18:
    print("Trong giờ làm việc")
else:
    print("Ngoài giờ làm việc")
# Bài 10
email = "user@gmail.com"
if "@" in email and "." in email:
    print("Địa chỉ email hợp lệ")
else:
    print("Địa chỉ email không hợp lệ")
    # Bài 11
order_value = 180000
total = order_value

if order_value >= 200000:
    shipping_fee = 0
else:
    shipping_fee = 30000

total = total + shipping_fee

print("Tổng tiền phải trả:", total)
# Bài 12
performance_score = 8.2

if performance_score >= 9:
    bonus = 5000000
elif performance_score >= 7:
    bonus = 2000000
else:
    bonus = 0

print("Thưởng nhân viên:", bonus)
# Bài 13
status_code = 2

if status_code == 1:
    status = "Pending"
elif status_code == 2:
    status = "Shipping"
elif status_code == 3:
    status = "Delivered"
else:
    status = "Unknown"

print("Trạng thái đơn hàng:", status)
# Bài 14
age = 15

if age < 12:
    price = 50000
elif age <= 17:
    price = 70000
else: 
    age >= 18
    price = 100000

print("Giá vé:", price)
# Bài 15
total_spent = 1200000

if total_spent >= 1000000:
    hang = "VIP"
elif total_spent >= 500000:
    hang = "Gold"
else:
    hang = "Normal"

print("Loại khách hàng:", hang)
# Bài 16
kwh = 135
total = 0

if kwh <= 50:
    total = kwh * 1678
elif kwh <= 100:
    total = 50 * 1678 + (kwh - 50) * 1734
else:  # 101 - 200
    total = 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014

print("Tổng tiền điện:", total)
# Bài 17
base_salary = 10000000
kpi = 0.85

if kpi >= 0.9:
    bonus = base_salary * 0.3
elif kpi >= 0.8:
    bonus = base_salary * 0.1
else:
    bonus = 0

tong_luong = base_salary + bonus

print("Lương tổng:", tong_luong)
# Bài 18
distance = 12
total = 0

if distance <= 1:
    total = 15000
elif distance <= 10:
    total = 15000 + (distance - 1) * 12000
else:
    total = 15000 + 9 * 12000 + (distance - 10) * 10000

print("Tiền taxi:", total)
# Bài 19
income = 15000000
debt = 3000000

if income >= 10000000 and debt <= 0.5 * income:
    print("Được vay")
else:
    print("Không được vay")
# Bài 20
price = 1000000
is_member = True
voucher = 100000
if is_member:
    price = price * 0.9
price = price - voucher
if price < 0:
    price = 0
print("Tổng tiền phải trả:", price)
