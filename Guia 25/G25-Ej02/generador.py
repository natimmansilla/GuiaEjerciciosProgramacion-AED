__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random


def generar_archivo_csv():
	nombres = ['Marcelo Tinelli', 'Susana Gimenez', 'Mirtha Legrand', 'Juana Viale', 'Mariana Fabbiani',
	           'Jorge Rial', 'Guillermo Andino', 'Alejandro Fantino', 'Luciano Pereyra', 'Soledad Pastorutti',
	           'Sebastian Yatra', 'Tini Stoessel', 'Lali Esposito', 'Jimena Baron', 'Paulo Londra',
	           'Carolina Ardohain', 'Nicole Neuman', 'Paula Chaves', 'Valeria Mazza', 'Abel Pintos',
	           'Trueno', 'LGante', 'Maria Becerra', 'Nicki Nicole', 'Rusherking']
	m = open('invitados.csv', 'wt')
	for nombre in nombres:
		mesa = random.randrange(13)
		ong = random.randrange(10)
		monto = random.randrange(1000, 10000, 100)
		m.write('{},{},{},{}\n'.format(nombre, mesa, ong, monto))
	m.close()


if __name__ == '__main__':
	generar_archivo_csv()
