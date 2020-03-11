# Este archivo solo simula los datos que proporcionaría una instancia
# del protocolo RPL en ejecución.
# En un caso real, el router físico proporcionaría de alguna forma los
# datos que genera el protocolo RPL.
#
RPL = {
    "VECINOS" : [
        "2001:db8:0:1::2",
        "2001:db8:0:1::5"
    ],

    "TOPOLOGIA" : {
        "2001:db8:0:1::2" : {
            "PADRE" : "2001:db8:0:1::1",
            "PADRE_RANGO" : 0,
            "PADRE_COSTO" : 1,
            "RANGO" : 1,
            "COSTO" : 1
        },
        "2001:db8:0:1::5" : {
            "PADRE" : "2001:db8:0:1::1",
            "PADRE_RANGO" : 0,
            "PADRE_COSTO" : 1,
            "RANGO" : 1,
            "COSTO" : 1
        },
        "2001:db8:0:1::3" : {
            "PADRE" : "2001:db8:0:1::2",
            "PADRE_RANGO" : 1,
            "PADRE_COSTO" : 1.2,
            "RANGO" : 2,
            "COSTO" : 2.2
        },
        "2001:db8:0:1::4" : {
            "PADRE" : "2001:db8:0:1::3",
            "PADRE_RANGO" : 2,
            "PADRE_COSTO" : 3,
            "RANGO" : 3,
            "COSTO" : 5.2
        },
        "2001:db8:0:1::6" : {
            "PADRE" : "2001:db8:0:1::5",
            "PADRE_RANGO" : 1,
            "PADRE_COSTO" : 2,
            "RANGO" : 2,
            "COSTO" : 3
        },
        "2001:db8:0:1::7" : {
            "PADRE" : "2001:db8:0:1::2",
            "PADRE_RANGO" : 1,
            "PADRE_COSTO" : 1.7,
            "RANGO" : 2,
            "COSTO" : 2.2
        },
        "2001:db8:0:1::8" : {
            "PADRE" : "2001:db8:0:1::2",
            "PADRE_RANGO" : 2,
            "PADRE_COSTO" : 1.1,
            "RANGO" : 3,
            "COSTO" : 3.8
        }
    }
}
