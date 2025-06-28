import time
from datetime import datetime

# getting input
alarm_input = input("Set the alarm time (HH:MM:SS AM/PM): ").strip()

# Split the input
try:
    time_part, period = alarm_input.split()
    hour_str, minute_str, second_str = time_part.split(":")
    
    hour = int(hour_str)
    minute = int(minute_str)
    second = int(second_str)
    period = period.upper()

    if period not in ["AM", "PM"]:
        print("Invalid period. Use AM or PM.")
        exit()

except ValueError:
    print("Invalid input format. Use HH:MM:SS AM/PM")
    exit()

print("⏳ Waiting for the alarm time... Please wait a few seconds/minutes...")

# Loop to wait for match
while True:
    now = datetime.now()
    curr_hour = int(now.strftime("%I"))
    curr_minute = int(now.strftime("%M"))
    curr_second = int(now.strftime("%S"))
    curr_period = now.strftime("%p")

    # Conditional check
    if (curr_hour == hour and 
        curr_minute == minute and 
        curr_second == second and 
        curr_period == period):
        print("⏰ Wake up! Alarm ringing at", now.strftime("%I:%M:%S %p"))
        break
    else:
        time.sleep(1)
