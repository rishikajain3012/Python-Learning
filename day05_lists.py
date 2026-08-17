servers = ["DV03", "DV01", "DV02"]
servers.append("DV04")
servers.append("PROD01")
servers.remove("DV03")
servers.sort()
print(servers)