
import cgi, cgitb
cgitb.enable()
#import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
#import matplotlib.patches

def pie():
    
    pages = []
    visits = []
    colors = [
        '#5d69d8',
        '#d85d5d',
        '#d85db4',
        '#8b5dd8',
        '#5dd8a0',
        '#88e074',
        '#b6e074',
        '#e0dc74',
        '#e0a274'
    ]

    with open('../tmp/frequencies.txt', mode='r', encoding="utf-8") as f_read:
        for line in f_read.readlines():
            words = line.strip().split(",")
            pages.append( str(words[1]) )
            visits.append( int(words[2]) )


    dpi = 300
    fig = plt.figure(dpi = dpi, figsize = (1920 / dpi, 1440 / dpi) )
    mpl.rcParams.update({'font.size': 7, 'edgecolor' : 'white'})

    plt.pie(visits, autopct="%.1f%%", labels = pages, radius = 1, colors = colors, shadow = True)
    fig.savefig('../tmp/pie.png')

    print('''
        <div class="pie">
            <img src="../tmp/pie.png" alt="pie chart with page visitings stats">
        </div>
    ''')


