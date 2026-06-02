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
                                                             
    
# #Bai 5
# def shipping_fee(distance_km):
#     if distance_km <= 5:
#         return 15000
#     elif distance_km <= 10:
#         return 25000
#     else:
#         return 40000
# print(shipping_fee(8))    

# #Bai 6
# def login(username, password):
#     if username == "admin" and password == "123456":
#         return True
#     return False
# print(login("admin", "123456"))

# #Bai 7
# def count_status(statuses):
#     result = {}

#     for status in statuses:
#         if status in result:
#             result[status] += 1
#         else:
#             result[status] = 1

#     return result

# #Bai 8

# def find_product(products, product_id):
#     for product in products:
#         if product["id"] == product_id:
#             return product

#     return None
# products = [
#     {"id": "SP01", "name": "Áo"},
#     {"id": "SP02", "name": "Quần"}
# ]
# print(find_product(products, "SP02"))

# #Bai 9

# def high_value_orders(orders, min_total):
#     result = []

#     for order in orders:
#         if order["total"] >= min_total:
#             result.append(order)

#     return result

# orders = [
#     {"id": 1, "total": 120000},
#     {"id": 2, "total": 800000},
#     {"id": 3, "total": 450000}
# ]

# print(high_value_orders(orders, 400000))

# #Bai 10 
# def can_pay(balance, order_total):
#     return balance >= order_total

# print(can_pay(balance=500000, order_total=350000))

# #Bai 11

# def update_stock(stock, sold_quantity):
#     if sold_quantity > stock:
#         return "Không đủ hàng"
#     else:
#         return stock - sold_quantity
    
# print(update_stock(stock=10, sold_quantity=3))   

# #Bai 12
# def loyalty_points(order_total):
#     return order_total // 10000

# print(loyalty_points(235000))

# #Bai 13

# def classify_customer(total_spent):
#     if total_spent < 1000000:
#         return "normal"
#     elif total_spent < 5000000:
#         return "silver"
#     else:
#         return "gold"


# # Test
# print(classify_customer(5200000))

# #Bai 14
# def is_valid_email(email):
#     if "@" in email and email.endswith(".com"):
#         return True
#     else:
#         return False
# print(is_valid_email("user@gmail.com"))

# #Bai 15
# def active_users(users):
#     result = []

#     for user in users:
#         if user["is_active"] == True:
#             result.append(user)

#     return result
# users = [
#     {"id": 1, "name": "An", "is_active": True},
#     {"id": 2, "name": "Bình", "is_active": False}
# ]

# print(active_users(users))

# #Bai 16

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# def latest_order(orders):
#     if len(orders) == 0:
#         return None

#     latest = orders[0]

#     for order in orders:
#         if order["id"] > latest["id"]:
#             latest = order

#     return latest

# @app.post("/latest-order")
# def get_latest_order(orders: list = Body(...)):
#     return latest_order(orders)

# #Bai 17
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# def daily_revenue(transactions):
#     total = 0
#     for transaction in transactions:
#         if transaction["status"] == "success":
#             total += transaction["amount"]
#     return total

# @app.post("/daily-revenue")
# def get_daily_revenue(transactions: list = Body(...)):
#     return  daily_revenue(transactions)

# #Bai 18

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# class User(BaseModel):
#     id: int
#     username: str
#     password: str

# def hide_password(users):
#     result = []

#     for user in users:
#         result.append({
#             "id": user.id,
#             "username": user.username
#         })

#     return result

# @app.post("/hide-password")
# def hide_user_password(users: List[User]):
#     return hide_password(users)
    
# #Bai 19

# from fastapi import FastAPI

# app = FastAPI()

# def order_code(order_id: int) -> str:
#     return f"ORD-{order_id:05d}"


# @app.get("/order-code/{order_id}")
# def get_order_code(order_id: int):
#     return {
#         "order_code": order_code(order_id)
#     }

# #Bai 20
# def is_admin(user):
#     return user.get("role") == "admin"
# user = {"id": 1, "name": "An", "role": "admin"}

# print(is_admin(user))  # True

# #Bai 21
# def add_vat(price, vat_percent):
#     return price * (1 + vat_percent / 100)
# print(add_vat(200000, 10))


# #Bai 22
# from fastapi import FastAPI
# from typing import List, Optional

# app = FastAPI()


# @app.post("/cheapest-product")
# def cheapest_product(products: List[dict]) -> Optional[dict]:
#     if not products:
#         return None

#     return min(products, key=lambda product: product["price"])

# #Bai 23
# def cart_quantity(cart):
#     return sum(item["quantity"] for item in cart)

# cart = [{"name": "Áo", "quantity": 2}, {"name": "Quần",
# "quantity": 1}]
# print(cart_quantity(cart))  # Output: 3

# #Bai 24

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# # Request body
# class CouponRequest(BaseModel):
#     code: str
#     coupons: List[str]

# @app.post("/coupon-exists")
# def coupon_exists(data: CouponRequest):
#     return {
#         "exists": data.code in data.coupons
#     }

# #Bai 25

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# class Product(BaseModel):
#     name: str
#     category: str

