logs_servidor = [
    {"ip": "192.168.1.10", "endpoint": "/home", "status": 200, "user_agent": "Chrome"},
    {"ip": "45.33.22.11", "endpoint": "/wp-admin.php", "status": 403, "user_agent": "Python-urllib"},
    {"ip": "10.0.0.5", "endpoint": "/api/v1/users", "status": 200, "user_agent": "Safari"},
    {"ip": "88.15.44.3", "endpoint": "/.env", "status": 404, "user_agent": "Curl/7.68.0"},
    {"ip": "192.168.1.12", "endpoint": "/dashboard", "status": 200, "user_agent": "Firefox"}
]

def es_amenaza(log:dict) -> bool:

    endpoints_peligroso = [".env", "wp-admin", "config.php"]

    if any(peligro in log['endpoint'] for peligro in endpoints_peligroso):
        return True
    
    if log["status"] == 403 and log ["user_agent"] not in ["Chrome", "Firefox", "Safari", "Edge"]:
        return True
    
    return False

ataques = list(filter(es_amenaza, logs_servidor))

for ataque in ataques:
    print(f" [Ip bloqueada]: {ataque["ip"]} -> Intenco acceder a: {ataque["endpoint"]}")