
from spyne import Application
from spyne.protocol.soap import Soap12

from .service import Service


application = Application([Service, ],
                          'spyne.examples.hello.soap',
                          in_protocol=Soap12(validator='lxml'),
                          out_protocol=Soap12())
