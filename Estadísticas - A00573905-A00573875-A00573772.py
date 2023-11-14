animenor2 = 0
anim2amenor5 = 0
anim5amenor10 = 0
animasoigual10 = 0
totalanimales = 0
condicion = input("Hay algún animal a registar? ").lower()
while condicion == "si":
  totalanimales += 1
  edad = float(input("Escribe la edad del animal en años. "))
  if edad < 2 :
      animenor2 += 1
  elif edad >= 2 and edad < 5:
      anim2amenor5 += 1
  elif edad >= 5 and edad < 10:
      anim5amenor10 += 1
  elif edad >= 10:
      animasoigual10 += 1
  condicion = input("Hay algún animal a registrar? ").lower()

print("El total de animales es:", totalanimales)
print("El total de animales menores a dos años de edad es:", animenor2)
print("El total de animales de entre 2 y menos de 5 años es:",anim2amenor5)
print("El total de animales de entre 5 y menos de 10 años es:",anim5amenor10)
print("El total de animales de 10 y más, muchos más es:",animasoigual10)
