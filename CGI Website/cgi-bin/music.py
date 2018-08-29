#!/usr/bin/env python3.4

import os,sys
import cgi, cgitb
cgitb.enable()
sys.stderr = sys.stdout
import pymysql

def music(db, cur, page_id, artist, form, mus_id):

	cur.execute("SELECT name, origin, genres, years, biography FROM musicians WHERE title = %s;", (artist))

	page_content = cur.fetchone()

	name = str(page_content[0])
	origin = str(page_content[1])
	genres = str(page_content[2])
	years = str(page_content[3])
	bio = str(page_content[4])

	print ('''
		<div id="prev">
			<div id="description">
				<div id="list-info">
					<p><span>Name:</span> {}</p>
					<p><span>Origin:</span> {}</p>
					<p><span>Genres:</span> {}</p>
					<p><span>Years:</span> {}</p>
				</div>
			</div>
			<div id="prev-bg" style="background: fixed url('../tmp/{}.jpg') center top no-repeat;"></div>
		</div>
	'''.format(name, origin, genres, years, artist.split(' ')[0]))


	print('''
		<div class="left">
			<h2>{}</h2>
			<h3>Information</h3>
			<p>{}</p>
		</div>
		<div class="right">
			<div id="rate" style="background: url('../tmp/thumb-{}.jpg') center center no-repeat; background-size: auto 100%">
				<div id="info-frame">
					<form id="like" method="post" target="_self" action="engine.py">
						<input type="hidden" name="mus_id" value="{}">
						<input type="hidden" name="function" value="page">
						<input type="hidden" name="page_id" value="{}">
						<input type="hidden" name="artist" value="{}">
						<input type="hidden" name="rate" value="like">
						<input type="submit" value="Like">
					</form>
					<form id="dislike" method="post" target="_self" action="engine.py">
						<input type="hidden" name="mus_id" value="{}">
						<input type="hidden" name="function" value="page">
						<input type="hidden" name="page_id" value="{}">
						<input type="hidden" name="artist" value="{}">
						<input type="hidden" name="rate" value="dislike">
						<input type="submit" value="Dislike">
					</form>
	'''.format(artist, bio, artist.split(' ')[0], mus_id, page_id, artist, mus_id, page_id, artist))

	if form.getvalue("rate"):

		rate = form.getvalue("rate")

		cur.execute("INSERT INTO ratings (artist, rate) VALUES (%s, %s);", (artist, rate))
		db.commit()

	cur.execute("SELECT COUNT(rate) FROM ratings WHERE rate = 'like' AND artist = %s;", (artist))
	likes = int(cur.fetchone()[0])

	cur.execute("SELECT COUNT(rate) FROM ratings WHERE rate = 'dislike' AND artist = %s;", (artist))
	dislikes = int(cur.fetchone()[0])

	total = dislikes + likes

	try:
		rating = round(likes/total * 100)
	except ZeroDivisionError:
		rating = 0

	print('''
					<div id="info-ratings">
						<span>Likes: </span> {}<br>
						<span>Dislikes: </span> {}<br>
						<span>Rating: </span> {}%<br>
					</div>
				</div>
				<div id="stat-bar" style="width: {}%"></div>
			</div>
	'''.format(likes, dislikes, rating, rating))

	print('''
			<div id="music">
				<h3>Best Songs</h3>
	''')

	cur.execute("SELECT name, link FROM songs WHERE artist = %s;", (artist))

	list_songs = cur.fetchall()

	for song in list_songs:
		print('''
			<div class="song">
				<p class="song-caption">{}</p>
				<audio src="{}" controls preload="metadata"></audio>
			</div>
		'''.format( song[0], song[1] ))

	print('''
			</div>
		</div>
	''')
