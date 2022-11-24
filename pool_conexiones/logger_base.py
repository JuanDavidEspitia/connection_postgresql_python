import logging as log

# si lo cambiamos a INFO, solo muestra de INFO en adelante, es por jerarquia de Logs
# Con los sigueintes parametros ajustamos el mensaje de como queremos que salga en consola o arhcivo
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M%:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel de Debug')
    log.info('Mensaje a nivel de Info')
    log.warning('Mensaje a nivel de Warning')
    log.error('Mensaje a nivel de Error')
    log.critical('Mensaje a nivel de Critical')