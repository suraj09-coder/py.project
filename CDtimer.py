import time

my_time=int(input("ENTER THE TIME IN SECONDS :"))
for x in reversed(range(0, my_time)):
    second=x%60
    minute=int(x/60)%60
    hour=int(x/3600)
    x=(f"{hour:02}:{minute:02}:{second:02}")
    print(x)
    time.sleep(1)
