from colorlog import info

from yangson.instance import InstanceRoute

from jetconf.helpers import JsonNodeT, PathFormat
from jetconf.handler_base import StateDataContainerHandler
from jetconf.handler_base import StateDataListHandler
from jetconf.data import BaseDatastore
from . import sim_inst_rpl

RPL = sim_inst_rpl.RPL
RUTA_RPL = "/ietf-routing:routing/control-plane-protocols/" + \
             "control-plane-protocol/uis-rpl:rpl"

class RPLNodesCount(StateDataContainerHandler):
    def generate_node(self, node_ii: InstanceRoute, username: str, staging: bool) -> JsonNodeT:
        return len(RPL['TOPOLOGIA'])+1

class RPLPreferredParents(StateDataListHandler):
    def generate_list(self, node_ii: InstanceRoute, username: str, staging: bool) -> JsonNodeT:
        padres = []
        for ip in RPL['TOPOLOGIA']:
            entrada = {
                "ipv6-address" : ip,
                "parent-ipv6-address" : RPL['TOPOLOGIA'][ip]['PADRE'],
                "parent-rank" : RPL['TOPOLOGIA'][ip]['PADRE_RANGO'],
                "parent-cost" : RPL['TOPOLOGIA'][ip]['PADRE_COSTO'],
                "rank" : RPL['TOPOLOGIA'][ip]['RANGO'],
                "cost" : RPL['TOPOLOGIA'][ip]['COSTO']
            }
            padres.append(entrada)
        return padres

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

def register_state_handlers(ds: BaseDatastore):
    handlers = [
        RPLPreferredParents(ds, RUTA_RPL+ "/routing-modes/upward-routing" + \
        "/node-preferred-parents/node-preferred-parent"),
        RPLNodesCount(ds, RUTA_RPL+ "/routing-modes/upward-routing" + \
        "/dodag-topology/num-of-nodes"),
        RPLRoutingTable(ds, RUTA_RPL + "/routing-modes/downward-routing" + \
        "/routing-table"),
        #Siguiente
    ]
    for handler in handlers:
        ds.handlers.state.register(handler)
