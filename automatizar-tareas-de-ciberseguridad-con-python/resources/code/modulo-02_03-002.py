import statistics
monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]
median_failed_attempts = statistics.median(monthly_failed_attempts)
print("median:", median_failed_attempts)
# Resultado: 20.5