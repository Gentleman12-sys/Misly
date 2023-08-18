from django.shortcuts import render, redirect
import random

a = set()
for i in range(10, 100):
    a.add(i - (int(str(i)[0]) + int(str(i)[1])))

def index(request):
    if request.method == 'POST':
        return redirect('pokaz')
    gifs = [f'https://mindreader.hacktest.net/{i}.gif' for i in range(1, 27)]
    request.session['gifs'] = gifs
    main = random.choice(request.session['gifs'])
    gifs.remove(main)
    request.session['main'] = main
    tables = []
    table = []
    a = list(range(0, 100))
    random.shuffle(a)
    for el, i in enumerate(a):
        if i%9 == 0:
            table.append('<td class="nymtd">{}</td><td class="symtd"><img src="{}" width="32" height="32"></td>'.format(i, request.session['main']))
        else:
            table.append('<td class="nymtd">{}</td><td class="symtd"><img src="{}" width="32" height="32"></td>'.format(i, random.choice(request.session['gifs'])))
        if el%10 == 0 and el != 0:
            tables.append(f"<tr>{''.join(table)}</tr>")
            table = []
    tables = ''.join(tables)
    return render(request, 'index.html', {'tables': tables})

def pokaz(request):
    if request.session.get('main'):
        a = request.session['main']
        del request.session['main']
        return render(request, 'pokaz.html', {'main': a})
    else:
        return redirect('index')