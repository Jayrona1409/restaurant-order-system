
name = input("Customer name: ")
student_id = input("Do you have a student ID? (yes/no): ")
order_time = int(input("Order time (0-23): "))

# Dish 1
dish1 = input("Dish 1 name: ")
price1 = float(input("Dish 1 price: "))
qty1 = int(input("Dish 1 quantity: "))

# Dish 2
dish2 = input("Dish 2 name: ")
price2 = float(input("Dish 2 price: "))
qty2 = int(input("Dish 2 quantity: "))

# Dish 3
dish3 = input("Dish 3 name: ")
price3 = float(input("Dish 3 price: "))
qty3 = int(input("Dish 3 quantity: "))

# Calculate subtotal
subtotal = price1 * qty1 + price2 * qty2 + price3 * qty3

# Student discount
student_discount = 0
if student_id == "yes":
    student_discount = subtotal * 0.15

# Happy hour discount
happy_discount = 0
if order_time >= 14 and order_time <= 17:
    happy_discount = subtotal * 0.20

# Choose the better main discount
if student_discount >= happy_discount:
    main_discount = student_discount
    main_name = "Student discount"
else:
    main_discount = happy_discount
    main_name = "Happy hour discount"

# Large order discount
large_discount = 0
if subtotal >= 150000:
    large_discount = subtotal * 0.05

# Total discounts
total_discount = main_discount + large_discount

# Subtotal after discounts
after_discount = subtotal - total_discount

# Service charge
service_charge = after_discount * 0.10

# Delivery fee
delivery = 15000
if subtotal >= 100000:
    delivery = 0

# Final total
final_total = after_discount + service_charge + delivery

# Total amount saved
saved = total_discount + (subtotal - total_discount) * 0.10
if delivery == 0:
    saved = saved + 15000

# Output
print("\n===== RESTAURANT BILL =====")
print("Customer:", name)
print("Student ID:", student_id)
print("Order time:", order_time)

print("\n--- Orders ---")
print(dish1, price1, "x", qty1, "=", price1 * qty1)
print(dish2, price2, "x", qty2, "=", price2 * qty2)
print(dish3, price3, "x", qty3, "=", price3 * qty3)

print("\nSubtotal:", subtotal)

print("\nStudent discount eligible:", student_id == "yes")
print("Student discount amount:", student_discount)

print("Happy hour eligible:", order_time >= 14 and order_time <= 17)
print("Happy hour discount amount:", happy_discount)

print("Applied main discount:", main_name)
print("Large order discount eligible:", subtotal >= 150000)
print("Large order discount amount:", large_discount)

print("Total discounts:", total_discount)
print("Subtotal after discounts:", after_discount)
print("Service charge:", service_charge)

print("Free delivery:", delivery == 0)
print("Delivery fee:", delivery)

print("Final total:", final_total)
print("Total amount saved:", saved)
