#!-*- coding: utf8 -*-

# -- TinyStore --
# TinyStore is the easy way of storing data into Datastore on Google App Engine.
# The use of TinyStore is very easy.
# TinyStore have only two functions, write and read.
# Please report to me about any bug reports or questions.
# TinyStore is Released into the Public Domain.
# 
# Author: Yuribossa
# Homepage: http://yuribossa.appspot.com/
# Mail: yuribossa@gmail.com
# 

# -- Example --
# from tiny_store import TinyStore
# 
# x = TinyStore()
# x.write('dog_name', 'alex')
# y = x.read('dog_name')
# 


from google.appengine.ext import db
import types

class TinyStoreModel(db.Expando):
    key_ = db.StringProperty()

class TinyStore():
    def write(self, key, value):
        query = db.Query(TinyStoreModel).filter('key_ =', key)
        if query.count():
            query = query.get()
            query.value = value
        else:
            if isinstance(key, (str, unicode)):
                query = TinyStoreModel(key_=key, value=value)
            else:
                return 0
        
        query.put()
        return 1
    
    def read(self, key):
        query = db.Query(TinyStoreModel).filter('key_ =', key)
        if query.count() == 1:
            query = query.get()
            return query.value
        return None
