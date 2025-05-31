name = input ("ingresa el nombre ")
mail= input("ingresa el mail")
birthdate= int(input("ingresa fehca de nacimiento"))
password =input('ingresa el password')

meesage=f"""
Nombre:{name}
Email {mail}
tendras 55 años en el {-(2025-birthdate)+55+2025}
tu contraseña es {"*"*len(password)}
"""
print(meesage)