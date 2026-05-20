👉Câu 1
Class là bản thiết kế (template/blueprint) để tạo ra các đối tượng
   Nó định nghĩa:
   Thuộc tính (attributes/data)
   Hành vi (methods/functions)
Object là một thực thể cụ thể được tạo ra từ class.
Ví dụ trong thương mại điện tử:
  Product là một class, iphone, laptop...object cụ thể của class Product
👉 Câu 2: Tác dụng của hàm __init__() và tham số self
Tác dụng chính:
  Khởi tạo dữ liệu ban đầu cho object
  Gán giá trị cho các thuộc tính của object
self đại diện cho chính object hiện tại đang được thao tác.
Tại sao self luôn là tham số đầu tiên?
   Do  object phải được truyền vào trước tiên → nên self luôn đứng đầu.
👉Câu 3: Các loại thuộc tính và phương thức trong Class
Liệt kê và giải thích ba loại phương thức trong Python

    Instance Method Là phương thức làm việc với đối tượng (object) cụ thể.
        Tham số đầu tiên luôn là self.
        Có thể truy cập:
              thuộc tính của object
              các phương thức khác của object
                         Dùng khi thao tác phụ thuộc vào dữ liệu riêng của từng đơn hàng.

             Class Method
                       Là phương thức làm việc với class thay vì object.
                            Dùng decorator @classmethod
                            Tham số đầu tiên là cls (class).
                          Dùng khi thao tác với biến class, tạo object theo cách đặc biệt
 
     Static Method
          Là phương thức không dùng self và cũng không dùng cls.
          Dùng decorator @staticmethod
          Hoạt động giống hàm bình thường nhưng đặt bên trong class để liên quan logic.
         Dùng khi không cần truy cập object,classclass , chỉ là chức năng hỗ trợ liên quan đến class

Cho ví dụ cụ thể cho mỗi loại trong bối cảnh class Order (đơn hàng).
class Order:
    tax_rate = 0.1

    def __init__(self, product, price):
        self.product = product
        self.price = price

    # Instance Method
    def total_price(self):
        return self.price + (self.price * Order.tax_rate)

    # Class Method
    @classmethod
    def update_tax(cls, new_tax):
        cls.tax_rate = new_tax

    # Static Method
    @staticmethod
    def check_price(price):
        return price > 0
o1 = Order("dien thoai", 1000)

print(o1.total_price())

Order.update_tax(0.3)

print(o1.total_price())

print(Order.check_price(200))

👉Câu 4 Tính đóng gói (Encapsulation) và access modifiers

Python không có access modifiers như Public, Protected, Private nhưng sử dụng
convention với dấu gạch dưới (_). Hãy giải thích ba mức độ: public (không có dấu),
protected (_name), private (__name). Giải thích lý do sử dụng getter/setter với ví dụ
class User có thuộc tính __password.

Public Thuộc tính hoặc phương thức không có dấu gạch dưới phía trước.
  Có thể truy cập ở mọi nơi
  Đây là loại mặc định trong Python
Protected (_name) Dùng một dấu gạch dưới _.
    Đây chỉ là quy ước: “thuộc tính này không nên truy cập trực tiếp từ bên ngoài”,Vẫn truy cập được
    Thường dùng khi: muốn class con dùng được, nhưng không muốn người dùng bên ngoài đụng vào nhiều
Private (__name)
    Dùng hai dấu gạch dưới __.,Python thực hiện cơ chế gọi là name mangling(cơ chế “che tên),Nó chủ yếu       để tránh truy cập nhầm

Getter và Setter
  Getter Dùng để lấy dữ liệu private.
  Setter Dùng để cập nhật dữ liệu private có kiểm tra điều kiện

Ví dụ class User với __password

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    # Getter
    def get_password(self):
        return self.__password

    # Setter
    def set_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
            print("Đổi mật khẩu thành công")
        else:
            print("Mật khẩu phải ít nhất 6 ký tự")

Sử dụng:
  u = User("chien", "123456")

  print(u.get_password())  Kết quả:123456

Đổi password:
  u.set_password("abc") Kết quả: Mật khẩu phải ít nhất 6 ký tự

👉Câu 5: Kế thừa (Inheritance) và ghi đè phương thức
Giải thích khái niệm kế thừa trong OOP. Làm thế nào để ghi đè (override) một phương
thức từ lớp cha? Viết ví dụ: tạo lớp cha Person (người), sau đó tạo lớp con Customer
(khách hàng) kế thừa từ Person với phương thức khác nhau.

Kế thừa trong OOP kế thừa là tính chất cho phép một lớp mới nhận lại các thuộc tính và phương thức của lớp đã có

