bill_thickness = 0.11 * 0.001  # Meters (0.11)
sears_height = 442  # Height in meters
num_bills = 1
days = 1

while num_bills * bill_thickness < sears_height:
    print(days, num_bills, num_bills * bill_thickness)
    days += 1
    num_bills *= 2

print('Number of days: ', days)
print('Number of bills: ', num_bills)
print('Final Height: ', num_bills * bill_thickness)
