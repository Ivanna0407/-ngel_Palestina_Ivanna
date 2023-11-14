#Objetivo: Algoritmo para calcular el suelo de "n" vendedores 
vendedores=0
sueldo=0
flag=1
while flag==1:
  vendedor=input("¿Hay otros vendedores?(si,no)").lower()
  print("")
  if vendedor!="si":
    break
  else: 
    nombre_vendedor=input("Inserta el nombre del vendedor:")
    print("")
    salario_base=float(input("Inserta el salario base del vendedor:"))
    ventas=float(input("Inserta el total de ventas del vendedor:"))
    if ventas<3500:
      comision=0.07*ventas
    elif 3500<=ventas<=7000:
      comision=0.10*ventas
    else: 
      comision=0.15*ventas
    
    subtotal=(salario_base+comision)
    
    vendedores +=1
    sueldo+=subtotal
    
    print("")
    print(f"Nombre del vendedor:{nombre_vendedor}")
    print(f"Salario total:{sueldo}")

  
  
