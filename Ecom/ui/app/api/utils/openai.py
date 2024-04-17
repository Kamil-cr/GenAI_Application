from openai import OpenAI
from api.utils.settings import OPENAI_API_KEY, TOKEN
client = OpenAI(api_key=OPENAI_API_KEY)
import requests
import json

TOKEN =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrYW1pbCIsImV4cCI6MTcxMzc4MzE4M30.ODEwzOsip8f85lb4p7m67LGFUctnqqmfgy2EZn1RgiA"

def get_order():
    url = "http://localhost:3000/api/orders"
    response = requests.get(url, headers={f"Authorization": f"Bearer {TOKEN}"})
    return json.dumps(response.json())

def get_products():
    url = "http://localhost:3000/api/products"
    response = requests.get(url)
    return json.dumps(response.json())

def post_cart(product_id, quantity, size):
    url = "http://localhost:3000/api/cart"
    response = requests.post(url,json={"product_id": product_id, "qauntity": quantity, "size": size}, headers={f"Authorization": f"Bearer {TOKEN}"})
    return json.dumps(response.json())

def update_cart(product_id, quantity, size):
    url = "http://localhost:3000/api/cart"
    response = requests.patch(url,json={"product_id": product_id, "qauntity": quantity, "size": size}, headers={f"Authorization": f"Bearer {TOKEN}"})
    return json.dumps(response.json())
    
def delete_cart(product_id, quantity, size):    
    url = "http://localhost:3000/api/cart"
    response = requests.delete(url,json={"product_id": product_id, "qauntity": quantity, "size": size}, headers={f"Authorization": f"Bearer {TOKEN}"})
    return json.dumps(response.json())

def post_order(payment_method, first_name, last_name, address, city, state, contact_number):
    url = "http://localhost:3000/api/order"
    response = requests.post(url,json={"payment_method": payment_method, "first_name": first_name, "last_name": last_name, "address": address, "city": city, "state": state, "contact_number": contact_number}, headers={f"Authorization": f"Bearer {TOKEN}"})
    return json.dumps(response.json())

def update_order(payment_method, first_name, last_name, address, city, state, contact_number, order_id, order_status):
    url = "http://localhost:3000/api/order"
    response = requests.patch(url,json={"order_id": order_id, "order_status": order_status,"payment_method": payment_method, "first_name": first_name, "last_name": last_name, "address": address, "city": city, "state": state, "contact_number": contact_number}, headers={f"Authorization": f"Bearer {TOKEN}"})
    return json.dumps(response.json())

def cancel_order(order_id, order_status):
    url = "http://localhost:3000/api/order"
    response = requests.delete(url,json={"order_id": order_id, "order_status": order_status}, headers={f"Authorization": f"Bearer {TOKEN}"})
    return json.dumps(response.json())

available_functions = {
    "get_order": get_order,
    "get_products": get_products,
    "post_cart": post_cart,
    "update_cart": update_cart,
    "delete_cart": delete_cart,
    "post_order": post_order,
    "update_order": update_order,
    "cancel_order": cancel_order
}

filepath = "./StyleHub.pdf"
file_object = client.files.create(filepath=open(filepath, "rb"), purpose="assistants")

