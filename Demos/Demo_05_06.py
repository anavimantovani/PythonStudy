
STOP_VALUE = 200
STEP_AMOUNT = 25

counter = 25
total = 0


while counter <= STOP_VALUE:
    print(counter)
    total = total + counter
    counter += STEP_AMOUNT


print()
print('Total:', total)
