Usage = float(input("Enter your CPU Usage: "))
Tables = int(input("Enter your Tables: "))
DATABASE = "DB2"
if (Usage <70):
    grade = "CPU Usage Normal"
elif(Usage >70 and Usage<90):
    grade = "CPU Usage High"
else :        
    grade = "CPU Usage Critical"

print("Your Grade is",grade)  

print("Database:",DATABASE)
print("CPU USAGE:",Usage)
print("Tables:",Tables)
print("Status:",grade)