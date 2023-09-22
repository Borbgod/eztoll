# Asks for input

hour = int(input())
weekend = input()
state = input()
vehicle_type = input()
addons = bool()
# Case sensitivity

weekend = weekend.upper()
state = state.upper()

# Variable info for toll and surcharges

toll = float(0)
val_discount = 3/4
oos_surcharge = float(0)
truck_surcharge = float(0)
ev_discount = 0
total = 0
# Acceptable states

states = ('IL', 'IN', 'OH', 'WI', 'MI')


if not state == 'IL':
    toll += 1.50
else:
    toll = 0.05

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
else:
    if weekend.upper() == 'Y' and not state == 'MI':
        if hour < 7:
            toll += 0.95
        elif 7 <= hour < 20:
            toll += 1.75
        elif 20 <= hour < 24:
            toll += 1.10

# Converts weekend to boolean variable

weekend = bool()
if weekend == 'N':
    weekend = True
else:
    weekend = False

# Apply out of state surcharge

if state == 'MI':
    toll = 0.05
elif not state == 'IL':
    oos_surcharge = float(1.50)
    total = + toll + oos_surcharge

# Guaranteed toll receipt header

print('Toll Charge Summary')
print(f'Info: {hour, weekend, state}')
print(f'Toll: ${toll:.2f}')

# Calculates surcharges and discounts
if vehicle_type == 'Car':
    pass
    if state == 'MI':
        toll = 0.05
elif vehicle_type == 'Truck' and state == 'MI':
    toll = 0.05
elif vehicle_type == 'Truck':
    truck_surcharge = float(2.50)
    total += truck_surcharge
elif vehicle_type == 'EV' and state == 'MI':
    toll = 0.05
elif vehicle_type == 'EV':
    ev_discount = total * 0.25
    total -= ev_discount
else:
    print(f'Oops! Vehicle type must be Car, Truck or EV.')


# Fixes surcharges

if oos_surcharge > 0:
    print(f'{state} surcharge: ${oos_surcharge:.2f}')
    if vehicle_type == 'Car':
        print(f'Total: ${total:.2f}')
if truck_surcharge > 0:
    print(f'{vehicle_type} surcharge: ${truck_surcharge:.2f}\nTotal: ${total:.2f}')
    print(f'Total: ${total:.2f}')
elif ev_discount > 0:
    print(f'{vehicle_type} discount: ${ev_discount:.2f}')
    print(f'Total: ${total:.2f}')

# Error check hour user input

if hour < 0 or hour > 23:
    print(f'Oops! Hour must be 0 - 23.')

# Error check state user input

if state not in states:
    print(f'Oops! State must be IL, OH, IN, WI or MI.')
