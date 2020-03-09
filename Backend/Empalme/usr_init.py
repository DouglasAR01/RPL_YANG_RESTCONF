from colorlog import info

def jc_startup():
    #Código a ejecutar cuando inicia el servidor via Jetconf
    info("Backend: Empalme iniciado con éxito.")

def jc_end():
    #Código a ejecutar cuando el servidor es apagado
    info("Backend: Empalme cerrado.")
