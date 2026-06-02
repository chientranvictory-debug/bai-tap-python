# Bài 1

from inspect import stack


class BrowserHistory:
    def __init__(self, homepage: str):
        self.back_stack = []       # lưu lịch sử quay lại
        self.forward_stack = []    # lưu lịch sử tiến tới
        self.current = homepage    # trang hiện tại

    def visit(self, url: str) -> None:
        # khi vào trang mới: xóa forward
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()

    def back(self, steps: int) -> str:
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            steps -= 1
        return self.current

    def forward(self, steps: int) -> str:
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            steps -= 1
        return self.current

    
h = BrowserHistory("trang-chu")  
h.visit("san-pham/ao-thun")
h.visit("san-pham/quan-jean")
h.visit("gio-hang")

print(h.back(1))
print(h.back(1))
print(h.forward(1))
print(h.back(3))

# Bài 2

def is_valid_brackets(s):
    stack = []

    pairs = { ')': '(', ']': '[','}': '{' }


    for char in s:
      if char in "([{":
        stack.append(char)
      elif char in ")]}":
        if not stack or stack[-1] != pairs[char]:
         return False
        stack.pop()

    # Nếu còn ngoặc mở chưa đóng -> False
    return len(stack) == 0

# Test
print(is_valid_brackets('{"name": "An", "items": [1, 2]}'))
print(is_valid_brackets('{"data": [{"id": 1}'))
print(is_valid_brackets('(())'))
print(is_valid_brackets('{"data": [{"id": 1]}'))

# Bài 3

from collections import defaultdict

def validate_transaction_order(events):
    txns = defaultdict(list)

   
    for e in events:
        txns[e["txn_id"]].append(e["event"])

    errors = []
    completed = 0
    valid = True

    for txn_id, evs in txns.items():
       
        if not evs or evs[0] != "INIT":
            errors.append(f"{txn_id}: thieu INIT")
            valid = False
            continue

       
        if "PROCESSING" not in evs:
            errors.append(f"{txn_id}: thieu buoc PROCESSING")
            valid = False
            continue

        
        last_event = evs[-1]
        if last_event not in ("COMPLETED", "FAILED"):
            errors.append(f"{txn_id}: thieu trang thai ket thuc")
            valid = False
            continue

       
        if last_event == "COMPLETED":
            completed += 1

    return {
        "valid": valid,
        "completed": completed,
        "errors": errors
    }

events1 = [
{"txn_id": "T1", "event": "INIT"},
{"txn_id": "T2", "event": "INIT"},
{"txn_id": "T2", "event": "PROCESSING"},
{"txn_id": "T2", "event": "COMPLETED"},
{"txn_id": "T1", "event": "PROCESSING"},
{"txn_id": "T1", "event": "FAILED"},
]
events2 = [
{"txn_id": "T3", "event": "INIT"},
{"txn_id": "T3", "event": "COMPLETED"},
]

print(validate_transaction_order(events1))
print(validate_transaction_order(events2))

# Bài 4

import heapq


class PriorityShippingQueue:
    def __init__(self):
        
        self.heap = []

        
        self.order = 0

        
        self.priority_map = {
            "express": 1,
            "vip": 2,
            "normal": 3
        }

    def enqueue(self, shipment):
       
        priority = self.priority_map[shipment["type"]]

        
        heapq.heappush(
            self.heap,
            (priority, self.order, shipment)
        )

        
        self.order += 1

    def dequeue(self):
        
        if self.heap:
            return heapq.heappop(self.heap)[2]
        return None
    
psq = PriorityShippingQueue()

psq.enqueue({"id": "S1", "type": "normal", "dest": "HN"})
psq.enqueue({"id": "S2", "type": "express", "dest": "HCM"})
psq.enqueue({"id": "S3", "type": "vip", "dest": "DN"})
psq.enqueue({"id": "S4", "type": "express", "dest": "HN"})

print(psq.dequeue())
print(psq.dequeue())
print(psq.dequeue())

