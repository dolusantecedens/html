import random
from tkinter import E
class film:
    def __init__ (self, title, year, type, watched):
        self.title=title
        self.year=year
        self.type=type
        self.watched=watched
    def __str__(self):
        return f'{self.title} ({self.year})'
    @property
    def play(self):
        self.watched+=1
class serial(film):
    def __init__ (self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode=episode
        self.season=season
    def __str__(self):
        if int(self.episode)<10 and int(self.season)<10:
            return f'{self.title}S0{self.season}E0{self.episode}'
        elif int(self.episode)>=10 and int(self.season)<10:
            return f'{self.title}S0{self.season}E{self.episode}'
        elif int(self.episode)<10 and int(self.season)>=10:
            return f'{self.title}S{self.season}E0{self.episode}'
        else:
            return f'{self.title}S{self.season}E{self.episode}'
dangan=film("Dangan",2012,"Mystery",23)
matrix=film("Matrix",2001,"Action",15847)
simp=serial(title="Simpsons",year=1990, type="Comedy", watched=2323,season=4,episode=12)
ranch=serial(23,2,title="Rancho",type="Slice of Life", year=1999,watched=245)
tomb=film("Tomb Raider",2006,"Adventure",2435)
m=serial(54,125,title="M jak milosc",type="Slice of life",year=1997,watched=20565)
lista_filmow=[dangan,simp,matrix,ranch,tomb,m]

def get_movies(list_F):
    x=[]
    for n in list_F:
        if isinstance(n,serial)==False:
            x.append(n)
    return sorted(x,key=lambda o:o.title)

def get_series(list_S):
    z=[]
    for n in list_S:
        if isinstance(n,serial):
            z.append(n)
    return sorted(z,key=lambda o:o.title)
print(get_series(lista_filmow)[2])

def search(tytul,lista_F):
    for i in lista_F:
        if tytul==i.title:
            return i
def generate_views(list):
    z=random.choice(list)
    z.watched+=random.randint(1,100)
def rep(a):
    for b in range(10):
        generate_views(a)
def top_titles(content_type, list_F, amount):
    list=[]
    list2=sorted(list_F,key=lambda i:i.watched) [::-1]
    if content_type=='film':
        for e in list2:
            if isinstance(e,serial):
                list2.remove(e)
    if content_type=='serial':
        for e in list2:
            if isinstance(e,serial)==0:
                list2.remove(e)
    for i in range(amount):
        list.append(list2[0])
        list2.remove(list2[0])
    return list

    



matrix=film(title='matrix', year=5, type=5, watched=2)
matrix.play
print(matrix)
