import platform
import subprocess
import time
import socket
import ssl

def ping_site(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    
    try:
        output = subprocess.run(command, capture_output=True, text=True, timeout=5)
        if output.returncode == 0:
            return f"{host} is active!"
    except (subprocess.TimeoutExpired, Exception):
        return

def check_ssl(host):
    context = ssl.create_default_context()
    try:
        with socket.create_connection((host, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                ssock.getpeercert()
                return f"{host} SSL certificate is valid!"
    except Exception as e:
        return

sites = [
    "google.com",
    "youtube.com",
    "facebook.com",
    "twitter.com",
    "instagram.com",
    "linkedin.com",
    "pinterest.com",
    "tumblr.com",
    "reddit.com",
    "wordpress.com",
    "blogspot.com",
    "wikipedia.org",
]

def main():
    while True:
        print("\nChecking the status of the sites...")
        print("-" * 40)
        
        for site in sites:
            ping_result = ping_site(site)
            ssl_result = check_ssl(site)
            print(ping_result)
            print(ssl_result)
        
        print("\nWill check again in 30 seconds...")
        time.sleep(30)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated.")