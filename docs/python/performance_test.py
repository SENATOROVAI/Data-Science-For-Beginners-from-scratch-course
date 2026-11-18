"""Бенчмарк производительности: замеры времени выполнения примеров."""

import time

start_time = time.time()
total = 0
for i in range(1, 10_000_000):
    total += i
end_time = time.time()

print("Result:", total)
print("Execution time:", end_time - start_time, "seconds")
