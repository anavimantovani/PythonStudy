hour_of_day = int(input('Enter the hour of day (1-12): '))
meridiem = input('Enter "am" or "pm": ')

print()
print()

if meridiem == 'am':
    print('Good morning!')
elif hour_of_day <= 4 or hour_of_day == 12:
    print('Good afternoon!')
else:
    print('Good evening!')