Ghi đè phương thức (Override) verride là khi lớp con viết lại một phương thức đã có ở lớp cha để tạo hành vi khác.

Cách ghi đè phương thức
  Trong lớp con, tạo phương thức có: cùng tên,cùng tham số

class Person:
    def introduce(self):
        print("Tôi là một người")

# Lớp con kế thừa Person
class Customer(Person):

    # Override phương thức introduce()
    def introduce(self):
        print("Tôi là khách hàng")

# Tạo object
p = Person()
c = Customer()

p.introduce()    Kết quả  Tôi là một người
c.introduce()   Kết quả Tôi là khách hàng

👉Câu 6: Scope (Phạm vi hoạt động) của biến trong class
Giải thích khái niệm Scope (phạm vi) trong Python.
Phân biệt giữa: biến global (toàn cục), biến local (cục bộ trong hàm), biến instance
(thuộc về object), và biến class (thuộc về class). Cho ví dụ cụ thể cho mỗi loại trong
class ShoppingCart


Trong Python, Scope (phạm vi) là khu vực mà một biến có thể được truy cập và sử dụng

Biến Global Được khai báo bên ngoài tất cả hàm/class, có thể dùng ở nhiều nơi trong chương trình.

Biến Local  Được tạo bên trong hàm, Chỉ sử dụng được trong hàm đó.

Biến Instance Thuộc về từng object riêng biệt

Biến Class  Thuộc về class, dùng chung cho mọi object, khai báo trực tiếp trong class nhưng ngoài hàm

# Global variable
shop_name = "ABC Store"

class ShoppingCart:

    # Class variable
    tax_rate = 0.1

    def __init__(self, customer):
        # Instance variable
        self.customer = customer

    def checkout(self):
        # Local variable
        total = 1000

        print("Cửa hàng:", shop_name)
        print("Khách hàng:", self.customer)
        print("Thuế:", ShoppingCart.tax_rate)
        print("Tổng tiền:", total)

👉Câu 7: Nguyên lý POLYMORPHISM và ABSTRACTION của OOP

- POLYMORPHISM (Tính đa hình): Cùng một interface (class) nhưng nhiều cách triển
khai khác nhau. Ưu điểm? Cho ví dụ: method move() được override trong Dog, Cat,
Bird nhưng có kết quả khác nhau.- ABSTRACTION (Tính trừu tượng): Ẩn đi các chi tiết phức tạp, chỉ cung cấp interface
đơn giản cho người dùng. Khác gì với Encapsulation? Cho ví dụ: class Shape với
abstract method area()

# Lớp cha
class Animal:
    def move(self):
        print("Động vật đang di chuyển")


# Lớp Dog kế thừa Animal
class Dog(Animal):
    def move(self):
        print("Chó chạy bằng 4 chân")


# Lớp Cat kế thừa Animal
class Cat(Animal):
    def move(self):
        print("Mèo đi nhẹ nhàng")


# Lớp Bird kế thừa Animal
class Bird(Animal):
    def move(self):
        print("Chim bay trên trời")
dog = Dog()
cat = Cat()
bird = Bird()

dog.move()
cat.move()
bird.move()

Kết quả
    Chó chạy bằng 4 chân
    Mèo đi nhẹ nhàng
    Chim bay trên trời

ABSTRACTION (Tính trừu tượng)                        Encapsulation
  Ẩn độ phức tạp                                       Ẩn dữ liệu
  Tập trung vào “làm gì”                               Tập trung vào “bảo vệ dữ liệu”
  Dùng abstract class / abstract method                Dùng private/protected
  Giảm độ phức tạp khi sử dụng                         Ngăn truy cập trực tiếp

Ví dụ class Shape với abstract method area()
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
r = Rectangle(4, 5)
print(r.area())
👉Câu 8: Schema (Sơ đồ thiết kế class) - Cách lập kế hoạch xây dựng class
Giải thích khái niệm Schema trong thiết kế OOP. Các bước cần làm trước khi viết code:
• Xác định các thuộc tính (attributes) và phương thức (methods) cần thiết
• Xác định mối quan hệ giữa các class (kế thừa, composition)
• Xác định public/private cho mỗi thành phần
Hãy vẽ/mô tả schema cho class PaymentProcessor (xử lý thanh toán) với các class con
CreditCardPayment, BankTransferPayment, E-WalletPayment.

Trong OOP, Schema là bản thiết kế mô tả: Class nào sẽ tồn tại, Mỗi class có thuộc tính hành vi gì, Các class liên kết với nhau như thế nào,thành phần nào được phép truy cập từ bên ngoài

