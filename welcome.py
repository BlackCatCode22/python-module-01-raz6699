name = input('Enter your name: ')

from datetime import datetime

# Get the current system time
current_time = datetime.now().time()

# Determine the appropriate greeting based on the current time - 24-hour clock
if current_time.hour < 12:
    greeting = "Good morning"
elif 12 <= current_time.hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

print (greeting,name)