# class FilterRequest(BaseModel):
#     category: str
#     products: List[Product]

# @app.post("/products/filter")
# def filter_by_category(request: FilterRequest):
#     result = [
#         product for product in request.products
#         if product.category == request.category
#     ]
#     return result

# #Bai 26
# def is_locked(failed_attempts):
#     return failed_attempts >= 5

# # Test
# print(is_locked(5))

# #Bai 27
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/normalize-name")
# def normalize_name(name: str):
#     normalized = name.strip().title()

#     return {
#         "original": name,
#         "normalized": normalized
#     }
# #Bai 28

# def calculate_salary(hours, rate):
#     if hours <= 40:
#         return hours * rate
#     else:
#         normal = 40 * rate
#         overtime = (hours - 40) * rate * 1.5
#         return int(normal + overtime)
# print(calculate_salary(hours=45, rate=50000))

# #Bai 29
# def count_urgent(tickets):
#     count = 0

#     for ticket in tickets:
#         if ticket["priority"] == "urgent":
#             count += 1

#     return count


# tickets = [
#     {"id": 1, "priority": "normal"},
#     {"id": 2, "priority": "urgent"},
#     {"id": 3, "priority": "urgent"}
# ]

# print(count_urgent(tickets))

# #Bai 30
# def progress_percent(done_tasks, total_tasks):
#     if total_tasks == 0:
#         return 0
#     return (done_tasks / total_tasks) * 100
# print(progress_percent(3, 10))

# #Bai 31
# from fastapi import FastAPI

# app = FastAPI()

# customers = [
#     {"name": "An", "phone": "0901"},
#     {"name": "Bình", "phone": "0902"}
# ]

# def find_customer(customers, phone):
#     for customer in customers:
#         if customer["phone"] == phone:
#             return customer

#     return None

# @app.get("/customer/{phone}")
# def get_customer(phone: str):
#     return find_customer(customers, phone)

# #Bai 32
# def username_exists(users, username):
#     for user in users:
#         if user["username"] == username:
#             return True
#     return False

# users = [
#     {"username": "admin"},
#     {"username": "user01"}
# ]
# print(username_exists(users, "admin"))

# #Bai 33

# def paid_orders(orders):
#     return [
#         order for order in orders
#         if order["is_paid"] == True
#     ]

# orders = [
#     {"id": 1, "is_paid": True},
#     {"id": 2, "is_paid": False}
# ]
# print(paid_orders(orders))

# #Bai 34
# def refund_total(transactions):
#     total = 0

#     for transaction in transactions:
#         if transaction["type"] == "refund":
#             total += transaction["amount"]

#     return total
# transactions = [
#     {"type": "payment", "amount": 500000},
#     {"type": "refund", "amount": 120000},
#     {"type": "refund", "amount": 80000}
# ]

# print(refund_total(transactions))

# #Bai 35
# def is_wishlisted(product_id, wishlist):
#     return product_id in wishlist
# wishlist = {"SP001", "SP005", "SP012"}

# print(is_wishlisted("SP005", wishlist))

#Bai 36

def unique_categories(products):
    categories = set()

    for product in products:
        categories.add(product["category"])

    return categories

products = [
    {"name": "Áo", "category": "ao"},
    {"name": "Quần", "category": "quan"},
    {"name": "Áo khoác", "category": "ao"}
]

print(unique_categories(products))

#Bai 37
def count_missing(values):
    return values.count(None)
values = [120, None, 350, None, 500]

print(count_missing(values))

#Bai 38
def average_rating(reviews):
    if not reviews:
        return 0

    total = sum(review["rating"] for review in reviews)
    return total / len(reviews)
reviews = [{"rating": 5}, {"rating": 4}, {"rating": 3}]

print(average_rating(reviews))

#Bai 39

def ticket_label(priority):
    if priority == "urgent":
        return "Xử lý ngay"
    elif priority == "high":
        return "Ưu tiên cao"
    elif priority == "normal":
        return "Bình thường"
    else:
        return "Không xác định"

print(ticket_label("high"))   

#Bai 40
def available_rooms(rooms):
    count = 0

    for room in rooms:
        if room["status"] == "empty":
            count += 1

    return count
rooms = [
    {"room": "101", "status": "booked"},
    {"room": "102", "status": "empty"},
    {"room": "103", "status": "empty"}
]
print(available_rooms(rooms))

#Bai 41

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


@app.post("/catalog")
def build_catalog(products: list = Body(...)):
    catalog = {}

    for product in products:
        catalog[product["id"]] = product

    return catalog

#Bai 42
def apply_coupon(cart_total, code, coupon_db):
    if code not in coupon_db:
        return {
            "valid": False,
            "message": "Mã giảm giá không tồn tại"
        }

    coupon = coupon_db[code]

    if cart_total < coupon["min_order"]:
        return {
            "valid": False,
            "message": "Chưa đạt giá trị đơn hàng tối thiểu"
        }

    if coupon["type"] == "percent":
        discount_amount = cart_total * coupon["value"] / 100
    elif coupon["type"] == "fixed":
        discount_amount = coupon["value"]
    else:
        discount_amount = 0

    final_price = max(0, cart_total - discount_amount)

    return {
        "valid": True,
        "discount_amount": int(discount_amount),
        "final_price": int(final_price),
        "message": "Áp dụng thành công"
    }
