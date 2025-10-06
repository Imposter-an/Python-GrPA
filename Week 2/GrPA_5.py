main_dish = input()
time_of_day = int(input())
has_voucher = input() == "True"
is_card_payment = input() == "True"

if main_dish == "paneer tikka":
    cost = 250
elif main_dish == "butter chicken":
    cost = 240
elif main_dish == "masala dosa":
    cost = 200
else: # if main dish is invalid print invalid dish and exit the code.
    print("Invalid main dish")
    exit() 

if time_of_day >= 12 and time_of_day <= 15:
    total_cost = (1 - 0.15) * cost
else:
    total_cost = cost

if has_voucher:
    total_cost *= 0.9  # Apply voucher discount

if is_card_payment:  # service charge for card payments
    service_charge = 0.05 * total_cost
    total_cost += service_charge

print(f"{total_cost:.2f}")
