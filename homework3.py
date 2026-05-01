from unittest import result


def filter_available(products):
    result = []
    
    for product in products:
        if product["stock"] > 0 and product["is_active"] == True:
            result.append(product)
    
    return result
                                 #áp dụng ví dụ
products = [
    {"id": 1, "name": "Áo thun", "stock": 10, "is_active": True},
    {"id": 2, "name": "Quần jean", "stock": 0, "is_active": True},
    {"id": 3, "name": "Giày sneaker", "stock": 5, "is_active": False},
    {"id": 4, "name": "Nón baseball", "stock": 3, "is_active": True},
]
print(filter_available(products))

#bai2

def cart_total(cart, discount=10):
    total = 0
    
    for item in cart:
        total += item["price"] * item["quantity"]
    
    # áp dụng giảm giá
    total = total * (1 - discount / 100)
    
    return total
                                     #áp dụng ví dụ
cart = [{"name": "Áo thun", "price": 120000, "quantity": 2},
{"name": "Quần dài", "price": 350000, "quantity": 1},
{"name": "Tất", "price": 25000, "quantity": 3},]                                     
cart_total(cart, discount=10) # giảm 10%

print(cart_total(cart))

#bai3

def related_products(product_id, products, limit=3):
    # 1. tìm category của product_id
    category = None
    for p in products:
        if p["id"] == product_id:
            category = p["category"]
            break
        # 2. lọc sản phẩm cùng category, trừ chính nó
    filtered = []
    for p in products:
        if p["category"] == category and p["id"] != product_id:
            filtered.append(p)

    # 3. sắp xếp theo rating giảm dần
    filtered.sort(key=lambda x: x["rating"], reverse=True)

    # 4. lấy limit
    return filtered[:limit]
                                        #áp dụng ví dụ
products = [
{"id": 1, "name": "Áo polo", "category": "ao", "rating": 4.5},
{"id": 2, "name": "Áo thun", "category": "ao", "rating": 4.8},
{"id": 3, "name": "Áo khoác", "category": "ao", "rating": 4.2},
{"id": 4, "name": "Quần jeans","category": "quan","rating": 4.7},
{"id": 5, "name": "Áo sơ mi", "category": "ao", "rating": 4.6},]
print(related_products(product_id=1, products=products, limit=3))  

#bai4
def detect_anomalies(orders, threshold=2.5):
    # 1. tính trung bình
    total_sum = 0
    for order in orders:
        total_sum += order["total"]
    
    avg = total_sum / len(orders)
    
    # 2. lọc đơn bất thường
    result = []
    for order in orders:
        if order["total"] > threshold * avg:
            result.append(order)
    
    return result
                                        #áp dụng ví dụ          
orders = [{"id": 101, "total": 250000},
{"id": 102, "total": 180000},
{"id": 103, "total": 920000},
{"id": 104, "total": 210000},
{"id": 105, "total": 195000},
]
print(detect_anomalies(orders, threshold=2.5))         


 #bai 5

def top_selling(items, top_n=2):
    summary = {}

    for item in items:
        pid = item["product_id"]

        if pid not in summary:
            summary[pid] = {
                "product_id": pid,
                "name": item["name"],
                "total_qty": 0,
                "revenue": 0
            }

        summary[pid]["total_qty"] += item["qty"]
        summary[pid]["revenue"] += item["qty"] * item["price"]

    result = list(summary.values())

    result.sort(key=lambda x: x["total_qty"], reverse=True)

    return result[:top_n]                            
                                        #áp dụng ví dụ  

items = [
{"product_id": 1, "name": "Áo thun", "qty": 5, "price": 120000},
{"product_id": 2, "name": "Quần jean", "qty": 3, "price": 350000},
{"product_id": 1, "name": "Áo thun", "qty": 8, "price": 120000},
{"product_id": 3, "name": "Giày", "qty": 2, "price": 450000},
{"product_id": 2, "name": "Quần jean", "qty": 4, "price": 350000},
]
result = top_selling(items, top_n=2)
print(result)                                

#bai6

def build_catalog(products):
    catalog = {}

    for p in products:
        catalog[p["id"]] = p

    return catalog
catalog = build_catalog(products)
print(catalog)
                   #áp dụng ví dụ
products = [   {"id": "SP001", "name": "Áo thun basic", "price": 120000,
"category": "ao"},
{"id": "SP002", "name": "Quần jogger", "price": 280000,
"category": "quan"},
{"id": "SP003", "name": "Nón bucket", "price": 95000,
"category": "phu_kien"},
]
catalog = build_catalog(products)
print(catalog)       


#bai7

def count_by_status(statuses):
    result = {}

    for s in statuses:
        if s in result:
            result[s] += 1
        else:
            result[s] = 1

    return result

#bai8

