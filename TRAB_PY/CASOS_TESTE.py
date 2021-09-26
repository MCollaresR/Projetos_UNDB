from selenium.webdriver.common.by import By
from lib import Lib
from time import sleep
import pyautogui

class TesteUndb (Lib):
    URL = 'https://undbclassroom.undb.edu.br/login/index.php#'
    __EMAIL_TEXTBOX =  By.ID, 'username'
    __SENHA_TEXTBOX = By.ID, 'password'
    __ACESSAR_BUTTON = By.CLASS_NAME, 'btn-primary'
    __CONF_ACESS = By.XPATH, '//*[@id="themesettings-control"]/span'
    __XPATH_CX_DISLX = By.XPATH, '//*[@id="fonttype"]'
    __XPATH_DISLX_SOP = By.XPATH, '//*[@id="fonttype"]/option[2]'
    __CLASS_PERFIL = By.CLASS_NAME, 'userpicture defaultuserpic'
    __XPATH_PREFERENCIAS = By.XPATH, '//*[@id="actionmenuaction-6"]'
    __XPATH_IDIOMA_PREFERIDO = By.XPATH, '//*[@id="region-main"]/div/div/div/div/div[1]/div/div/div/div[3]/a'
    __XPATH_CX_IDIOMA = By.XPATH, '//*[@id="id_lang"]'
    __XPATH_INGLES = By.XPATH, '//*[@id="id_lang"]/option[1]'
    __NAME_SAVE_IDIOMA = By.NAME, 'Salvar mudanças'
    __XPATH_ICON_MSG = By.XPATH, '//*[@id="message-drawer-toggle-614f5910d1996614f5910a546218"]'
    __XPATH_MSG_FAV = By.XPATH, '//*[@id="yui_3_17_2_1_1632590098721_72"]'
    __XPATH_MSG_SELF_USER = By.XPATH, '//*[@id="view-overview-favourites-target-614f5910d6a43614f5910a546229"]/div[2]/a/div[1]/p'
    __TESTE_SELF_TEXTBOX_ = By.XPATH, '//*[@id="message-drawer-614f5910d6a43614f5910a546229"]/div[3]/div[1]/div[1]/div[2]/textarea'
    __ICON_BARRA_LATERAL = By.CLASS_NAME, 'btn nav-link float-sm-left mr-1'
    __LINK_GEST_QUALD_SFT = By.LINK_TEXT, 'https://undbclassroom.undb.edu.br/course/view.php?id=3835'
    __ICON_PARTICIPANTES = By.LINK_TEXT, 'https://undbclassroom.undb.edu.br/user/index.php?id=3835'
    __LINK_MANUAL_DO_CASE = By.XPATH, '//*[@id="module-29817"]/div/div/div[2]/div/a/span'
    __XPATH_DOWNLOAD_CASE_PAPPER = By.XPATH, '//*[@id="icon"]/iron-icon'
    __LINK_MANUAL_PAPPER = By.XPATH, '//*[@id="module-29818"]/div/div/div[2]/div/a/span'
    __ICON_ID_NOTAS = By.ID, 'actionmenuaction-4'

    def __init__(self, driver):
        self.driver = driver 
    
    def login(self, user, password):
        #LOGIN
        self.open_page(self.URL)
        self.fill(self.__EMAIL_TEXTBOX, user)
        self.fill(self.__SENHA_TEXTBOX, password)
        self.click(self.__ACESSAR_BUTTON)
        sleep(3)
    
    def ctt_0031(self):
        #TESTAGEM DE FONTE DE DISLEXIA
        self.click(self.__CONF_ACESS)
        self.click(self.__XPATH_CX_DISLX)
        self.click(self.__XPATH_DISLX_SOP)
        self.click(self.__XPATH_CX_DISLX)

    def ctt_0032(self):
        #SALVAMENTO DA FONTE DE DISLEXIA
        self.click(self.__CONF_ACESSIBILIDADE)
        self.click(self.__XPATH_CX_DISLX)
        sleep(3)
        self.click(self.__XPATH_DISLX_SOP)
        sleep(3)
        self.click(self.__XPATH_CX_DISLX)
        sleep(2)
        pyautogui.moveTo(1280, 394)
        pyautogui.doubleClick()
    
    def ctt_0033(self):
        #TESTAGEM MUDAR IDIOMA DO SISTEMA
        self.click(self.__CLASS_PERFIL)
        self.click(self.__XPATH_PREFERENCIAS)
        self.click(self.__XPATH_IDIOMA_PREFERIDO)
        self.click(self.__XPATH_CX_IDIOMA)
        self.click(self.__XPATH_INGLES)
        self.click(self.__XPATH_CX_IDIOMA)
        self.click(self.__NAME_SAVE_IDIOMA)

    def ctt_0034(self, test_text):
        #TESTAR ENVIAR MENSAGEM PARA SI MESMO
        self.click(self.__XPATH_ICON_MSG)
        self.click(self.__XPATH_MSG_FAV)
        self.click(self.__XPATH_MSG_SELF_USER)
        self.fill(self.__TESTE_SELF_TEXTBOX_, test_text)

    def ctt_0035(self):
        #TESTAGEM DE MENU LATERAL
        self.click(self.__ICON_BARRA_LATERAL)
    
    def ctt_0036(self):
        #ACESSO AOS PARTICIPANTES DA DISCIPLINA
        self.click(self.__LINK_GEST_QUALD_SFT)
        self.click(self.__ICON_BARRA_LATERAL)
        self.click(self.__ICON_PARTICIPANTES)
    
    def ctt_0037(self):
        #PREFERÊNCIAS DE USUÁRIO
        self.click(self.__CLASS_PERFIL)
        self.click(self.__XPATH_PREFERENCIAS)
    
    def ctt_0038(self):
        #DOWNLOAD MANUAL DO CASE
        self.click(self.__LINK_MANUAL_DO_CASE)
        self.click(self.__XPATH_DOWNLOAD_CASE_PAPPER)
        pyautogui.press('Enter')

    def ctt_0039(self):
        #DOWNLOAD DO MANUAL DO PAPPER
        self.click(self.__LINK_MANUAL_PAPPER)
        self.click(self.__XPATH_DOWNLOAD_CASE_PAPPER)
        pyautogui.press('Enter')

    def ctt_0040(self):
        #VISUALIZAÇÃO DE NOTAS
        self.click(self.__CLASS_PERFIL)
        self.click(self.__ICON_ID_NOTAS)
