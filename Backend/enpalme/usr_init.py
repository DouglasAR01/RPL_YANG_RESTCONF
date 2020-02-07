from colorlog import info

def jc_startup():
    #Código a ejecutar cuando inicia el servidor via Jetconf
    info("Backend: Enpalme iniciado con éxito.")

def jc_end():
    #Código a ejecutar cuando el servidor es apagado
    info("Backend: Enpalme cerrado.")
