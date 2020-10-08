#!/usr/bin/env python3
import logging

logging.basicConfig(
    filename= "ref.log",
    level= logging.DEBUG,
    format= "%(asctime)s [ %(levelname)s ] %(name)s [ %(funcName)s ] [ %(filename)s, %(lineno)s ] %(message)s",
    datefmt= "[ %d/%m/%Y %H:%M:%S ]"
)


# logging.debug("Mensagem de debug")
# logging.info("mensagem de info")
# logging.warning("mensagem de warning")
# logging.error("Mensagem de Erro")
# logging.critical("mensagem critica")49


CUSTOM = 49
logging.addLevelName(CUSTOM, "CUSTOM")
def custom(self, message, *args, **kwargs):
    if self.isEnabledFor(CUSTOM):
        self._log(CUSTOM, message, args, **kwargs)
logging.Logger.custom = custom

logger = logging.getLogger()
logger.custom("Meu log custamizado")