def apply_coupon(cart_total, code, coupon_db):
    # 1. kiểm tra tồn tại
    if code not in coupon_db:
        return {
            "valid": False,
            "discount_amount": 0,
            "final_price": cart_total,
            "message": "Mã không tồn tại"
        }

    coupon = coupon_db[code]

    # 2. kiểm tra min_order
    if cart_total < coupon["min_order"]:
        return {
            "valid": False,
            "discount_amount": 0,
            "final_price": cart_total,
            "message": f"Đơn tối thiểu {coupon['min_order']}"
        }

    # 3. tính discount
    if coupon["type"] == "percent":
        discount = cart_total * coupon["value"] // 100
        message = f"Áp dụng thành công {code} (-{coupon['value']}%)"
    else:
        discount = coupon["value"]
        message = f"Áp dụng thành công {code} (-{discount})"

    # 4. tính final
    final_price = cart_total - discount

    # 5. return
    return {
        "valid": True,
        "discount_amount": discount,
        "final_price": final_price,
        "message": message
    }

#áp dụng ví dụ
coupon_db = {
"SALE20": {"type": "percent", "value": 20, "min_order": 200000},
"SHIP50K": {"type": "fixed", "value": 50000, "min_order":
150000},
"VIP30": {"type": "percent", "value": 30, "min_order": 500000},
}
apply_coupon(350000, "SALE20", coupon_db)
print(apply_coupon(350000, "SALE20", coupon_db))

#bai9

def daily_report(transactions):
    result = {}

    for t in transactions:
        date = t["date"]

        if date not in result:
            result[date] = {
                "total": 0,
                "count": 0
            }

        result[date]["total"] += t["amount"]
        result[date]["count"] += 1

    # tính avg
    for date in result:
        total = result[date]["total"]
        count = result[date]["count"]
        result[date]["avg"] = round(total / count, 2)

    return result
#áp dụng ví dụ
transactions = [
{"date": "2024-01-15", "amount": 320000},
{"date": "2024-01-15", "amount": 185000},
{"date": "2024-01-16", "amount": 450000},
{"date": "2024-01-15", "amount": 270000},
{"date": "2024-01-16", "amount": 390000},
]
print(daily_report(transactions))

#bai10

import time

class SessionStore:
    def __init__(self, timeout=1800):
        self.sessions = {}   # nơi lưu session
        self.timeout = timeout

    def create(self, user_id, data):
        now = int(time.time())
        self.sessions[user_id] = {
            "user_id": user_id,
            "data": data,
            "created_at": now,
            "expires_at": now + self.timeout
        }

    def get(self, user_id):
        session = self.sessions.get(user_id)

        # không tồn tại
        if not session:
            return None

        now = int(time.time())

        # hết hạn
        if now > session["expires_at"]:
            del self.sessions[user_id]
            return None

        return session

    def delete(self, user_id):
        if user_id in self.sessions:
            del self.sessions[user_id]


                 #áp dụng ví dụ
store = SessionStore(timeout=1800) # 30 phút
store.create("user_123", {"name": "An", "role": "customer"})
session = store.get("user_123")
print(session)
store.delete("user_123")
print(store.get("user_123"))

#bai11

# Bảng phân quyền
rbac = {
    "admin": {
        "products": ["read", "create", "update", "delete"],
        "orders": ["read", "update", "delete"]
    },
    "seller": {
        "products": ["read", "create", "update"],
        "orders": ["read"]
    },
    "customer": {
        "orders": ["read", "create"]
    },
}

# Hàm kiểm tra quyền
def can_access(role, resource, action, rbac):
    # 1. kiểm tra role có tồn tại không
    if role not in rbac:
        return False

    # 2. kiểm tra resource có trong role không
    if resource not in rbac[role]:
        return False

    # 3. kiểm tra action có được phép không
    if action in rbac[role][resource]:
        return True

    return False

#áp dụng ví dụ

rbac = {
"admin": {"products": ["read","create","update","delete"],
"orders": ["read","update","delete"]},
"seller": {"products": ["read","create","update"],
"orders": ["read"]},
"customer": {"orders": ["read","create"]},}
can_access("seller", "products", "delete", rbac) # False
can_access("admin", "orders", "delete", rbac) # True
can_access("customer", "products", "read", rbac) # False

#bai12

def calc_shipping(city, weight_kg, order_total, zones):
    # 1. lấy zone (nếu không có thì dùng "other")
    zone = zones.get(city, zones["other"])

    zone_rate = zone["zone_rate"]
    free_threshold = zone["free_threshold"]
    min_fee = zone["min_fee"]

    # 2. kiểm tra miễn phí ship
    if order_total >= free_threshold:
        return {
            "fee": 0,
            "free_shipping": True,
            "message": f"Miễn phí vận chuyển đến {city}"
        }

    # 3. tính phí theo cân nặng
    fee = weight_kg * zone_rate

    # 4. đảm bảo không thấp hơn min_fee
    if fee < min_fee:
        fee = min_fee

    # 5. format tiền
    fee = int(fee)

    return {
        "fee": fee,
        "free_shipping": False,
        "message": f"Phí ship đến {city}: {fee:,}đ"
    }


# áp dụng ví dụ

