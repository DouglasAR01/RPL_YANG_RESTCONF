echo 'ACTUALIZANDO...'
curl --http2-prior-knowledge -X PUT -d '{"uis-rpl:metric":"'$3'"}' \
"http://$1:8443/rpl/data/\
ietf-routing:routing/control-plane-protocols/\
control-plane-protocol=uis-rpl:rpl,RPL/uis-rpl:rpl/metrics/metric=$2"

echo 'RESULTADO...'
curl --http2-prior-knowledge -X GET "http://$1:8443/rpl/data/\
ietf-routing:routing/control-plane-protocols/\
control-plane-protocol=uis-rpl:rpl,RPL/uis-rpl:rpl/metrics"
