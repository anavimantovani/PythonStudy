
import time

for hour in range(0, 24):
    for minute in range(0, 60):
        for second in range(0, 60):
            print(format(hour, '02d') + ':' + format(minute, '02d') + ':' + format(second, '02d'))


            time.sleep(1)


