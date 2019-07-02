import requests

res = requests.get("https: // www.illinois.gov/aging/AboutUs/Documents /
                   Exec_Phone_EmailDirectory.pdf")
res.raise_for_status()
# print(res.status_code)
