
from spyne import Integer, Iterable, ServiceBase, Unicode, rpc
import logging
from .models import RequestParameter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


class Service(ServiceBase):

    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello_1(ctx, name, times):
        logger.info("say_hello_1")
        for i in range(times):
            yield f'Hello, {name}'

    @rpc(RequestParameter, _returns=Iterable(Unicode))
    def say_hello_2(ctx, request_parameter: RequestParameter):
        logger.info("say_hello_2")
        for i in range(request_parameter.times):
            yield f'Hello, {request_parameter.name}'

    @rpc(RequestParameter, _returns=RequestParameter)
    def say_hello_3(ctx, request_parameter: RequestParameter):
        logger.info("say_hello_3")
        logger.info(request_parameter.name)
        logger.info(request_parameter.times)
        return request_parameter
