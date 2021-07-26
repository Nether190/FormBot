from selenium import webdriver
import time
import codecs
from tkinter import messagebox, Tk

browser = webdriver.Chrome('chromedriver')
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSf8IpgwW4DcIsvrKMp-UhffOTP5MMiSCd5ttxVvK6pFXXbwCA/viewform')

time.sleep(1.5)
    
with codecs.open('dados.txt', encoding='utf-8', mode='r') as ler:
    Dados = ler.read().splitlines()

Email = Dados[0]
Nome = Dados[1]
Numero = Dados[2]
Turma = Dados[3]
Grupamento = Dados[4]
Aula = Dados[6]

idBotao = {'301':17, '302':20, '303':23, '304':26, '305':29, "A":36,"B":39}

idCaixa = {
"Geografia":3,
"História":4,
"Matemática":5,
"literatura":6,
"Biologia":7,
"Arte":8,
"Educação física":9,
"Português":10,
"Sociologia":11,
"Filosofia":12,
"Química":13,
"Física":14,
"Redação":15,
"Inglês":16,
"Espanhol":17}


inputEmail = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
inputEmail.send_keys(Email)


inputNome = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
inputNome.send_keys(Nome)


inputNumero = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
inputNumero.send_keys(Numero) 


inputTurma = browser.find_element_by_xpath(f'//*[@id="i{idBotao.get(Turma)}"]/div[3]/div')
inputTurma.click()


inputGrupamento = browser.find_element_by_xpath(f'//*[@id="i{idBotao.get(Grupamento)}"]/div[3]/div')
inputGrupamento.click()


inputAula = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[1]/div[1]')
inputAula.click()

abcd = idCaixa.get(Aula)
print(abcd)

time.sleep(0.5)
try:
    inputAula = browser.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]/div[{idCaixa.get(Aula)}]/span')
except: 
    Tk().withdraw()
    messagebox.showerror('Erro', 'Nenhuma aula encontrada')
    browser.quit()
    exit()

    
inputAula.click()

time.sleep(2)

enviar = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[3]/div/div/span')
enviar.click()