Schema hệ thống PaymentProcessor

 
                         +----------------------------------+
                         |        PaymentProcessor          |
                         +----------------------------------+
                         | - amount                         |
                         | - transaction_id                 |
                         | - status                         |
                         +----------------------------------+
                         | + pay()                          |
                         | + validate_payment()             |
                         | + refund()                       |
                         +----------------+-----------------+
                                          |
             +----------------------------+----------------------------+
             |                            |                            |
             v                            v                            v

      +----------------------+   +----------------------+   +----------------------+
      | CreditCardPayment    |   | BankTransferPayment |   | EWalletPayment       |
      +----------------------+   +----------------------+   +----------------------+
      | - card_number        |   | - bank_name          |   | - wallet_id          |
      | - cvv                |   | - account_number     |   | - phone_number       |
      | - expiry_date        |   | - account_holder     |   | - provider           |
      +----------------------+   +----------------------+   +----------------------+
      | + pay()              |   | + pay()              |   | + pay()              |
      | + validate_card()    |   | + verify_bank()      |   | + verify_wallet()    |
      +----------------------+   +----------------------+   +----------------------+


👉Câu 9: Cách vẽ sơ đồ tư duy (Mind Map) để thiết kế class
Giải thích lợi ích của việc vẽ sơ đồ tư duy trước khi code. Các thành phần chính trong
sơ đồ tư duy:
• Tên class ở trung tâm
• Các nhánh chính: Thuộc tính, Phương thức, Quan hệ với class khác
• Chi tiết: tên, kiểu dữ liệu, access level
Hãy mô tả sơ đồ tư duy cho class InventoryManager (quản lý kho hàng).

Lợi ích của sơ đồ tư duy trước khi code

    Tránh thiếu sót logic
    Thiết kế rõ ràng hơn Class được chia thành các phần thay vì viết rời rạc.
    Giảm sửa code về sau
    Hiểu quan hệ giữa các class
    Team có thể hiểu thiết kế nhanh

Sơ đồ tư duy cho class InventoryManager

InventoryManager
│
├── Attributes
│   ├── items (dict)                  mô tả: lưu danh sách hàng hóa trong kho
│   ├── product_details (dict)        mô tả: thông tin chi tiết sản phẩm
│   ├── warehouse_location (str)      mô tả: vị trí kho
│   └── low_stock_threshold (int)     mô tả: ngưỡng cảnh báo hàng tồn thấp
│
├── Methods
│   ├── add_product()
│   ├── update_stock()
│   ├── remove_product()
│   ├── check_stock()
│   ├── is_low_stock()
│   ├── get_all_products()
│   └── generate_report()
│
└── Relationships
    ├── Product (manages)          quản lý nhiều Product
    ├── Order (updates stock)      khi có đơn hàng
    └── Supplier (supplies stock)  khi nhập hàng

👉👉PHẦN II: CÂU HỎI THỰC HÀNH


