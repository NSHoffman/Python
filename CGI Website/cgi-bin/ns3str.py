#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout


def lab3(form):

	print ('''
		<div class="left">
			<h3>Хахаев (58). Массивы.</h3>
			<p><span class="bold">Вариант 28</span><br>
	Заданы M строк символов, которые вводятся с клавиатуры. Каждая строка содержит слово. Записать каждое слово в разрядку (вставить по пробелу между буквами).</p>
			<h3>Порядок реализации:</h3>
			<ol style="font-family: sans-serif; font-size: 0.9em; padding: 0 0 0 1.5em;">
				<li>Проверка формы на наличие данных с использованием <span class="imp">if getvalue()</span></li>
				<li>Загрузка полученных данных.</li>
				<li>Вывод исходных данных для сравнения с полученным результатом.</li>
				<li>Разбиение строк по буквам при помощи <span class="imp">list()</span>.</li>
				<li>Вставка пробелов между буквами при помощи <span class="imp">" ".join()</span>.</li>
				<li>Вывод результата.</li>
			</ol>
		</div>
	''')

	print ('''
		<div class="right">
			<form class="regform" action="" target="_self" method="get">
				<input type="hidden" name="function" value="page">
				<input type="hidden" name="page_id" value="4">
	            <input type="text" name="x1" onfocus="this.placeholder = ''" onblur="this.placeholder = 'First line'" placeholder="First line"><br>
	            <input type="text" name="x2" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Second line'" placeholder="Second line"><br>
	            <input type="text" name="x3" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Third line'" placeholder="Third line"><br><br>
	            <input type="Submit" value="Submit">
	        </form>
			''')

	form = cgi.FieldStorage()

	if form.getvalue("x1") and form.getvalue("x2") and form.getvalue("x3"):

		a = str(form["x1"].value)
		b = str(form["x2"].value)
		c = str(form["x3"].value)

		print("<h3>Исходные строки:</h3>")
		print("<p>1. {}</p>".format(a))
		print("<p>2. {}</p>".format(b))
		print("<p>3. {}</p>".format(c))

		print("<h3>Итоговые строки:</h3>")
		print('''<p>{}</p>'''.format(" ".join(list(a))))
		print('''<p>{}</p>'''.format(" ".join(list(b))))
		print('''<p>{}</p>'''.format(" ".join(list(c))))

	else:
		print('<p class="red">Есть пустые поля!</p>')

	print ('''
		</div>
	''')