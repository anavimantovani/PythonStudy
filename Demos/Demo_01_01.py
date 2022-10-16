# Rocket blast countdown
import time

seconds = 10

while seconds>= 1:
  print('T -', seconds,'seconds')
  time.sleep(1)
  seconds = seconds - 1

print()
print('BLAST OFF!!')
