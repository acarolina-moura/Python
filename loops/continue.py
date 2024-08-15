"""Continue é usado para continuar o loop /  Pula para a próxima iteração
No caso do código se a condição "m" for encontrada, sai do for, executa o else
Mas CONTINUE iterando o loop 

Ou seja, modifica o fluxo do loop"""


names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
 
for name in names:
  if 'm' in name.lower():
      continue
  else:
      print(name)