#Bai 5
def simulate_checkout(customers, n_counters):
    # Khởi tạo các quầy
    counters = {
        f"counter_{i+1}": {
            "customers": [],
            "total_items": 0
        }
        for i in range(n_counters)
    }

    # Phân khách vào quầy có ít total_items nhất
    for customer in customers:
        # Tìm quầy ít hàng nhất
        min_counter = min(
            counters,
            key=lambda c: counters[c]["total_items"]
        )

        # Thêm khách vào quầy
        counters[min_counter]["customers"].append(customer["id"])
        counters[min_counter]["total_items"] += customer["items"]

    return counters
customers = [
    {"id": "C1", "items": 5},
    {"id": "C2", "items": 12},
    {"id": "C3", "items": 3},
    {"id": "C4", "items": 8},
    {"id": "C5", "items": 1},
]

result = simulate_checkout(customers, n_counters=2)

print(result)    #khách mới → vào quầy có total_items nhỏ nhất ở thời điểm hiện tại


#Bai 6 Graph và Tree khác nhau như thế nào? Khi nào dùng Graph, khi nào dùng Tree?

# Graph và Tree đều là cấu trúc dữ liệu dùng để biểu diễn mối quan hệ giữa các phần tử,
# nhưng Tree là một trường hợp đặc biệt của Graph.

# # Tree                            Có cấp bậc
#                                   1 root
#                                   Không loop                    
#       A
#      / \
#     B   C


# Graph
# Quan hệ tự do
# Có thể loop
# Có nhiều đường đi                   
# A ---- B
# |    / |
# |   /  |
# C ---- D

# Khi nào dùng Graph: Dùng khi quan hệ giữa các đối tượng là mạng lưới phức tạp
# Khi nào dùng Tree: Dùng khi quan hệ giữa các đối tượng có cấu trúc phân cấp rõ ràng

#Bai 7
# Giải thích khái niệm và so sánh DFS và BFS. Hãy suy nghĩ và đưa ra một ví dụ trong hệ
# thống thương mại điện tử trường hợp nào dùng DFS, trường hợp nào là BFS?

    # DFS = Tìm kiếm theo chiều sâu
    # BFS = Tìm kiếm theo chiều rộng

# So sánh DFS vs BFS

# Đặc điểm             DFS                     BFS
# # Cấu trúc dữ liệu   Stack                   Queue
# Cách duyệt           Đi sâu trước            Duyệt từng tầng
# Bộ nhớ               Thấp hơn (O(h))         Cao hơn (O(w))
# Tốc độ tìm sâu       Nhanh hơn               Chậm hơn nếu giải pháp gần gốc
# Tìm gần nhất         Không tốt               Rất tốt

# Ví dụ trong hệ thống thương mại điện tử
# Trường hợp dùng DFS Xuất toàn bộ category con của “Electronics”

         # Electronics
         #  ├── Laptop
         #  │    ├── Gaming
         #  │    └── Office
         #  └── Phone

# Trường hợp dùng BFS Hiển thị sản phẩm liên quan gần nhất cho user

         # Laptop A
         #  ├── Laptop B
         #  ├── Laptop C
         #  └── Laptop D



#Bai 8  

# Binary Search Tree (BST) là gì?

# Binary Search Tree là cây nhị phân có quy tắc:

# Node bên trái nhỏ hơn node cha
# Node bên phải lớn hơn node cha
# Node không có con gọi là leaf node (node lá)         

# Ví dụ BST: bst_search(value)

#         8
#       /   \
#      3     10
#     / \      \
#    1   6      14
#       / \     /
#      4   7   13

# Leaf node ở đây là: 1, 4, 7, 13

# Cách tìm kiếm trong BST
     # Nếu giá trị cần tìm nhỏ hơn node hiện tại → đi sang trái
     # Nếu lớn hơn → đi sang phải
     # Nếu bằng → tìm thấy

      #  Ví dụ tìm giá trị 7
# Bước 1

# Đang ở node gốc 8

# 7 < 8
# → đi sang trái
# Bước 2

# Đến node 3

# 7 > 3
# → đi sang phải
# Bước 3

# Đến node 6

