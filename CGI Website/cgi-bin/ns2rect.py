#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout


def lab2(form):

	print ('''
		<div class="left">
			<h3>Хахаев (46). Алгоритмы.</h3>
			<p><span class="bold">Вариант 18</span><br>
	Даны вещественные положительные числа a, b, c, d <span class="bold">(от 0 до 250)</span>. Выясните, может ли прямоугольник со сторонами c, d уместиться внутри прямоугольника со сторонами a, b так, чтобы каждая сторона внутреннего прямоугольника была параллельна или перпендикулярна стороне внешнего прямоугольника</p>
			<h3>Порядок реализации:</h3>
			<ol style="font-family: sans-serif; font-size: 0.9em; padding: 0 0 0 1.5em;">
				<li>Проверка формы на наличие данных с использованием <span class="imp">if getvalue()</span></li>
				<li>Загрузка полученных данных.</li>
				<li>Проверка соответствия введенных величин требованиям.</li>
				<li>Сравнение сторон прямоугольников.</li>
				<li>Вывод результата в графическом (с помощью <span class="imp">div</span> элементов соответствующих размеров) и текстовом варианте.</li>
			</ol>
		</div>
	''')

	print ('''
		<div class="right">
			<form class="regform" action="engine.py" target="_self" method="get">
				<input type="hidden" name="function" value="page">
				<input type="hidden" name="page_id" value="3">
	            <h4>First Rectangle</h4>
	            <input type="text" name="x1" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Width'" placeholder="Width"><br>
	            <input type="text" name="y1" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Height'" placeholder="Height"><br>
	            <h4>Second Rectangle</h4>
	            <input type="text" name="x2" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Width'" placeholder="Width"><br>
	            <input type="text" name="y2" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Height'" placeholder="Height"><br><br>
	            <input type="Submit" value="Submit">
	        </form>
			''')

	form = cgi.FieldStorage()

	if form.getvalue("x1") and form.getvalue("y1") and form.getvalue("x2") and form.getvalue("y2"):

		try:
			a = int(form["x1"].value)
			b = int(form["y1"].value)
			c = int(form["x2"].value)
			d = int(form["y2"].value)

			if (a > 250 or b > 250 or c > 250 or d > 250) or (a <= 0 or b <= 0 or c <= 0 or d <= 0):
				print('<p class="red">Стороны должны быть от 1 до 250!</p>')
			else:
				if a > c and b > d:
				        print('<p class="green">Прямоугольник со сторонами C,D умещается в прямоугольник со сторонами A,B!</p>')
				else:
				        print('<p class="red">Прямоугольник со сторонами C,D больше прямоугольника со сторонами A,B!</p>')
				print('''
				<div class="frame" style="height: 275px; width: 100%; border: 2px solid black; position: relative; margin: 15px 0;">
					<div class="rect1" style="height: {}px; width: {}px; border: 2px dashed #ff4646; position: absolute; bottom: 10px; left: 50px;"></div>
					<div class="rect2" style="height: {}px; width: {}px; border: 2px solid black; position: absolute; bottom: 10px; left: 50px;"></div>
				</div>
				'''.format(b,a,d,c))
		except:
			print('<p class="red">Некорректные значения! Убедитесь в том, что вы используете только числа!</p>')
	else:
		print('<p class="red">Есть пустые поля!</p>')

	print('''
		</div>
	''')