db2_objects = ("TABLESPACE", "INDEX", "TABLE", "TABLESPACE", "DATABASE")
db2_objects = ("TABLESPACE", "INDEX", "TABLE", "TABLESPACE", "DATABASE")

# 1. First item
print(db2_objects[0])

# 2. Last item
print(db2_objects[-1])

# 3. Count TABLESPACE
print(db2_objects.count("TABLESPACE"))

# 4. Position of INDEX
print(db2_objects.index("INDEX"))

# 5. Middle items
print(db2_objects[1:4])