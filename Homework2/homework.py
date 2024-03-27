#1
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
restaurant_menu["Beverages"]={"Wine":6.99,"beer":3.99}
del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)

#2

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}
hotel_rooms["101"].update({"status":"booked"})
hotel_rooms["101"].update({"customer":"Cheryl"})
hotel_rooms["102"].update({"status":"available","customer":''})
print(hotel_rooms)
2.2

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}
mashed=[]
search_product=input("Type in product: ")
for search_products in products:
        print(search_products)
        if search_product ==products[search_products]["name"]:
                mashed.append(products[search_products])
print(mashed)

3
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
def new_ticket():
    ticket_id=input("Please enter ticket id: ")
    customer_name=input("Please enter your name: ")
    service_tickets[ticket_id]={}
    service_tickets[ticket_id]["Customer"]=customer_name
def update_ticket():
    ticket_id=input("Please enter ticket id: ")
    status_update=input("Please enter new status: ")
    service_tickets[ticket_id]["Status"]=status_update

def display_ticket():
        pass
new_ticket()
update_ticket()
print(service_tickets)

#4
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}
import copy
sales_copy= copy.deepcopy(weekly_sales)
sales_copy["Week 2"].update({"Electronics": 1800, "Clothing": 6000, "Groceries":8000})
print(weekly_sales)
print(sales_copy)