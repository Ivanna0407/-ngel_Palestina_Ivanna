#Lenia Palestina Medina Nicasio
#Ivanna Martinez de Alba
#Ángel Saúl Hernandez Vidales
import random
thislist=[]
estado=True
print("Este es un porgrama que hace contraseñas")
while len(thislist)<8:
  c=input("Dime un de los caracteres de tu contraseña")
  if c=="!" or c=="¡" or c=="." or c=="-" or c=="_" or c=="/" or c=="#" or c=="$" or c=="%" or c=="(" or c==")" or c=="*" or c=="+" or c==">" or c=="<" or c==";" or c==",":
    print("No es valido")
  elif c.isdigit or c.isalpha:
    thislist+=c
pas="".join(thislist)

print("Tu contraseña es: ",pas)
while estado==True:
  r=input("Dime tu contraseña")
  if r==pas:
    print("Tu contraseña es correcta")
    estado=False
  else:
    print("Contraseña incorrecta")
    print("intenta de nuevo")
