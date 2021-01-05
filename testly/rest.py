import requests
import __main__


def call_restendpoint():
    if __main__.debug == 1:
        print("DEBUG: REST url: ", __main__.host)
    return __main__.sys.exit(0)


class Restly:

    def getStatus(self,URL):
        response = requests.get(URL)
        print("Status Code for Request: {} ".format(response.status_code))
        return __main__.sys.exit(0)
