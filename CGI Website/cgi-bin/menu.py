#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout
import pymysql
import music

def menu(db, cur, form):

	if "mus_id" not in form:
		mus_id = 0
	else:
		mus_id = int(form.getvalue("mus_id"))

	if mus_id == 0:

		if "filter" in form:

			mus_filter = str(form.getvalue("filter"))
			cur.execute("SELECT id, title, genres FROM musicians ORDER BY {};".format(mus_filter))
			data = cur.fetchall()

		elif "search" in form:

			mus_search = str(form.getvalue("search"))
			cur.execute("SELECT id, title, genres FROM musicians WHERE title LIKE %s;", (mus_search))
			data = cur.fetchall()

		else:

			cur.execute("SELECT id, title, genres FROM musicians;")
			data = cur.fetchall()

		print('''<div class="content-wrapper">''')

		if not len(data):

			print('''
				<p class="not-found">There is no <span class="request">'{}'</span> without SUCC!</p>
				<img class="foqu" src="../tmp/foqu.png">
			'''.format(mus_search))

		else:

			print('''
				<div class="search-n-filter">
		            <form class="search" action="engine.py" target="_self" method="get">
		            	<input type="hidden" name="function" value="page">
						<input type="hidden" name="page_id" value="6">
		                <input class="search-input" type="text" name="search" placeholder="Type the name of an artist...">
		                <input class="search-button" type="submit" value="Search">
		            </form>
		            <form class="filter" action="engine.py" target="_self" method="get">
		            	<input type="hidden" name="function" value="page">
						<input type="hidden" name="page_id" value="6">
		                <button class="filter-button" type="submit" name="filter" value="title">
		                    Title
		                </button>
		                <button class="filter-button" type="submit" name="filter" value="origin">
		                    Location 
		                </button>
		                <button class="filter-button" type="submit" name="filter" value="genres">
		                    Genre
		                </button>
		            </form>
		        </div>
			''')

			for item in data:
				print('''<a class="search-item" href="http://g03u32.nn2000.info/cgi-bin/engine.py?function=page&page_id=6&mus_id={}" style="background: url('../tmp/thumb-{}.jpg') center no-repeat; background-size: auto 100%;"><p>{}<br><span>{}</span></p></a>'''.format(item[0], item[1].split(' ')[0], item[1], item[2]))

		print('''</div>''')

	elif mus_id > 0:

		cur.execute("SELECT title FROM musicians WHERE id = {};".format(mus_id))
		page_info = cur.fetchone()

		music.music(db, cur, 6, page_info[0], form, mus_id)