def calculate_fare(distance):
    return 50+(10*distance)
trips=[5,10,3]
total=0
for i,d in enumerate(trips,1):
    fare=calculate_fare(d)
    total+=fare
    print(f"Trip {i}: ${fare}")
print(f"Total Fare: ${total}")
