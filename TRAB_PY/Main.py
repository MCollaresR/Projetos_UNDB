from lib import Lib
from CASOS_TESTE import TesteUndb
from time import sleep

lib = Lib()
driver = lib.start_browser()
teste_main = TesteUndb(driver)

teste_main.login('001-013328', 'undb@class')
teste_main.ctt_0034()