assistant = client.beta.assistants.create(
    name="StyleHub",
    file=file_object.id,
    model="gpt-3.5-turbo",
    instructions="",
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_order",
                "description": "Get all orders of the user",
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_products",
                "description": "Get all products",
            },
        },
        {
            "type": "function",
            "function": {
                "name": "post_cart",
                "description": "Add a product to the cart with the specified quantity and size",
            },
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "string",
                        "description": "The id of the product to add to the cart. Product id can be get from get_products function.",
                    },
                    "quantity": {
                        "type": "number",
                        "description": "The quantity of the product to add to the cart",
                    },
                    "size": {
                        "type": "string",
                        "description": "The size of the product to add to the cart. Available sizes are 'S', 'M', 'L', 'XL'",
                    },
                },
                "required": ["product_id", "quantity", "size"],
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_cart",
                "description": "Update the quantity of a product in the cart with the specified size",
            },
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "string",
                        "description": "The id of the product to update in the cart. Product id can be get from get_products function.",
                    },
                    "quantity": {
                        "type": "number",
                        "description": "The new quantity of the product in the cart to update",
                    },
                    "size": {
                        "type": "string",
                        "description": "The size of the product in the cart to update. Available sizes are 'S', 'M', 'L', 'XL'",
                    },
                },
                "required": ["product_id", "quantity", "size"],
            }
        },
        {
            "type": "function",
            "function": {
                "name": "delete_cart",
                "description": "Delete a product from the cart",
            },
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "string",
                        "description": "The id of the product to delete from the cart Product id can be get from get_products function.",
                    },
                    "quantity": {
                        "type": "number",
                        "description": "The quantity of the product to delete from the cart. If the quantity is not specified, the entire product will be removed from the cart.",
                    },
                    "size": {
                        "type": "string",
                        "description": "The size of the product to delete from the cart. If the size is same as the product in the cart, the entire product will be removed from the cart. Available sizes are 'S', 'M', 'L', 'XL'",
                    },
                },
                "required": ["product_id", "quantity", "size"],
            }
        },
        {
            "type": "function",
            "function": {
                "name": "post_order",
                "description": "Create an order with the specified details",
            },
            "parameters": {
                "type": "object",
                "properties": {
                    "payment_method": {
                        "type": "string",
                        "description": "The payment method for the order (card or cash)",
                    },
                    "first_name": {
                        "type": "string",
                        "description": "The first name of the customer ",
                    },
                    "last_name": {
                        "type": "string",
                        "description": "The last name of the customer",
                    },
                    "address": {
                        "type": "string",
                        "description": "The address of the customer",
                    },
                    "city": {
                        "type": "string",
                        "description": "The city of the customer",
                    },
                    "state": {
                        "type": "string",
                        "description": "The state of the customer",
                    },
                    "contact_number": {
                        "type": "string",
                        "description": "The contact number of the customer",
                    },
                },
                "required": ["payment_method", "first_name", "last_name", "address", "city", "state", "contact_number"],
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_order",
                "description": "Update an order with the specified details",
            },
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "number",
                        "description": "The id of the order to update. Order id can be get from get_order function.",
                    },
                    "order_status": {
                        "type": "string",
                        "description": "The status of the order to update, must be 'pending', 'confirmed', 'shipped', 'delivered' or 'cancelled'",
                    },
                    "payment_method": {
                        "type": "string",
                        "description": "The payment method for the order",
                    },
                    "first_name": {
                        "type": "string",
                        "description": "The first name of the customer",
                    },
                    "last_name": {
                        "type": "string",
                        "description": "The last name of the customer",
                    },
                    "address": {
                        "type": "string",
                        "description": "The address of the customer",
                    },
                    "city": {
                        "type": "string",
                        "description": "The city of the customer",
                    },
                    "state": {
                        "type": "string",
                        "description": "The state of the customer",
                    },
                    "contact_number": {
                        "type": "string",
                        "description": "The contact number of the customer",
                    },
                },
                "required": ["payment_method", "first_name", "last_name", "address", "city", "state", "contact_number"],
            }
        },
        {
            "type": "function",
            "function": {
                "name": "cancel_order",
                "description": "Cancel an order",
            },
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "number",
                        "description": "The id of the order to cancel. Order id can be get from get_order function.",
                    },
                    "order_status": {
                        "type": "string",
                        "description": "The status of the order to cancel, must be 'cancelled'",
                    },
                },
                "required": ["order_id", "order_status"],
            }
        },
    ]
)

# def generate_message(prompt: str) -> str:
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response.choices[0].message.content