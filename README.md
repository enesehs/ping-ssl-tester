# Ping-Ssl-Tester

A Python script that continuously monitors the status and SSL certificates of popular websites. It checks whether the sites are reachable and validates their SSL certificates to ensure secure communication.

## How It Works
1. **Ping Check**: Sends a single ping to each site in the list to determine if it is active (reachable).
2. **SSL Certificate Check**: Validates the SSL certificate of each site to confirm secure communication.
3. **Loop**: The checks are repeated every 30 seconds, providing real-time monitoring.

## Features
- Supports both Windows and Unix-based systems.
- Detects unreachable sites or invalid SSL certificates.
- Periodic updates with user-friendly output.

## Usage
1. Ensure Python3 is installed on your system.
2. Run the script using the following command:
3. If you want change custom domains and websites

   ```bash
   python main.py


# Example Output
```
Checking the status of the sites...
----------------------------------------
google.com is active!
google.com SSL certificate is valid!
facebook.com is active!
facebook.com SSL certificate is valid!
...
Will check again in 30 seconds...
