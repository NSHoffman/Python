#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
import pymysql

cgitb.enable()
sys.stderr = sys.stdout


def dataFetch(db, cur, form):

	print ('''
		<div class="left">
			<h2 data-text="Welcum!">Welcum!</h2>
			<p>This portal is dedicated to such sophisticated things as synthwave music and anime!</p>
			<p>Here you can find some pieces of information about best synthwave musicians, listen to their masterpiece songs and become one of us!</p>
			<p>Moreover, whether or not you are registered on the site, you can take part in one of our votings concerning best tracks and musicians! Enjoy!</p>
		</div>
	''')

	print ('''
		<div class="right">
			<form class="regform" action="engine.py" method="post" target="_self">
				<input type="hidden" name="function" value="page">
				<input type="hidden" name="page_id" value="1">
				<input type="text" id="name" name="name" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Nickname'" placeholder="Nickname"><br>
				<input type="text" id="num" name="num" onfocus="this.placeholder = ''" onblur="this.placeholder = 'E-Mail'" placeholder="E-Mail"><br>
				<input type="text" id="year" name="year" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Year of Birth'" placeholder="Year of Birth"><br><br>
				<input type="Submit" value="Sign Up!">
			</form>
			''')

	if form.getvalue("name") and form.getvalue("year") and form.getvalue("num"):

		try:
			a = str(form["name"].value)
			b = str(form["num"].value)
			c = int(form["year"].value)		

			cur.execute("""CREATE TABLE IF NOT EXISTS `users` (
			`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
			`nickname` varchar(255) NOT NULL,
			`email` varchar(255) NOT NULL,
			`year` int(10) unsigned NOT NULL,
			PRIMARY KEY (`id`)
			) ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_general_ci;""")
			db.commit()
			
			cur.execute('''INSERT INTO users (nickname, email, year) VALUES ("{}", "{}", {});'''.format(a, b, c))
			db.commit()
			print('<p class="green">Suckass!</p>')

		except:
			print('<p class="red">Incorrect values given!</p>')		

	else:
		print('<p class="red">Empty Fields!</p>')

	print ('''
		</div>
	''')
