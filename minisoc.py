# MiniSOC - Simple Security Monitoring Tool

def count_failed_logins():
    failed = 0

    with open("logs/login.log", "r") as file:
        for line in file:
            if "LOGIN_FAILED" in line:
                failed += 1

    return failed


def check_port_scan():
    with open("logs/web.log", "r") as file:
        for line in file:
            if "PORT_SCAN" in line:
                return True

    return False


def check_sql_injection():
    with open("logs/web.log", "r") as file:
        for line in file:
            if "SQL_INJECTION" in line:
                return True

    return False


print("MiniSOC Security Monitor")
print("-------------------------")

failed_logins = count_failed_logins()
print("Failed login attempts:", failed_logins)

if failed_logins >= 5:
    print("ALERT: Possible Brute Force Attack!")
    print("Severity: HIGH")
else:
    print("No brute force attack detected.")

if check_port_scan():
    print("ALERT: Possible Port Scan Detected!")
    print("Severity: MEDIUM")
else:
    print("No port scan detected.")

if check_sql_injection():
    print("ALERT: Possible SQL Injection Detected!")
    print("Severity: HIGH")
else:
    print("No SQL injection detected.")

print("-------------------------")
print("Monitoring completed.")