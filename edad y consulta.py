#Edad y consulta#
edad = int(input("Ingrese su edad: "))
producto = int(input("Ingrese la cantidad de articulos comprados: "))
edad = edad > 18
producto = producto > 1
resultado = edad and producto
print(f"¿La persona es mayor de 18 años y compró más de 1 artículo?: {resultado}")