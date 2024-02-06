#reto python dia lunes
#autor jgcv
# Nombre(s)
# Apellidos
# Número de teléfono
# Correo electrónico.


def datos():

    name = input("Nombre: ")
    last_name = input("Apellido: ")
    phone = input("Telefono: ")
    email = input("Correo: ")
    saludo ="Hola " + name + last_name + ', en breve recibiras un correo a ' + email +'@email.com'
    print(saludo)


def main():
    datos()


print(main())
