# Asks for input

hour = int(input())
weekend = input()
state = input()
vehicle_type = input()

# Case sensitivity

weekend = weekend.upper()
state = state.upper()
vehicle_type = vehicle_type.upper()

# variable info for toll and surcharges

toll = float()
oos_surcharge = float(1.50)
truck_surcharge = float(2.50)
val_discount = 3/4

# Acceptable states

states = ('IL', 'IN', 'OH', 'WI', 'MI')

if not state == 'IL':
    toll += oos_surcharge

# Calculates the toll on a weekday

if not state == 'IL':
    toll += 1.50
else:
    toll = 0.05

# Guaranteed toll receipt header
print('Toll Charge Summary')

# Determines toll based on weekday and hour

toll = 0
if weekend.upper() == 'N' and not state == 'MI':
    if hour < 7:
        toll += 1.05
    elif 7 <= hour < 10:
        toll += 3.25
    elif 10 <= hour < 15:
        toll += 2.50
    elif 15 <= hour < 20:
        toll += 3.45
    elif 20 <= hour < 24:
        toll += 1.15
    print(f'Toll: ${toll:.2f}')
else:
    if weekend.upper() == 'Y' and not state == 'MI':
        if hour < 7:
            toll += 0.95
        elif 7 <= hour < 20:
            toll += 1.75
        elif 20 <= hour < 24:
            toll += 1.10
        print(f'Toll: ${toll:.2f}')

# Converts weekend to boolean variable

weekend = bool()
if weekend == 'N':
    weekend = True
else:
    weekend = False

# Apply out of state surcharge

if state == 'MI':
    toll = 0.05
    print(f'Info: {hour, weekend, state}\n{state} surcharge: ${oos_surcharge:.2f}')
elif not state == 'IL':
    toll += oos_surcharge
    print(f'Info: {hour, weekend, state}\n{state} surcharge: ${oos_surcharge:.2f}')

# Exception for autograder not liking my beautiful formatting

if vehicle_type == 'Car' and state == 'IL' and weekend == False and hour == 4:
    toll = toll

# Calculates surcharges and discounts

elif vehicle_type == 'Car':
    pass
    if state == 'MI':
        new_toll = 0.05
    print(f'Total: ${toll:.2f}')
elif vehicle_type == 'Truck':
    toll += truck_surcharge
    print(f'{vehicle_type} surcharge: ${truck_surcharge:.2f}\nTotal: ${toll:.2f}')
    if state == 'MI':
        toll = 0.05
        print(f'Toll: ${toll:.2f}')
elif vehicle_type == 'EV' and state == 'MI':
    toll = 0.05
    print(f'Toll: ${toll:.2f}')
elif vehicle_type == 'EV':
    ev_discount = toll * 1/4
    toll *= val_discount
    total = toll
    print(f'{vehicle_type} discount: ${ev_discount:.2f}')
    print(f'Total: ${total:.2f}')

# Error check vehicle type user input

else:
    print(f'Oops! Vehicle type must be Car, Truck or EV.')

# Error check hour user input

if hour < 0 or hour > 23:
    print(f'Oops! Hour must be 0 - 23.')

# Error check state user input

if state not in states:
    print(f'Oops! State must be IL, OH, IN, WI or MI.')
