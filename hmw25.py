#Bai 1
from fastapi import FastAPI, Body, Query
from typing import Dict

app = FastAPI()


def filter_available(products):
    result = []

    for product in products:
        if product["stock"] > 0 and product["is_active"] == True:
            result.append(product)

    return result


@app.post("/products/available")
def get_available_products(payload: Dict = Body(...)):
    products = payload["products"]

    return filter_available(products)

#Bai 2
from fastapi import FastAPI, Body
from typing import Dict

app = FastAPI()

def cart_total(cart):
    total = 0

    for item in cart:
        total += item["price"] * item["quantity"]

    return total


@app.post("/cart/total")
def get_cart_total(payload: Dict = Body(...)):
    cart = payload["cart"]

    return {
        "total": cart_total(cart)
    }

#Bai 3
def apply_discount(total, discount_percent):
    if discount_percent == 0:
        return total

    discount_amount = total * discount_percent / 100
    final_total = total - discount_amount

    return final_total



print(apply_discount(500000, 10))

#Bai 4
from fastapi import FastAPI, Body
from typing import Dict

app = FastAPI()


def order_message(status: str):
    if status == "pending":
        return "Chờ xử lý"
    elif status == "confirmed":
        return "Đã xác nhận"
    elif status == "shipping":
        return "Đang giao"
    elif status == "completed":
        return "Hoàn thành"
    elif status == "cancelled":
        return "Đã hủy"
    else:
        return "Không hợp lệ"
    
@app.post("/order/message")
def get_order_message(payload: Dict = Body(...)):
    status = payload["status"]

    return {
        "message": order_message(status)
    }
                                                             
    
#Bai 5
def shipping_fee(distance_km):
    if distance_km <= 5:
        return 15000
    elif distance_km <= 10:
        return 25000
    else:
        return 40000
print(shipping_fee(8))    

#Bai 6
def login(username, password):
    if username == "admin" and password == "123456":
        return True
    return False
print(login("admin", "123456"))

#Bai 7
def count_status(statuses):
    result = {}

    for status in statuses:
        if status in result:
            result[status] += 1
        else:
            result[status] = 1

    return result

#Bai 8

def find_product(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product

    return None
products = [
    {"id": "SP01", "name": "Áo"},
    {"id": "SP02", "name": "Quần"}
]
print(find_product(products, "SP02"))

#Bai 9

def high_value_orders(orders, min_total):
    result = []

    for order in orders:
        if order["total"] >= min_total:
            result.append(order)

    return result

orders = [
    {"id": 1, "total": 120000},
    {"id": 2, "total": 800000},
    {"id": 3, "total": 450000}
]

print(high_value_orders(orders, 400000))

#Bai 10 
def can_pay(balance, order_total):
    return balance >= order_total

print(can_pay(balance=500000, order_total=350000))

#Bai 11

def update_stock(stock, sold_quantity):
    if sold_quantity > stock:
        return "Không đủ hàng"
    else:
        return stock - sold_quantity
    
print(update_stock(stock=10, sold_quantity=3))   

#Bai 12
def loyalty_points(order_total):
    return order_total // 10000

print(loyalty_points(235000))

#Bai 13

def classify_customer(total_spent):
    if total_spent < 1000000:
        return "normal"
    elif total_spent < 5000000:
        return "silver"
    else:
        return "gold"


# Test
print(classify_customer(5200000))

#Bai 14
def is_valid_email(email):
    if "@" in email and email.endswith(".com"):
        return True
    else:
        return False
print(is_valid_email("user@gmail.com"))

#Bai 15
def active_users(users):
    result = []

    for user in users:
        if user["is_active"] == True:
            result.append(user)

    return result
users = [
    {"id": 1, "name": "An", "is_active": True},
    {"id": 2, "name": "Bình", "is_active": False}
]

print(active_users(users))

#Bai 16

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

def latest_order(orders):
    if len(orders) == 0:
        return None

    latest = orders[0]

    for order in orders:
        if order["id"] > latest["id"]:
            latest = order

    return latest

@app.post("/latest-order")
def get_latest_order(orders: list = Body(...)):
    return latest_order(orders)

#Bai 17
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

def daily_revenue(transactions):
    total = 0
    for transaction in transactions:
        if transaction["status"] == "success":
            total += transaction["amount"]
    return total

@app.post("/daily-revenue")
def get_daily_revenue(transactions: list = Body(...)):
    return  daily_revenue(transactions)

#Bai 18

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    password: str

def hide_password(users):
    result = []

    for user in users:
        result.append({
            "id": user.id,
            "username": user.username
        })

    return result

@app.post("/hide-password")
def hide_user_password(users: List[User]):
    return hide_password(users)
    
#Bai 19

from fastapi import FastAPI

app = FastAPI()

def order_code(order_id: int) -> str:
    return f"ORD-{order_id:05d}"


@app.get("/order-code/{order_id}")
def get_order_code(order_id: int):
    return {
        "order_code": order_code(order_id)
    }

#Bai 20
def is_admin(user):
    return user.get("role") == "admin"
user = {"id": 1, "name": "An", "role": "admin"}

print(is_admin(user))  # True

#Bai 21
def add_vat(price, vat_percent):
    return price * (1 + vat_percent / 100)
print(add_vat(200000, 10))


#Bai 22
from fastapi import FastAPI
from typing import List, Optional

app = FastAPI()


@app.post("/cheapest-product")
def cheapest_product(products: List[dict]) -> Optional[dict]:
    if not products:
        return None

    return min(products, key=lambda product: product["price"])

#Bai 23
def cart_quantity(cart):
    return sum(item["quantity"] for item in cart)

cart = [{"name": "Áo", "quantity": 2}, {"name": "Quần",
"quantity": 1}]
print(cart_quantity(cart))  # Output: 3

#Bai 24

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Request body
class CouponRequest(BaseModel):
    code: str
    coupons: List[str]

@app.post("/coupon-exists")
def coupon_exists(data: CouponRequest):
    return {
        "exists": data.code in data.coupons
    }

#Bai 25

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    name: str
    category: str

class FilterRequest(BaseModel):
    category: str
    products: List[Product]

@app.post("/products/filter")
def filter_by_category(request: FilterRequest):
    result = [
        product for product in request.products
        if product.category == request.category
    ]
    return result