from colorlog import info

from yangson.instance import InstanceRoute

from jetconf.helpers import JsonNodeT, PathFormat
from jetconf.handler_base import StateDataContainerHandler
from jetconf.handler_base import StateDataListHandler
from jetconf.data import BaseDatastore
from . import sim_inst_rpl

RUTA_RPL = "/ietf-routing:routing/control-plane-protocols/" + \
             "control-plane-protocol=uis-rpl:rpl,RPL/uis-rpl:rpl"

class RPLNodesCount(StateDataContainerHandler):
    def generate_node(self, node_ii: InstanceRoute, username: str, staging: bool) -> JsonNodeT:
        ruta = RUTA_RPL + "/routing-modes/upward-routing/" + \
        "node-preferred-parents/node-preferred-parent"
        lista_nodos_ii = self.ds.parse_ii(ruta,PathFormat.URL)
        nodos = self.ds.get_data_root().goto(lista_nodos_ii).value
        return len(nodos)

class RPLRoutingTable(StateDataListHandler):
    def generate_list(self, node_ii: InstanceRoute, username: str, staging: bool) -> JsonNodeT:
        rutas = []
        for ip in RPL['TOPOLOGIA']:
            par = {
                "dest-ip" : ip,
                "next-hop-ip" : RPL['TOPOLOGIA'][ip]['PADRE']
            }
            rutas.append(par)
        return rutas
class Prueba(StateDataContainerHandler):
    def generate_node(self, node_ii: InstanceRoute, username: str, staging: bool) -> JsonNodeT:
        return 0;

def register_state_handlers(ds: BaseDatastore):
    handlers = [
        RPLNodesCount(ds,RUTA_RPL+ "/routing-modes/upward-routing" + \
        "/dodag-topology/num-of-nodes"),
        RPLRoutingTable(ds, RUTA_RPL + "/routing-modes/downward-routing" + \
        "/routing-table"),

        #Siguiente
    ]
    for handler in handlers:
        ds.handlers.state.register(handler)
