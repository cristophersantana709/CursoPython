P_colombianos=int(input("Ingresar los pesos colombianos: "))
S_peruanos=int(input("Ingresar los soles peruanos: "))
R_brasileños=int(input("Ingresar los reales brasileños: "))

Dolares1= P_colombianos * 4022.81
Dolares2= S_peruanos * 0.27
Dolares3= R_brasileños * 0.18
 
Resultado= Dolares1+Dolares2+Dolares3
print("Resultado en dolares: ",Resultado)
