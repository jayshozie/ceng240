# 0 <= day <= 30
class WeekBill:
    def __init__(self, prc):
        self.consumptions = [0] * 31
        self.price = prc

    def consume(self, day, amnt):
        self.consumptions[day] += amnt

    def bill(self):
        totalcons = sum(self.consumptions)
        weekendcons = 0

        # Calculate weekend consumption (assuming days 5,6,12,13,19,20,26,27 are weekends)
        weekend_days = [5, 6, 12, 13, 19, 20, 26, 27]
        for day in weekend_days:
            if day < len(self.consumptions):
                weekendcons += self.consumptions[day]

        discount = weekendcons * self.price * 0.2
        total = totalcons * self.price - discount

        return {
            'totalcons': totalcons,
            'weekendcons': weekendcons,
            'discount': discount,
            'total': total
        }
        # discount = weekendcons * price * 0.2
        # total = totalcons * price - discount
        # Return : {'totalcons': totalcons, 'weekendcons': weekendcons, 'discount': discount, 'total': total}


# Examples are provided by Claude.ai.

# Example 1: Basic usage with consumption on weekdays only
wb1 = WeekBill(10)  # Price per unit is $10
wb1.consume(1, 5)   # 5 units on day 1 (weekday)
wb1.consume(2, 3)   # 3 units on day 2 (weekday)
wb1.consume(3, 2)   # 2 units on day 3 (weekday)
result1 = wb1.bill()
print("Example 1 (Weekdays only):")
print(f"Total consumption: {result1['totalcons']} units")
print(f"Weekend consumption: {result1['weekendcons']} units")
print(f"Discount: ${result1['discount']:.2f}")
print(f"Total bill: ${result1['total']:.2f}")
print()

# Example 2: Usage with consumption on weekend days
wb2 = WeekBill(15)  # Price per unit is $15
wb2.consume(5, 8)   # 8 units on day 5 (weekend)
wb2.consume(6, 7)   # 7 units on day 6 (weekend)
result2 = wb2.bill()
print("Example 2 (Weekend days only):")
print(f"Total consumption: {result2['totalcons']} units")
print(f"Weekend consumption: {result2['weekendcons']} units")
print(f"Discount: ${result2['discount']:.2f}")
print(f"Total bill: ${result2['total']:.2f}")
print()

# Example 3: Mixed weekday and weekend consumption
wb3 = WeekBill(12)  # Price per unit is $12
wb3.consume(4, 10)  # 10 units on day 4 (weekday)
wb3.consume(5, 15)  # 15 units on day 5 (weekend)
wb3.consume(7, 5)   # 5 units on day 7 (weekday)
result3 = wb3.bill()
print("Example 3 (Mixed weekday and weekend):")
print(f"Total consumption: {result3['totalcons']} units")
print(f"Weekend consumption: {result3['weekendcons']} units")
print(f"Discount: ${result3['discount']:.2f}")
print(f"Total bill: ${result3['total']:.2f}")
print()

# Example 4: High weekend consumption
wb4 = WeekBill(20)  # Price per unit is $20
wb4.consume(12, 30)  # 30 units on day 12 (weekend)
wb4.consume(13, 25)  # 25 units on day 13 (weekend)
result4 = wb4.bill()
print("Example 4 (High weekend consumption):")
print(f"Total consumption: {result4['totalcons']} units")
print(f"Weekend consumption: {result4['weekendcons']} units")
print(f"Discount: ${result4['discount']:.2f}")
print(f"Total bill: ${result4['total']:.2f}")
print()

# Example 5: Multiple consumption entries on the same day
wb5 = WeekBill(8)  # Price per unit is $8
wb5.consume(19, 5)  # 5 units on day 19 (weekend)
wb5.consume(19, 3)  # 3 more units on day 19 (weekend)
wb5.consume(19, 2)  # 2 more units on day 19 (weekend)
result5 = wb5.bill()
print("Example 5 (Multiple entries on same day):")
print(f"Total consumption: {result5['totalcons']} units")
print(f"Weekend consumption: {result5['weekendcons']} units")
print(f"Discount: ${result5['discount']:.2f}")
print(f"Total bill: ${result5['total']:.2f}")
print()

# Example 6: Usage across an entire month
wb6 = WeekBill(10)  # Price per unit is $10
# Add consumption for each day of the month
for day in range(30):
    if day % 2 == 0:  # Even days get 2 units
        wb6.consume(day, 2)
    else:  # Odd days get 3 units
        wb6.consume(day, 3)
result6 = wb6.bill()
print("Example 6 (Full month consumption):")
print(f"Total consumption: {result6['totalcons']} units")
print(f"Weekend consumption: {result6['weekendcons']} units")
print(f"Discount: ${result6['discount']:.2f}")
print(f"Total bill: ${result6['total']:.2f}")
print()

# Example 7: Zero consumption
wb7 = WeekBill(15)  # Price per unit is $15
result7 = wb7.bill()
print("Example 7 (Zero consumption):")
print(f"Total consumption: {result7['totalcons']} units")
print(f"Weekend consumption: {result7['weekendcons']} units")
print(f"Discount: ${result7['discount']:.2f}")
print(f"Total bill: ${result7['total']:.2f}")
print()

# Example 8: High weekday consumption, low weekend consumption
wb8 = WeekBill(25)  # Price per unit is $25
for day in range(30):
    if day in [5, 6, 12, 13, 19, 20, 26, 27]:  # Weekend days
        wb8.consume(day, 1)  # 1 unit on weekend days
    else:
        wb8.consume(day, 8)  # 8 units on weekdays
result8 = wb8.bill()
print("Example 8 (High weekday, low weekend):")
print(f"Total consumption: {result8['totalcons']} units")
print(f"Weekend consumption: {result8['weekendcons']} units")
print(f"Discount: ${result8['discount']:.2f}")
print(f"Total bill: ${result8['total']:.2f}")
print()

# Example 9: Usage with different price
wb9 = WeekBill(5.5)  # Price per unit is $5.50
wb9.consume(1, 10)
wb9.consume(5, 20)  # Weekend day
wb9.consume(10, 15)
result9 = wb9.bill()
print("Example 9 (Fractional price):")
print(f"Total consumption: {result9['totalcons']} units")
print(f"Weekend consumption: {result9['weekendcons']} units")
print(f"Discount: ${result9['discount']:.2f}")
print(f"Total bill: ${result9['total']:.2f}")
print()

# Example 10: Comparing total bill with and without weekend discount
standard_price = 18
wb10a = WeekBill(standard_price)  # With weekend discount
wb10b = WeekBill(standard_price)  # Calculating manual total without discount

# Same consumption pattern for both
for day in range(30):
    consumption = day % 5 + 1  # 1-5 units depending on day
    wb10a.consume(day, consumption)
    wb10b.consume(day, consumption)

result10a = wb10a.bill()
# Manual calculation without discount
total_without_discount = sum(wb10b.consumptions) * standard_price

print("Example 10 (With vs without discount):")
print(f"Total consumption: {result10a['totalcons']} units")
print(f"Weekend consumption: {result10a['weekendcons']} units")
print(f"Discount: ${result10a['discount']:.2f}")
print(f"Total bill with discount: ${result10a['total']:.2f}")
print(f"Total bill without discount: ${total_without_discount:.2f}")
print(f"Savings: ${total_without_discount - result10a['total']:.2f}")
