from zeep import Client
from models import RequestParameter


class Caller:

    def __init__(self):
        wsdl_url = "http://0.0.0.0:8080/?wsdl"
        self._name = "dummy_name"
        self._times = 3
        self._client = Client(wsdl_url)

    def call_say_hello_1(self):
        result = self._client.service.say_hello_1(
            self._name,
            self._times)
        print(result)

    def call_say_hello_2(self):
        result = self._client.service.say_hello_2(
            {
                "name": self._name,
                "times": self._times
            }
        )
        print(result)

    def call_say_hello_3(self):
        param = RequestParameter(
            name=self._name,
            times=self._times
        )
        result = self._client.service.say_hello_3(param.as_dict())
        print(result)
        print(type(result))


def main():

    caller = Caller()

    caller.call_say_hello_1()
    print("=====================")
    caller.call_say_hello_2()
    print("=====================")
    caller.call_say_hello_3()
    print("=====================")


if __name__ == '__main__':
    main()
