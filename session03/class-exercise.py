
import time
epoch = time.time()
days = epoch / (60 * 60 * 24)
hour = days % int(days) * 24
min  = hour % int(hour) * 60
sec  = min % int(min) * 60
print(f"Days: {int(days)}")
print(f"Time: {int(hour)}:{int(min)}:{int(sec)}")
