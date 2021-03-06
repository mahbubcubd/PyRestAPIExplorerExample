# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

import urllib2
import json
def index():
    return locals()

def news():
    if request.vars.q:
        query=request.vars.q
        url='https://newsapi.org/v2/everything?q='+query+'&apiKey=4cb16c3e195043e19c78bf41f380b784'
        contents = urllib2.urlopen(url).read()
        js=json.loads(contents)
        art=js['articles']
        now=js['articles'][1]
        image_now=now['urlToImage']
        title_now=now['title']
        url_now=now['url']
    else:
        contents = urllib2.urlopen("https://newsapi.org/v2/top-headlines?country=us&apiKey=4cb16c3e195043e19c78bf41f380b784").read()
        js=json.loads(contents)
        art=js['articles']
        now=js['articles'][1]
        image_now=now['urlToImage']
        title_now=now['title']
        url_now=now['url']
        
    sports_api='https://newsapi.org/v2/top-headlines?sources=bbc-sport&apiKey=4cb16c3e195043e19c78bf41f380b784'
    load_sports = urllib2.urlopen(sports_api).read()
    s_json=json.loads(load_sports)
    s1=s_json['articles'][1]
    s1_img=s1['urlToImage']
    s1_title=s1['title']
    s1_url=s1['url']
    s1_description=s1['description']
    return locals()




def movie():
    if request.vars.q:
        url="https://api.themoviedb.org/3/search/movie?api_key=d424b71bd56ee69ccd96fcaf5d9959d8&language=en-US&query="+str(request.vars.q)+"&page=1&include_adult=false"
        qr = urllib2.urlopen(url).read()
        pl=json.loads(qr)
        pll=pl['results']
    else:
        base="https://api.themoviedb.org"
        popular=base+"/3/movie/popular?api_key=d424b71bd56ee69ccd96fcaf5d9959d8&language=en-US&page=1"
        p = urllib2.urlopen(popular).read()
        pjson=json.loads(p)
        popular_list=pjson['results']
    return locals()

def movie_description():
    base="https://image.tmdb.org/t/p/w500/"
    if request.vars.id:
        movie_id=request.vars.id
        url="https://api.themoviedb.org/3/movie/"+str(movie_id)+"?api_key=d424b71bd56ee69ccd96fcaf5d9959d8&language=en-US"
        cr_url="https://api.themoviedb.org/3/movie/"+str(movie_id)+"/credits?api_key=d424b71bd56ee69ccd96fcaf5d9959d8&language=en-US"
        crload=urllib2.urlopen(cr_url).read()
        cj=json.loads(crload)
        writer=cj['crew'][0]['name']
        director=cj['crew'][1]['name']
        d = urllib2.urlopen(url).read()
        djsn=json.loads(d)
        poster=base+djsn['poster_path']
        overview=djsn['overview']
        
    return locals()


def github():
    user="https://api.github.com/users/mahbubcubd"
    r_u = urllib2.urlopen(user).read()
    j_u=json.loads(r_u)
    mp="https://api.github.com/search/repositories?q=stars:%3E1&s=stars&type=Repositories"
    mp_u = urllib2.urlopen(mp).read()
    mp_u=json.loads(mp_u)
    return locals()


def git_user():
    if request.vars.q:
        userlogin=request.vars.q
        user="https://api.github.com/users/"+str(userlogin)
        r_u = urllib2.urlopen(user).read()
        j_u=json.loads(r_u)
        mp="https://api.github.com/users/"+str(userlogin)+"/repos"
        mp_u = urllib2.urlopen(mp).read()
        mp_u=json.loads(mp_u)
        kp="https://api.github.com/search/repositories?q=stars:%3E1&s=stars&type=Repositories"
        kp_u = urllib2.urlopen(kp).read()
        kp_u=json.loads(kp_u)
    return locals()

def user():
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
