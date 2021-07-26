from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter
from time import strftime
import codecs

wb = load_workbook('horario.xlsx')
ws = wb.active

tabela = {'Mon':1,'Tue':4,'Wed':7,'Thu':10,'Fri':13}

hora = int(strftime('%H%M'))
dia = strftime('%a')

with codecs.open('dados.txt', encoding='utf-8', mode='r') as ler:
    Dados = ler.read().splitlines()

Camil = Dados[5]

diaHora = tabela.get(dia)
if Camil: diaAula = diaHora+1
else: diaAula = diaHora+2



def compara_hora(CH,CA,C,F):
    letra = get_column_letter(CH)
    aula = get_column_letter(CA)
    for row in range(C,F+1):
        valor = ws[letra+str(row)].value
        if hora <= valor:
            return(ws[aula+str(row-1)].value)
        else: pass


aulaAtual = compara_hora(diaHora,diaAula,2,11).encode('utf-8')


with  open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()

if len(linhas) == 7:
    del linhas[6]

with open("dados.txt", "w+") as arquivoNovo:
    for linha in linhas:
        arquivoNovo.write(linha)

with open('dados.txt', 'ab') as nota:
    nota.write(aulaAtual)