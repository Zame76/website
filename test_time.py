from datetime import datetime, UTC



date_str = "2023-11-13 22:18:11.972260"
# date_str = '2023-11-13' 
date_format = '%Y-%m-%d %H:%M:%S'
# test = datetime.strptime("2023-11-13T17:21:19Z", "%Y-%m-%d %H:%M:S")
test = datetime.strptime(date_str, date_format)

delta = datetime.now() - test


# print(datetime.now(UTC))
print(test)
print(datetime.now())
print(f"time diff: {delta.total_seconds() / 60}")
#print(f"time diff: {delta.min()}")

# print(test2.utcoffset())
