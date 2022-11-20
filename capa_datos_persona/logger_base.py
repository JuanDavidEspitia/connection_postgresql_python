import logging as log

# si lo cambiamos a INFO, solo muestra de INFO en adelante, es por jerarquia de Logs
log.basicConfig(level=log.DEBUG)





if __name__ == '__main__':
    log.debug('Mensaje a nivel de Debug')
    log.info('Mensaje a nivel de Info')
    log.warning('Mensaje a nivel de Warning')
    log.error('Mensaje a nivel de Error')
    log.critical('Mensaje a nivel de Critical')