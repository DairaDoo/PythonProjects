# aquí se usa regex que es un formato para pedir información, en este caso buscamos 5 decimales con \d, si no se encunetran devuelve none, si es
# encontrado devuelve match object.
import re
codigo_cinco_digitos = "12345"
codigo_nueve_digitos = "12345-6789"
numero_telefono = "123-456-7890"

regex_cinco_digitos = r'\d{5}' #regex de cinco digitos
print(re.search(regex_cinco_digitos, codigo_cinco_digitos))
print(re.search(regex_cinco_digitos, codigo_nueve_digitos))
print(re.search(regex_cinco_digitos, numero_telefono))