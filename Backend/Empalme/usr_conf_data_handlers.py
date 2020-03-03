from jetconf.handler_base import ConfDataObjectHandler
from yangson.instance import InstanceRoute
from jetconf.data import BaseDatastore, DataChange


class MyConfDataHandler(ConfDataObjectHandler):
    def create(self, ii: InstanceRoute, ch: DataChange):
        pass

    def replace(self, ii: InstanceRoute, ch: DataChange):
        pass

    def delete(self, ii: InstanceRoute, ch: DataChange):
        pass

def register_conf_handlers(ds: BaseDatastore):
    ds.handlers.conf.register(MyConfDataHandler(ds, "/prueba-conf"))
