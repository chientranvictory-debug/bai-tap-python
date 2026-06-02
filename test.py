from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model for cart item
class CartItem(BaseModel):
    name: str
    price: float
    quantity: int

# Function to calculate cart total
def cart_total(cart: List[dict]) -> float:
    """
    Tính tổng tiền giỏ hàng
    Args:
        cart: Danh sách các mặt hàng với price và quantity
    Returns:
        Tổng tiền của giỏ hàng
    """
    total = sum(item["price"] * item["quantity"] for item in cart)
    return total

# API endpoint
@app.post("/cart/total")
async def calculate_cart_total(items: List[CartItem]):
    """
    API endpoint để tính tổng tiền giỏ hàng
    """
    # Convert Pydantic models to dictionaries
    cart = [item.dict() for item in items]
    total = cart_total(cart)
    return {
        "total": total,
        "items": items,
        "message": f"Tổng tiền giỏ hàng: {total:,.0f} VND"
    }

# Test function
if __name__ == "__main__":
    # Sample test data
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


#run server: uvicorn test:app --reload



    
    


