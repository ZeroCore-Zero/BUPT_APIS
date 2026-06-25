from buptapi.service import Service
from buptapi.endpoint import Endpoint

class CAS(Service):
    BASEURI = "https://auth.bupt.edu.cn"
    LOGIN = Endpoint("/authserver/login")
