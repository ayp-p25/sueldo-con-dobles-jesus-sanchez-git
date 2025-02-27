A = float(input("Ingrese las horas trabajadas: \n"))
B = float(input("Ingrese el sueldo por hora : \n"))
 
if A>48:
    HE = A -48
    Pe = HE*(2*B)
    HN = 48
else:
    HE = 0
    Pe = 0
    HN = A
Total = (HN*B)+Pe
print("El total de horas extra fueron : ", HE)
print("Sueldo por horas extra : ", Pe)
print("Su pago total fue : ", Total)