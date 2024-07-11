with open('proxies.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(':')
        if len(parts) == 4:
            ip = parts[0]
            port = parts[1]
            username = parts[2]
            password = parts[3]
            formatted_proxy = f'{username}:{password}@{ip}:{port}'
            print(formatted_proxy)
