#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout

def lab1(form):

	print ('''
		<div class="left">
			<h3>Павловская (393). Строки.</h3>
			<p><span class="bold">Вариант 20</span><br>
	Написать программу, которая считывает текст <span class="bold">(макс. 2000 знаков)</span> из файла и выводит на экран
	предложения, содержащие максимальное количество знаков пунктуации.</p>
			<h3>Порядок реализации:</h3>
			<ol style="font-family: sans-serif; font-size: 0.9em; padding: 0 0 0 1.5em;">
				<li>Проверка формы на наличие данных с использованием <span class="imp">if getvalue()</span>.</li>
				<li>Загрузка полученных данных.</li>
				<li>Проверка соответствия длины текста максимально возможному объему при помощи <span class="imp">if len() < 2000</span>.</li>
				<li>Вывод исходного текста.</li>
				<li>Подсчет количества знаков препинания в каждом предложении.</li>
				<li>Сохранение данных о количестве знаков препинания в списке <span class="imp">Counter</span>.</li>
				<li>Выбор наибольшего значения в списке и сопоставление его с индексом предложения.</li>
				<li>Вывод полученной информации.</li>
			</ol>
		</div>
	''')

	print ('''
		<div class="right">
			<form class="regform" action="engine.py" target="_self" method="get">
				<input type="hidden" name="function" value="page">
				<input type="hidden" name="page_id" value="2">
				<input type="text" name="path" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Enter the filepath'" placeholder="Enter the filepath"><br><br>
				<input type="Submit" value="Submit">
			</form>
	''')

	if form.getvalue("path"):

		try:
			filepath = str(form["path"].value)
			n = 1
			counter = []

			f = open(filepath,'r', encoding="utf-8")
			f_read = f.read()

			if len(f_read) < 2000:

				print("<h3>Исходный текст:</h3>")
				print('''<p>{}</p>'''.format(f_read))
				f.close()
				
				s = open(filepath,'r', encoding="utf-8")
				strcopy = (s.read().replace("!","."))
				strcopy = strcopy.replace("?",".")
				strcopy = strcopy.split(".")
				del strcopy[-1]
				for sent in strcopy:
				        for sign in sent:
				                if sign in '"#$%&\'()*+,-/:;<=>@[\\]^_`{|}~':
				                        n += 1
				                else:
				                        continue
				        counter.append(n)
				        n = 1
				for i, x in enumerate(counter):
				        if x == max(counter):
				        		print("<h3>Предложение с наибольшим количеством пунктуационных знаков:</h3>")
				        		print('''<p><span class="bold">Предложение №{}</span> : {}. <span class="bold">({} знаков)</span></p>'''.format(i+1, strcopy[i], max(counter)))
				s.close()

			else:
				print('<p class="red">Объем текста не должен превышать 2000 знаков!</p>')

		except:
			print('<p class="red">Файл не найден! Убедитесь в том, что ваш путь не содержит кириллических символов!</p>')
	else:
		print('<p class="red">Есть пустые поля!</p>')

	print('''
		</div>
	''')