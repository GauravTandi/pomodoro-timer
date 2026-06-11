import sys
import time

timer_set = sys.argv[1]
hr_min_sec = sys.argv[2]

if "hr" in hr_min_sec:
    print("setting time for hours")
elif "min" in hr_min_sec:
    print("setting time for minutes")
    time.sleep(5)
elif "sec" in hr_min_sec:
    print("setting time for seconds")
else:
    print("usage: \n")

print(timer_set)