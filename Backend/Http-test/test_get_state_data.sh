echo "====TOPOLOGÍA:===="
curl --http2-prior-knowledge -X GET "http://$1:8443/rpl/data/\
ietf-routing:routing/control-plane-protocols/\
control-plane-protocol=uis-rpl:rpl,RPL/uis-rpl:rpl/\
routing-modes/upward-routing/node-preferred-parents/node-preferred-parent"

echo "====TABLA DE RUTAS===="
curl --http2-prior-knowledge -X GET "http://$1:8443/rpl/data/\
ietf-routing:routing/control-plane-protocols/\
control-plane-protocol=uis-rpl:rpl,RPL/uis-rpl:rpl/\
routing-modes/downward-routing/routing-table"