shipping_zones = {
    "HN": {"zone_rate": 15000, "free_threshold": 300000, "min_fee": 15000},
    "HCM": {"zone_rate": 15000, "free_threshold": 300000, "min_fee": 15000},
    "DN": {"zone_rate": 20000, "free_threshold": 350000, "min_fee": 20000},
    "other": {"zone_rate": 30000, "free_threshold": 500000, "min_fee": 30000},
}

result = calc_shipping(city="DN", weight_kg=1.5, order_total=200000, zones=shipping_zones)
print(result)

#bai13

def is_wishlisted(product_id, wishlist):
    return product_id in wishlist


# ===== Dữ liệu =====
wishlist = {"SP001", "SP005", "SP012", "SP018", "SP024"}
# ===== Áp dụng =====
print(is_wishlisted("SP005", wishlist))  
print(is_wishlisted("SP999", wishlist))  

#bai14

def get_unviewed(all_products, viewed_products):
    return all_products - viewed_products


# ===== Dữ liệu =====
all_products = {"SP001","SP002","SP003","SP004","SP005","SP006"}
viewed_products = {"SP001","SP003","SP005"}

#===== Áp dụng =====
print(get_unviewed(all_products, viewed_products))

#bai15

def unique_categories(products):
    categories = set()

    for p in products:
        categories.add(p["category"])

    return categories
# ===== Dữ liệu =====
products = [
{"name": "Áo thun", "category": "ao"},
{"name": "Quần jean", "category": "quan"},
{"name": "Áo khoác", "category": "ao"},
{"name": "Giày", "category": "giay"},
{"name": "Áo polo", "category": "ao"},
]
# ===== Áp dụng =====
print(unique_categories(products))

#bai16

def cross_sell(product_id, order_history, current_cart):
    recommendations = set()

    for order in order_history:
        items = order["items"]

        # nếu đơn hàng có product_id
        if product_id in items:
            for item in items:
                # loại chính nó
                if item != product_id:
                    recommendations.add(item)

    # loại các sản phẩm đã có trong giỏ
    recommendations -= current_cart

    return recommendations

# ===== Dữ liệu =====
order_history = [
{"items": ["SP001","SP002","SP005"]},
{"items": ["SP001","SP003"]},
{"items": ["SP001","SP002","SP004"]},
{"items": ["SP006","SP002"]},
]
current_cart = {"SP001", "SP003"}

#bai17

def sale_diff(old_sale, new_sale):
    removed = old_sale - new_sale   
    added = new_sale - old_sale     
    kept = old_sale & new_sale      

    return {
        "removed": removed,
        "added": added,
        "kept": kept
    }
# ===== Dữ liệu =====
old_sale = {"SP001","SP002","SP003","SP004","SP005"}
new_sale = {"SP002","SP004","SP005","SP006","SP007"}
sale_diff(old_sale, new_sale)

print(sale_diff(old_sale, new_sale))

#bai18

def filter_verified_reviews(reviews, verified_buyers):
    result = []

    for review in reviews:
        user_id = review["user_id"]

        if user_id in verified_buyers:
            result.append(review)

    return result
# ===== Dữ liệu =====
verified_buyers = {"U001", "U003", "U005", "U007"}
reviews = [
{"user_id": "U001", "rating": 5, "comment": "Rất tốt!"},
{"user_id": "U002", "rating": 1, "comment": "Kém chất lượng"},
{"user_id": "U003", "rating": 4, "comment": "Ưng ý"},
{"user_id": "U004", "rating": 5, "comment": "Tuyệt vời"},
]
print(filter_verified_reviews(reviews, verified_buyers))

#bai19

def segment_users(order_counts):
    result = {
        "one_time": set(),
        "repeat": set(),
        "vip": set()
    }

    for user_id, count in order_counts.items():
        if count == 1:
            result["one_time"].add(user_id)
        elif 2 <= count <= 4:
            result["repeat"].add(user_id)
        else:
            result["vip"].add(user_id)

    return result
# ===== Dữ liệu =====
order_counts = {
    "U001": 1, "U002": 7, "U003": 3, "U004": 1,
    "U005": 5, "U006": 2, "U007": 9, "U008": 4,
}
print(segment_users(order_counts))

#bai20

def check_conflicts(flash_sale_items, active_campaigns):
    conflicts = {}
    safe_items = set()

    for item in flash_sale_items:
        conflict_campaigns = []

        for campaign_name, products in active_campaigns.items():
            if item in products:
                conflict_campaigns.append(campaign_name)

        if conflict_campaigns:
            conflicts[item] = conflict_campaigns
        else:
            safe_items.add(item)

    return {
        "has_conflict": len(conflicts) > 0,
        "conflicts": conflicts,
        "safe_items": safe_items
    }
# ===== Dữ liệu =====
active_campaigns = {
"clearance": {"SP001","SP005","SP009"},
"bundle_deal": {"SP003","SP007","SP011"},
"new_arrival": {"SP013","SP015"},
}
flash_sale_items = {"SP001","SP003","SP007","SP020","SP025"}
print(check_conflicts(flash_sale_items, active_campaigns))