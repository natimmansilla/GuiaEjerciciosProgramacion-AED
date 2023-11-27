__author__ = 'Catedra Algoritmos y Estructuras de Datos'

print("Ejercicio de IMC")

# Titulo y carga de datos
peso=float(input("Ingrese su peso expresado en Kg.:"))
altura=float(input("Ingrese su altura expresada en mts.:"))
mensaje='*' * 50
imc=round(peso/altura**2,2)
mensaje+="\nResultado de IMC: "+str(imc)+"\n"
mensaje+='*' * 50+"\n"


# Procesos
if imc<=16:
    mensaje += "Necesita asistencia de un medico, los riesgos para su salud son muy altos."
elif imc<=17:
    mensaje += "Usted tiene infrapeso, alimentese mas."
elif imc<=18:
    mensaje += "Usted tiene bajo peso, alimentese mejor."
elif imc>18 and imc<=26:
    mensaje += "Usted tiene un peso saludable, continue asi!."
elif imc>26 and imc<30:
    mensaje += "Tiene sobrepeso de grado I, hoy es un buen día para empezar a hacer ejercicios."
elif imc>=30 and imc<=35:
    mensaje += "Tiene obesidad de grado II, necesita el apoyo de un plan nutricional."
elif imc>35 and imc<=40:
    mensaje += "Tiene obesidad grado III (pre-morbida), consulte con su medico los riesgos para su salud."
else:
    mensaje += "Usted tiene obesidad de grado IV (morbida), los riesgos para su salud son muy altos, consulte con su medico a la brevedad."

# Presentacion de Resultados
print(mensaje)