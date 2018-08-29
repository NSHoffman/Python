#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
import pymysql
import pie

cgitb.enable()
sys.stderr = sys.stdout


def dataGet(db, cur):

	print ('''
		<div class="right">
			<h3>M33t da Crew!</h3>
	''')

	try:

		cur.execute("SELECT nickname, email FROM users ORDER BY nickname;")
		db_all  =  cur.fetchall()

		print('<table class="user-list">')
		print('''
			<tr>
				<th>Псевдоним</th><th>E-Mail</th>
			</tr>
		''')
		for row in db_all:
			print('<tr>')
			for item in row:
				print('<td>{}</td>'.format(item))
			print('</tr>')
		print('</table>')

	except:
		print('<p class="red">SpyWare has foked up!(((9</p>')

	print ('''
		</div>
	''')

	print ('''
		<div class="left">
			<h3>PendoSpyWare v1337</h3>
	''')

	try:

		cur.execute("SELECT page_title, page_ip, page_date, page_time FROM py_page_visits ORDER BY id DESC LIMIT 15;")
		db_all  =  cur.fetchall()

		print('<table class="spy">')
		print('''
			<tr>
				<th>Страница</th><th>IP-Адрес</th><th>День</th><th>Время</th>
			</tr>
		''')
		for row in db_all:
			print('<tr>')
			for item in row:
				print('<td>{}</td>'.format(item))
			print('</tr>')
		print('</table>')

	except:
		print('<p class="red">Data has foked up!(((9</p>')

	print('''
		</div>
	''')

	pie.pie()
