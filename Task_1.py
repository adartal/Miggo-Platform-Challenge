
###############################################
#Task 1 
import socket
import requests

domains = [
    "example.com",
    "nonexistentdomain.xyz",
    "google.com",
    "localhost",
    "test.invalid",
    "openai.com",
    "facebook.com",
    "private.example.com",
    "kafka.miggo.io",   # Open to the internet
    "backoffice.miggo.io",  # Not open to the internet
    "app.miggo.io",   # Open to the internet
    "miggo.io",   # Open to the internet
    "collector.miggo.io" # Not open to the internet
]

def is_public(domain):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        # Attempt HTTP/HTTPS request
        for scheme in ["http", "https"]:
            try:
                response = requests.get(f"{scheme}://{domain}", timeout=5, headers=headers)
                if response.status_code == 200:
                    return True
            except requests.RequestException:
                pass
    except (socket.gaierror, requests.RequestException) as e:
        return False
    
    return False

def test_is_public():
    test_cases = [
        ("example.com", True),
        ("nonexistentdomain.xyz", False),
        ("localhost", False),
        ("test.invalid", False),
        ("openai.com", True)
    ]
    [print(f"PASSED: {domain} -> {expected}" if is_public(domain) == expected 
           else f"FAILED: {domain} -> {not expected} (Expected: {expected})") for domain, expected in test_cases]

# Run the tests
test_is_public()

public_domains = {domain: is_public(domain) for domain in domains}
[print(domain) for domain in public_domains.items()]


