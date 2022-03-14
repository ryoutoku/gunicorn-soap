from spyne.protocol.json import JsonDocument
from spyne.protocol.http import HttpRpc
from spyne import Iterable
from spyne import (
    Application,
    rpc,
    ServiceBase,
    Integer,
    Unicode
)
import logging

logging.basicConfig(level=logging.INFO)


class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield 'Hello, %s' % name


application = Application([HelloWorldService],
                          tns='spyne.examples.hello',
                          in_protocol=HttpRpc(validator='soft'),
                          out_protocol=JsonDocument())
