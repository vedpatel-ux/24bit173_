prices = {
    "mango": 6,
    "apple": 30,
    "chai": 60,
    "tomato": 40,
    "coffee": 5
}
quantity = {
    "mango": 2,
    "apple": 5,
    "chai": 1,
    "tomato": 2,
    "coffee": 12
}
total_bill = 0

for item in quantity:
    if item in prices:
        total_bill += prices[item] * quantity[item]

print("Total Bill Amount: ₹", total_bill)