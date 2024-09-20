import pywhatkit
import os
from dotenv import load_dotenv
load_dotenv()
idgrupo = os.getenv("CODGRUPO")
x = 1

lista = [['Grafiato', 'Ultrablack', 12.5], ['Laufen', 'Ultrablack', 14.5]]

y = ['Slide', 'Ultrablack', 17.8]

lista.append(y)

x = len(lista) - 1 #contador

print(f'{lista[x][0]} na cor {lista[x][1]} possui {lista[x][2]} disponíveis\n{lista[x-1][0]} na cor {lista[x-1][1]} possui {lista[x-1][2]} disponíveis')




# pywhatkit.sendwhatmsg_to_group_instantly(idgrupo, f"A quantidade disponível no tecido para a cor '' é: ")
