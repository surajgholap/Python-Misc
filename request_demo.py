import requests


def main():
    url = "http://httpbin.org/xml"
    result = requests.get(url)
    print_results(result)

    url = "http://httpbin.org/post"
    data = {
        "key1": "val1",
        "key2": "val2"
    }
    result = requests.post(url, data=data)
    print_results(result)

    url = "http://httpbin.org/get"
    headers = {
        "User-Agent": "Arihan App / 1.1"
    }
    result = requests.get(url, headers=headers)
    print_results(result)


def print_results(res):
    print("Result code: {}".format(res.status_code))

    print("Header--")
    print(res.headers)

    print("Returned data--")
    print(res.text)


if __name__ == "__main__":
    main()
