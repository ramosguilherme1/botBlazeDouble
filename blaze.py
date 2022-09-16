import requests
from bs4 import BeautifulSoup

documento = requests.get("https://kitblaze.com/double/?visitante=home")

html_doc = BeautifulSoup(documento.text, 'html.parser') #html inteiro do site
ultimos_giros = html_doc.find_all('div',{'class':'giro-img'}) #variavel lista c/ ult 100 giros
dict_cores = {'0':'B','1':'V','2':'V','3':'V','4':'V','5':'V','6':'V','7':'V','8':'P','9':'P','10':'P','11':'P','12':'P','13':'P','14':'P'}
cores = []
numeros = []

for giro in ultimos_giros: #passar por cada um dos 100
    numero = giro.find('span')
    if numero:
        numero_atual = (numero.text)
        cor = dict_cores[numero.text]
        numeros.append(numero_atual)
        cores.append(cor)
    else:
        cores.append('B')
        numeros.append(0)

numeros.reverse()

print('-'*100)
print("Ultimos giros Blaze Double".center(100))
print('-'*100)
print(f"Branco....:{cores.count('B')}%")
print(f"Preto.....:{cores.count('P')}%")
print(f"Vermelho..:{cores.count('V')}%")
print('-'*100)
print(numeros)

#Estrategia para o numero 5
win = 0
g1 = 0
g2 = 0
loss = 0

for posicao,numero in enumerate(numeros):
    if numero == '5':
        try:
            if dict_cores[numeros[posicao+4]] == 'V':
                win+=1
            elif dict_cores[numeros[posicao+5]] == 'V':
                g1+=1
            elif dict_cores[numeros[posicao+6]] == 'V':
                g2+=1
            else:
                loss+=1
        except:
            pass

print('-'*100)
print("Estratégia para o número 5")
print(f'Win->{win} G1->{g1}  G2->{g2}  Loss->{loss}')

#Estrategia para o numero 6
win = 0
g1 = 0
g2 = 0
loss = 0

for posicao,numero in enumerate(numeros):
    if numero == '6':
        try:
            if dict_cores[numeros[posicao+5]] == 'V':
                win+=1
            elif dict_cores[numeros[posicao+6]] == 'V':
                g1+=1
            elif dict_cores[numeros[posicao+7]] == 'V':
                g2+=1
            else:
                loss+=1
        except:
            pass

print('-'*100)
print("Estratégia para o número 6")
print(f'Win->{win} G1->{g1}  G2->{g2}  Loss->{loss}')

#Estrategia para o numero 7
win = 0
g1 = 0
g2 = 0
loss = 0

for posicao,numero in enumerate(numeros):
    if numero == '7':
        try:
            if dict_cores[numeros[posicao+6]] == 'V':
                win+=1
            elif dict_cores[numeros[posicao+7]] == 'V':
                g1+=1
            elif dict_cores[numeros[posicao+8]] == 'V':
                g2+=1
            else:
                loss+=1
        except:
            pass        

print('-'*100)
print("Estratégia para o número 7")
print(f'Win->{win} G1->{g1}  G2->{g2}  Loss->{loss}')