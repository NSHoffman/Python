#!/usr/bin/env python3.4

import os,sys
import time, datetime
import cgi, cgitb 
cgitb.enable()
sys.stderr  =  sys.stdout

import ns1str
import ns2rect
import ns3str
import dataFetch
import visits
import data
import music
import menu

import pymysql


print('''\
Content-type:text/html\r\n
''', end = '')

domen = "g03u32.nn2000.info"
words = ('http://',domen, '/cgi-bin/engine.py')
href_py_file = "".join(words)

qr_string  =  cgi.FieldStorage() 

function = qr_string.getvalue("function")
page_id = qr_string.getvalue("page_id")

if "function" not in qr_string:
	function = "page"
	page_id = 1


try:
	db  =  pymysql.connect(host = "127.0.0.1", user = "g03u32", passwd = "mysql16", db = "g03u32", charset = "utf8",use_unicode = True) # Open database connection
except:
	print('Connection to database has failed!')
	sys.exit(0)


cur  =  db.cursor()

cur.execute("SELECT `page_title`, `page_keywords` FROM `sql_pages` WHERE `page_id` = {};".format( page_id ))
db_one  =  cur.fetchone()

page_title = str(db_one[0])
page_keywords = str(db_one[1])

print('''\
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv = "Content-Type" CONTENT = "text/html; charset = utf-8">
	<title>HOTLINE NYAMI | {} </title>
	<meta name = "keywords" content = "{}">
	<link rel = "stylesheet" href = "../tmp/sk.css">
	<link href="https://fonts.googleapis.com/css?family=Raleway:400,700" rel="stylesheet">
</head>
<body>

'''.format( page_title, page_keywords ), end = '')

visits.visits(db,cur,page_id, page_title, page_keywords)

print('''
<div class="bar">
			<div class="header-content">
				<div class="pendosteam-logo">
					<a href="engine.py">
						<img src="../tmp/img/pteam1.svg" alt="pendosteam-logo">
					</a>
				</div>
				<ul class="top-nav">
''')

cur.execute("SELECT `page_id`,`page_prior_navig`,`page_title` FROM `sql_pages` ORDER BY `sql_pages`.`page_prior_navig` DESC;")
db_all  =  cur.fetchall()

for result in db_all:

	if (int(result[0]) > 4):
		if (int(result[0]) == int(page_id)):
			print ('''
				<li><a data-text="{}" href = "{}?function=page&page_id={}" class = "active">
			'''.format( result[2], href_py_file, result[0] ), sep = '', end = '')
		else:
			print ('''
				<li><a data-text="{}" href = "{}?function=page&page_id={}">
			'''.format( result[2], href_py_file, result[0] ), sep = '', end = '')

		print("{}</a></li>".format( result[2] ), end = '')

print(''' 
				</ul>
			</div>
</div>
''')

print('''
		<div class="main-wrapper">
''')

with open('../tmp/header.html', mode='r', encoding="utf-8", errors=None) as f_read:
	for line in f_read: print (line)

print ('''
			<div class="body-wrapper">
''')

if (function == "page"):

	cur.execute("SELECT page_id FROM sql_pages;")
	pages = cur.fetchall()

	pageList = []

	for i in pages:
		pageList.append( i[0] )

	if (int(page_id) == 1):

		dataFetch.dataFetch(db, cur, qr_string)

	elif (int(page_id) == 2):

		ns1str.lab1(qr_string)

	elif (int(page_id) == 3):

		ns2rect.lab2(qr_string)

	elif (int(page_id) == 4):

		ns3str.lab3(qr_string)

	elif (int(page_id) == 5):

		data.dataGet(db, cur)

	elif (int(page_id) == 6):

		menu.menu(db, cur, qr_string)

	elif (int(page_id) > 6):
		for i in pageList:
			if (int(page_id) == i):
				cur.execute("SELECT `page_content` FROM `sql_pages`  WHERE `page_id` = {};".format( page_id ))
				db_one  =  cur.fetchone()
				page_content = db_one[0]
				print(page_content, end = '')

print ('''
			</div>
''')

with open('../tmp/footer.htm', mode='r', encoding="utf-8", errors=None) as f_read:
	for line in f_read: print (line)

print ('''
		</div>
	</body>
</html>
''')

db.close()