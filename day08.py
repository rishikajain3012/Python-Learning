server_info = {
    "name": "DV01",
    "database": "DB2",
    "status": "Active"
}

print(server_info["name"])
print(server_info["database"])
production = {"DB2", "Oracle", "PostgreSQL"}
development = {"DB2", "MySQL", "PostgreSQL"}
print(production.union(development))
print(production.intersection(development))