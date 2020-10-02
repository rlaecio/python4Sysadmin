#!/usr/bin/env python3
import logging

logging.basicConfig(
    filename= "app.log",
    level= logging.DEBUG,
    format= "%(asctime)s [ %(levelname)s ] %(name)s\n" +
        "[ %(funcName)s ] [%(filename)s, %(lineno)s] %(message)s",
    datefmt= "[ %d/%m/%Y %H:%M:%S ]"
)


logging.debug("Mensagem de debug")
logging.info("mensagem de info")
logging.warning("mensagem de warning")
logging.error("Mensagem de Erro")
logging.critical("mensagem critica")