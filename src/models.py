from spyne import ComplexModel
from spyne.model.primitive import String, Integer


class RequestParameter(ComplexModel):
    name = String
    times = Integer
