import os
import subprocess
import json

cve_list = [
    "CVE-2023-0001", # Example CVE
    "CVE-2023-0002", # Example CVE
    "CVE-2022-1234", # Example CVE
    "CVE-2021-44228",# Log4j (Apache Log4j library)
    "CVE-2017-5638", # Apache Struts (Another library)
    "CVE-2019-17571",# Log4j (Apache Log4j library)
    "CVE-2015-0204", # OpenSSL (Different library)
    "CVE-2018-11776" # Apache Struts (Another library)
]
packages = [
    ("formidable", "1.2.2"),
    ("follow-redirects", "1.15.2"),
    ("follow-redirects", "1.15.6"),
    ("ecdsa-sig-formatter", "1.0.11")
]

def task2():
    # creating a directory for the project
    project_dir = "my-node-project"
    os.makedirs(project_dir, exist_ok=True)
    
    os.chdir(project_dir)
    
    # initialize a new Node.js project
    subprocess.run(["npm", "init", "-y"], check=True)
    
    for package in packages:
        # Installing current package
        subprocess.run(["npm", "install", f"{package[0]}@{package[1]}"], check=True)
        print(f"installed the package : {package[0]} of version :{package[1]}")
        # npm audit and save output
        result = subprocess.run(["npm", "audit", "--json"], capture_output=True, text=True)
        audit_data = json.loads(result.stdout)

        # Check for vulnerabilities
        vulnerabilities = audit_data.get("vulnerabilities", {})

        if vulnerabilities:
            print("Vulnerabilities found:")
            for package, details in vulnerabilities.items():
                print(f"- Package: {package}")
                print(f"  Severity: {details['severity']}")
                print(f"  Version: {details['via'][0]['range']}")
                print(f"  More info: {details['via'][0]['url']}\n")
        else:
            print("No vulnerabilities found.")

    # output a message indicating completion
    print("npm audit completed.")

    # cleaning
    os.chdir("..")
    subprocess.run(["rm", "-rf", project_dir])


task2()
print("-------------------------------------------------\n")


result = '''
Vulnerabilities found:
- Package: follow-redirects
  Severity: moderate
  Version: <1.15.4
  More info: https://github.com/advisories/GHSA-jchw-25xp-jwwc

"Versions of the package follow-redirects before 1.15.4 are vulnerable to Improper Input Validation due to the improper handling of URLs by the url.parse() function. When new URL() throws an error, it can be manipulated to misinterpret the hostname. An attacker could exploit this weakness to redirect traffic to a malicious site, potentially leading to information disclosure, phishing attacks, or other security breaches."

'''

print(result)