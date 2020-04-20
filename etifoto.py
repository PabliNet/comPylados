#!/usr/bin/python3
import locale
from sys import argv
from os import name
from os.path import exists
from mimetypes import guess_type
from datetime import datetime
from exif import Image

locale.setlocale(locale.LC_ALL, "")

def nombre (clave='', ayuda=False):
	dic = {
		'rmp': 'Resolución',
		'ancho': 'Ancho de la fotografía',
		'alto': 'Alto de la fotografía',
		'mp': 'Megapíxeles',
		'mym': 'Marca y modelo del equipo',
		'marca': 'Marca del equipo',
		'modelo': 'Modelo del equipo',
		'iso': 'ISO',
		'expo': 'Tiempo de exposición',
		'focal': 'Distancia focal',
		'f': 'Apertura',
		'balance': 'Balance de blancos',
		'fyh': 'Fecha y hora',
		'fecha': 'Fecha',
		'hora': 'Hora'
	}
	if ayuda:
		for tag in list(dic.keys()):
			if tag in ('marca', 'expo', 'focal', 'f', 'fecha', 'hora'):
				dic[tag] = 'la ' + dic[tag].lower()
			elif tag == 'iso':
				dic[tag] = 'la ' + dic[tag]
			elif tag == 'mp':
				dic[tag] = 'los ' + dic[tag].lower()
			else:
				dic[tag] = 'el ' + dic[tag].lower()
	if clave:
		return dic[clave]
	else:
		return dic

def etiquetas ():
	resol = (imagen.pixel_x_dimension, imagen.pixel_y_dimension, int(round(imagen.pixel_x_dimension * imagen.pixel_y_dimension / 1000000, 0)))
	return {
		'rmp': str(resol[0]) + ' píxeles \u00D7 ' + str(resol[1]) + ' píxeles (' + str(resol[2]) + 'MP)',
		'ancho': imagen.pixel_x_dimension,
		'alto': imagen.pixel_y_dimension,
		'mp': resol[2],
		'mym': imagen.make + ' ' + imagen.model,
		'marca': imagen.make,
		'modelo': imagen.model,
		'iso': imagen.photographic_sensitivity,
		'expo': imagen.exposure_time,
		'focal': imagen.focal_length,
		'f': imagen.f_number,
		'balance': manual[imagen.white_balance],
		'fyh': datetime.strftime(datetime.strptime(imagen.datetime_original, '%Y:%m:%d %H:%M:%S'), '%a, %-d-%b-%Y %H:%M:%S'),
		'fecha': datetime.strftime(datetime.strptime(imagen.datetime_original, '%Y:%m:%d %H:%M:%S'), '%a, %-d-%b-%Y'),
		'hora': datetime.strftime(datetime.strptime(imagen.datetime_original, '%Y:%m:%d %H:%M:%S'), '%a, %H:%M:%S'),
	}


manual = ('Auto', 'Manual')

if exists(argv[-1]) and guess_type(argv[-1], strict=True)[0].split('/')[1] == 'jpeg':
	with open(argv[-1], 'rb') as Imagen:
		imagen = Image(Imagen)

		tags = etiquetas()
elif not exists(argv[-1]) and not '--help' in argv[1:]:
	print (f'El archivo {argv[-1]} no existe.')
	exit()
elif not '--help' in argv[1:]:
	print ('No es formato Joint Photographic Experts Group')
	exit()

if (len(argv) == 2 and argv[1] == '--help') or len(argv) == 3:
	ltags = list(nombre(ayuda=True).keys())
	for tag in ('rmp', 'mym', 'fyh'):
		ltags.remove(tag)

if len(argv) == 2:
	if not argv[1] == '--help':
		for tag in tags:
			if not tag in ('ancho', 'alto', 'mp', 'marca', 'modelo', 'fecha', 'hora'):
				print (format('\x1b[32m\x1b[1m' + nombre(tag) + ':', '<35'), '\x1b[0m' + str(tags[tag]))
	else:
		print (f'Modo de empleo: {argv[0]} [OPCIÓN\u2026] imagen.jpg')
		print ('Muestra las etiquetas Exif.')
		for tag in ltags:
			sng = ' ' * 2
			fmt = '<31'
			print (sng, format('-' + tag, fmt) + 'Muestra', nombre(tag, True))
		print ('\nOpciones de ayuda')
		print (sng, format('-' + tag, fmt) + 'Muestra este mensaje de ayuda.')

elif len(argv) == 3:
	if argv[1][:1] == '-' and argv[1][1:] in ltags:
		print (tags[argv[1][1:]])