import requests

res = requests.get('https://www.illinois.gov/aging/AboutUs/Documents/Exec_Phone\
	_EmailDirectory.pdf')
res.raise_for_status()
#print(res.status_code)