coupon_db = {
"SALE20": {"type": "percent", "value": 20, "min_order":
200000},
"SHIP50K": {"type": "fixed", "value": 50000, "min_order":
150000}
}
print(apply_coupon(cart_total=350000, code="SALE20", coupon_db=coupon_db))

#Bai 43

from fastapi import FastAPI

app = FastAPI()


@app.post("/daily-report")
def daily_report(transactions: list = Body(...)):
    report = {}

    for transaction in transactions:
        date = transaction["date"]
        amount = transaction["amount"]

        if date not in report:
            report[date] = {
                "total": 0,
                "count": 0
            }

        report[date]["total"] += amount
        report[date]["count"] += 1

    for date in report:
        total = report[date]["total"]
        count = report[date]["count"]
        report[date]["avg"] = round(total / count, 2)

    return report

#Bai 44

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    category: str
    rating: float


@app.post("/related-products")
def related_products(
    product_id: int,
    limit: int,
    products: List[Product]
):
    # Tìm sản phẩm hiện tại
    current_product = None
    for product in products:
        if product.id == product_id:
            current_product = product
            break

    # Không tìm thấy product_id
    if current_product is None:
        return []

    # Lọc sản phẩm cùng category, bỏ sản phẩm hiện tại
    related = [
        product
        for product in products
        if product.category == current_product.category
        and product.id != product_id
    ]

    # Sắp xếp rating giảm dần
    related.sort(key=lambda x: x.rating, reverse=True)

    return related[:limit]

#Bài 45

def top_selling(items, top_n):
    products = {}

    for item in items:
        product_id = item["product_id"]

        if product_id not in products:
            products[product_id] = {
                "product_id": product_id,
                "name": item["name"],
                "total_qty": 0,
                "revenue": 0
            }

        products[product_id]["total_qty"] += item["qty"]
        products[product_id]["revenue"] += item["qty"] * item["price"]

    result = list(products.values())

    result.sort(key=lambda x: x["total_qty"], reverse=True)

    return result[:top_n]


items = [
    {"product_id": 1, "name": "Áo", "qty": 5, "price": 120000},
    {"product_id": 2, "name": "Quần", "qty": 3, "price": 350000},
    {"product_id": 1, "name": "Áo", "qty": 8, "price": 120000}
]

print(top_selling(items, 2))

#Bai 46
def detect_anomalies(orders, threshold):
    if not orders:
        return []

    avg = sum(order["total"] for order in orders) / len(orders)

    batthuong = []

    for order in orders:
        if order["total"] > threshold * avg:
            batthuong.append(order)

    return batthuong

orders = [
    {"id": 101, "total": 250000},
    {"id": 102, "total": 180000},
    {"id": 103, "total": 920000},
    {"id": 104, "total": 210000}
]

print(detect_anomalies(orders, 2.0))

#Bai 47

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AccessRequest(BaseModel):
    role: str
    resource: str
    action: str
    rbac: dict


@app.post("/can-access")
def can_access(data: AccessRequest):
    if data.role not in data.rbac:
        return {"can_access": False}

    if data.resource not in data.rbac[data.role]:
        return {"can_access": False}

    return {
        "can_access": data.action in data.rbac[data.role][data.resource]
    }
#Bai 48

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class SaleData(BaseModel):
    old_sale: List[str]
    new_sale: List[str]


@app.post("/sale-diff")
def sale_diff(data: SaleData):
    old_set = set(data.old_sale)
    new_set = set(data.new_sale)

    return {
        "removed": list(old_set - new_set),
        "added": list(new_set - old_set),
        "kept": list(old_set & new_set)
    }

#Bai 49

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()


class OrderCounts(BaseModel):
    order_counts: Dict[str, int]


@app.post("/segment-users")
def segment_users(data: OrderCounts):
    one_time = set()
    repeat = set()
    vip = set()

    for user_id, count in data.order_counts.items():
        if count == 1:
            one_time.add(user_id)
        elif 2 <= count <= 4:
            repeat.add(user_id)
        else:  # count >= 5
            vip.add(user_id)

    return {
        "one_time": list(one_time),
        "repeat": list(repeat),
        "vip": list(vip)
    }

#Bai 50

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()


class ConflictRequest(BaseModel):
    flash_sale_items: List[str]
    active_campaigns: Dict[str, List[str]]


@app.post("/check-conflicts")
def check_conflicts(data: ConflictRequest):
    conflicts = {}
    safe_items = set()

    for product_id in data.flash_sale_items:
        campaigns = []

        for campaign_name, products in data.active_campaigns.items():
            if product_id in products:
                campaigns.append(campaign_name)

        if campaigns:
            conflicts[product_id] = campaigns
        else:
            safe_items.add(product_id)

    return {
        "has_conflict": len(conflicts) > 0,
        "conflicts": conflicts,
        "safe_items": list(safe_items)
    }