# 7 > 6
# → đi sang phải
# Bước 4

# Đến node 7

# 7 == 7
# → tìm thấy value đến đây giả sử không có 7 thì trả về none


# Minh họa bst_insert(value)

# Cây ban đầu:

#           8
#         /   \
#        3     10
#       / \
#      1   6
#         / \
#        4   7
# Thêm giá trị 5
# Bước 1
# 5 < 8
# → đi trái
# Bước 2
# 5 > 3
# → đi phải
# Bước 3
# 5 < 6
# → đi trái
# Bước 4
# 5 > 4
# → đi phải
# Bước 5

# Bên phải node 4 đang trống (None)

# → chèn 5 vào đây
# Cây sau khi insert
#           8
#         /   \
#        3     10
#       / \
#      1   6
#         / \
#        4   7
#         \
#          5

#Bai 9

# Nên chọn Adjacency List thay vì Adjacency Matrix.
# Hệ thống có:

# 10,000 kho → tức 10,000 node
# Mỗi kho chỉ kết nối trung bình 5 kho khác
# Điều này có nghĩa số cạnh rất ít so với số cạnh tối đa có thể có ⇒ đây là graph thưa
# Nếu dùng Adjacency List
# Mỗi node chỉ lưu các hàng xóm thực sự kết nối.

# Vì mỗi kho trung bình chỉ có ~5 cạnh:

# 10,000×5=50,000

# Chỉ cần lưu khoảng 50,000 kết nối thay vì 100 triệu ô.


# Adjacency Matrix cần ma trận:

# N×N=10,000×10,000

# 10,000×10,000=100,000,000

# Tức cần:

# 100 triệu ô nhớ
# Dù nhiều ô sẽ là 0 vì các kho không kết nối với nhau

#Bai 10
# Đề bài: Làm sao để kiểm tra một đồ thị có chu trình hay không?
# Ý tưởng DFS:

# Khi đi từ node A sang B:

# Nếu B đã visited
# và B không phải là cha (parent) của A 
# # → thì có chu trình
# cần lưu:  visited[] và parent[] cần parent? Vì trong đồ thị vô hướng: A đi B, 
# rồi B quay lại A là bình thường → KHÔNG phải cycle

# Ví dụ:

# 1 -- 2
# |    |
# 4 -- 3
# DFS:

# 1 → 2 → 3 → 4
# Tại 4, thấy 1:

# 1 đã visited
# 1 không phải parent của 4 ⇒ Có chu trình:

# Đồ thị có hướng
# Chỉ visited là không đủ.
# Cần lưu thêm: visited = set()
#                rec_stack = set()   # stack DFS hiện tại

# Khi vào một node → đưa vào rec_stack
# Khi DFS xong node đó → loại khỏi rec_stack

#    1 → 2 → 3

#    1 → 4

# Bước 3 Đi sang 3  rec_stack = {1, 2, 3}  3 không còn node  nào sau nó
# DFS của 3 kết thúc. lúc này phải bỏ 3 ra: rec_stack = {1, 2}
# DFS của 2 kết thúc. Bỏ 2 ra: rec_stack = {1}
# Sau đó DFS từ 1 sang 4 rec_stack = {1, 4} Nếu không loại khỏi rec_stack, ta sẽ có
# rec_stack = {1, 2, 3, 4} Khi đó các node 2, 3 vẫn bị coi là đang nằm trên đường DFS hiện tại
# dù thực tế DFS đã rời khỏi chúng từ lâu. Điều này có thể gây báo sai chu trình.


# Ví dụ:

# 1 → 2 → 3

# 1 → 4 → 3

# Đồ thị này không có chu trình. Nhưng nếu 3 không bị xóa khỏi rec_stack:
# DFS xong nhánh 1→2→3
# Sang nhánh 1→4
# Từ 4 gặp 3
# Thấy 3 vẫn trong rec_stack
# Kết luận nhầm là có cycle

# Nếu gặp một node đã nằm trong rec_stack
# ⇒ quay lại chính đường đang đi
# ⇒ có chu trình