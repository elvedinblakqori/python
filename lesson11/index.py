import datetime

current_time = datetime.datetime.now()

print("Year:" ,current_time.year)
print("Month:" ,current_time.month)
print("Day:" ,current_time.day)
print("Hour:" ,current_time.hour)
print("Minute:" ,current_time.minute)
print("Second:" ,current_time.second)
print("Microsecond:" ,current_time.microsecond)

current1_time = datetime.datetime.now().date()

print(current1_time)

settime = datetime.datetime.now()

specific_time = datetime.datetime(2020, 10, 22)


print(specific_time.year)
print(specific_time.month)
print(specific_time.day)

future_time = current_time + datetime.timedelta(days= 100)



print(future_time)


teksti1 = "Hello world this is the world where we drink ashav"

with open("example.txt", "w") as file:
    file.write(teksti1)

file_path = "example.txt"
file = open(file_path, "r")

content = file.read()
print(content)
file.close()

with open("example.txt", "r") as file:
    lines = file.readLines()
    print(lines)

with open("example.txt", "r") as file:
    line = file.readLine()
    print(line)



