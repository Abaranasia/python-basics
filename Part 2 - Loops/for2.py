from data import *

# Count how many items of each type are

for fault in analysis["faults"]:
    for status in statuses:
        if fault["status"] == status["type"]:
            status["count"] += 1

# print (statuses)
for status in statuses:
    print(f"{status['type']}: {status['count']}")