👉 Xây dựng class Product
class Product:
    def __init__(self, product_id, name, price, quantity, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def apply_discount(self, discount_percent):
        """
        Trả về giá sau khi giảm giá
        """
        discounted_price = self.price * (1 - discount_percent / 100)
        return discounted_price

    def is_in_stock(self):
        """
        Kiểm tra còn hàng hay không
        """
        return self.quantity > 0

p1 = Product("P001", "Laptop", 1000, 5, "Electronics")
p2 = Product("P002", "Mouse", 20, 0, "Electronics")
p3 = Product("P003", "Book", 10, 12, "Education")
products = [p1, p2, p3]
for p in products:
    print("ID:", p.product_id)
    print("Name:", p.name)
    print("Price after 10% discount:", p.apply_discount(10))
    print("In stock:", p.is_in_stock())

👉Bài tập 2: Xây dựng class Customer với Encapsulation

class Customer:
    def __init__(self, customer_id, name, email, password, credit_balance=0):
        # Public attributes
        self.customer_id = customer_id
        self.name = name

        # Protected attribute (quy ước: không truy cập trực tiếp từ bên ngoài)
        self._email = email

        # Private attributes (name mangling)
        self.__password = password
        self.__credit_balance = credit_balance

    # Getter cho credit_balance
    def get_credit_balance(self):
        return self.__credit_balance

    # Setter cho credit_balance (chỉ cho phép >= 0)
    def set_credit_balance(self, value):
        if value >= 0:
            self.__credit_balance = value
        else:
            print("Số dư không hợp lệ (phải >= 0)")

    # Nạp tiền
    def add_credit(self, amount):
        if amount > 0:
            self.__credit_balance += amount
            print(f"Nạp {amount} thành công. Số dư mới: {self.__credit_balance}")
        else:
            print("Số tiền nạp phải > 0")

    # Sử dụng tiền
    def use_credit(self, amount):
        if amount <= 0:
            print("Số tiền sử dụng phải > 0")
            return

        if amount <= self.__credit_balance:
            self.__credit_balance -= amount
            print(f"Đã sử dụng {amount}. Số dư còn lại: {self.__credit_balance}")
        else:
            print("Không đủ số dư")


#  TEST
c = Customer("C001", "An", "an@gmail.com", "123456", 100)

print(c.customer_id)   # OK (public)
print(c.name)          # OK (public)

# print(c.__password)   #  Lỗi: không truy cập trực tiếp được

c.add_credit(50)
c.use_credit(30)

print("Số dư:", c.get_credit_balance())

👉Bài tập 3: Xây dựng class Order và tính tổng tiềnclass Order:
  class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


class Order:
    def __init__(self, order_id, customer, order_date):
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.items = []
        self.quantities = []
        self.discount = 0

    def add_item(self, product, quantity):
        self.items.append(product)
        self.quantities.append(quantity)

    def calculate_total(self):
        total = 0
        for product, qty in zip(self.items, self.quantities):
            total += product.price * qty

        total *= (1 - self.discount / 100)
        return total

    def apply_discount(self, discount_percent):
        self.discount = discount_percent
p1 = Product(1, "Laptop", 1000)
p2 = Product(2, "Mouse", 50)
p3 = Product(3, "Keyboard", 80)

order1 = Order(101, c1, "2026-05-15")
order1.add_item(p1, 1)
order1.add_item(p2, 2)
order1.apply_discount(10)

print("Order 1 total:", order1.calculate_total())

order2 = Order(102, c2, "2026-05-15")
order2.add_item(p3, 2)
order2.add_item(p2, 1)

print("Order 2 total:", order2.calculate_total())

👉👉Bài tập 4: Kế thừa - Tạo class SpecialCustomer từ Customer

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self._email = email  # protected


class SpecialCustomer(Customer):
    def __init__(self, customer_id, name, email):
        super().__init__(customer_id, name, email)
        self.loyalty_points = 0
        self.loyalty_level = "Bronze"

    def add_loyalty_points(self, points):
        self.loyalty_points += points
        self.update_level()

    def update_level(self):
        if self.loyalty_points >= 1000:
            self.loyalty_level = "Gold"
        elif self.loyalty_points >= 500:
            self.loyalty_level = "Silver"
        else:
            self.loyalty_level = "Bronze"

    def get_discount(self):
        if self.loyalty_level == "Gold":
            return 15
        elif self.loyalty_level == "Silver":
            return 10
        else:
            return 5

    def __str__(self):
        return (f"Customer VIP Info:\n"
                f"ID: {self.customer_id}\n"
                f"Name: {self.name}\n"
                f"Email: {self._email}\n"
                f"Loyalty Points: {self.loyalty_points}\n"
                f"Loyalty Level: {self.loyalty_level}\n"
                f"Discount: {self.get_discount()}%")

customer1 = SpecialCustomer(1, "A", "an@gmail.com")

# Mua hàng -> cộng điểm
customer1.add_loyalty_points(200)
customer1.add_loyalty_points(400)

# Xem thông tin
print(customer1)

# Xem riêng discount
print("Giảm giá hiện tại:", customer1.get_discount(), "%")

👉👉Bài tập 5: Polymorphism - Tạo class cho các loại sản phẩm khác nhau
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def calculate_final_price(self):
        return self.price


# 1. PhysicalProduct
class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, weight, shipping_fee):
        super().__init__(product_id, name, price)
        self.weight = weight
        self.shipping_fee = shipping_fee

    def calculate_final_price(self):
        return self.price + self.shipping_fee


# 2. DigitalProduct
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, file_size, license_type):
        super().__init__(product_id, name, price)
        self.file_size = file_size
        self.license_type = license_type  # 'one-time' hoặc 'lifetime'

    def calculate_final_price(self):
        if self.license_type == "one-time":
            return self.price * 0.8  # giảm 20%
        return self.price


# 3. ServiceProduct
class ServiceProduct(Product):
    def __init__(self, product_id, name, price, duration_days, renewal_fee):
        super().__init__(product_id, name, price)
        self.duration_days = duration_days
        self.renewal_fee = renewal_fee

    def calculate_final_price(self):
        return (self.price * self.duration_days) + self.renewal_fee


products = [
    PhysicalProduct(1, "Laptop", 1000, 2.5, 50),
    DigitalProduct(2, "Software", 200, 500, "one-time"),
    DigitalProduct(3, "Cloud App", 300, 1000, "lifetime"),
    ServiceProduct(4, "Hosting", 10, 30, 5)]

for p in products:
    print(f"{p.name}: {p.calculate_final_price()}")
