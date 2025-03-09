"""8. Crie um programa em Linguagem Python que solicite a palavra-passe de um utilizador e
depois peça para digitar a palavra-passe novamente, até que as duas palavras-passe sejam
correspondentes (iguais).
Exemplo de saía do terminal:
Insira a sua palavra-passe:
--> 1234
Digite novamente:
-->12345
As palavras-passe introduzidas são diferentes.
Introduza nova palavra-passe:
-->123
Digite novamente:
-->123
As palavras-passe correspondem!"""


senha1 = input("Insira a sua palavra-passe: \n")
senha2 = input("Digite novamente: \n")

if senha1 != senha2:
    print("As palavras-passe introduzidas são diferentes. Introduza nova palavra-passe:")
    senha1 = input("Insira a nova palavra-passe: \n")
    senha2 = input("Digite novamente: \n")

if senha1 == senha2:
    print("As palavras-passe correspondem!")
else:
    print("As palavras-passe ainda não correspondem. Tente novamente.")

