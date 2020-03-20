echo 'AÑADIENDO...'
curl --http2-prior-knowledge -X POST -d '{"uis-rpl:metric":"'$2'"}' \
"http://$1:8443/rpl/data/\
ietf-routing:routing/control-plane-protocols/\
control-plane-protocol=uis-rpl:rpl,RPL/uis-rpl:rpl/metrics"

echo 'RESULTADO...'
curl --http2-prior-knowledge -X GET "http://$1:8443/rpl/data/\
ietf-routing:routing/control-plane-protocols/\
control-plane-protocol=uis-rpl:rpl,RPL/uis-rpl:rpl/metrics"
