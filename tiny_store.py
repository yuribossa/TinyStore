#!-*- coding: utf8 -*-

# -- TinyStore --
# TinyStore is the easy way of storing data into Datastore on Google App Engine.
# The use of TinyStore is very easy.
# TinyStore have three functions, write(), read(), check() and delete().
# All data-types supported by GAE can store TinyStore.
# TinyStore is released into the Public Domain.
# 

# Author: Yuribossa
# Hosted: http://github.com/yuribossa/TinyStore
# Homepage: http://yuribossa.appspot.com/
# Mail: yuribossa@gmail.com
# 

# -- Example --
# from tiny_store import TinyStore
# 
# x = TinyStore()
# x.write('dog_name', 'alex')
# y = x.read('dog_name')
# if x.check('dog_name'):
#     x.delete('dog_name')
# 


from google.appengine.ext import db

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
                return False
        
        query.put()
        return True
    
    def read(self, key):
        query = db.Query(TinyStoreModel).filter('key_ =', key)
        if query.count() == 1:
            query = query.get()
            return query.value
        return None
    
    def check(self, key):
        query = db.Query(TinyStoreModel).filter('key_ =', key)
        if query.count():
            return True
        else:
            return False
    
    def delete(self, key):
        query = db.Query(TinyStoreModel).filter('key_ =', key)
        if query.count():
            query = query.get()
            query.delete()
            return True
        else:
            return False
