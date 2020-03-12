from yangson.instance import InstanceRoute
from jetconf.helpers import JsonNodeT
from jetconf.data import BaseDatastore

from . import sim_inst_rpl
from colorlog import info

RPL = sim_inst_rpl.RPL
RUTA_RPL = "/ietf-routing:routing/control-plane-protocols/" + \
             "control-plane-protocol/uis-rpl:rpl"

class OpHandlersContainer:
    def __init__(self, ds: BaseDatastore):
        self.ds = ds

    def RPl_get_route_stack(self, input_args: JsonNodeT, username: str) -> JsonNodeT:
        def busqueda_recursiva(stack, destino):
            for ip in RPL['TOPOLOGIA']:
                if ip == destino:
                    stack.append(ip)
                    busqueda_recursiva(stack,RPL['TOPOLOGIA'][ip]['PADRE'])
                    break
        info('Generando stack de enrutamiento...')
        stack = []
        target = input_args["uis-rpl:target-ipv6-address"]
        busqueda_recursiva(stack,target)
        stack.reverse()
        info('Enviando...')
        return stack

def register_op_handlers(ds: BaseDatastore):
    handlers = [
        OpHandlersContainer(ds).RPl_get_route_stack,
    ]
    for handler in handlers:
        ds.handlers.op.register(handler,"uis-rpl:get-route-stack")
