# -*- coding: utf-8 -*-
from gluon.tools import Auth

db = DAL("sqlite://storage.sqlite")

auth = Auth(db)
auth.define_tables(username=True)

db.define_table('image',
                Field('name', unique=True),
                Field('original_name', unique=True),
                Field('md5', 'string', unique=True),
                Field('size', 'integer'),
                Field('tif_parent_md5', 'string', unique=True),
                Field('size_tiff_parent', 'integer'),
                Field('file', 'upload'),
                format ='%(title)s')

db.define_table('note',
                Field('image_id', 'reference image'),
                Field('user_id', 'reference auth_user'),
                Field('title'),
                Field('email'),
                Field('body_text', 'text'))

db.image.name.requires = IS_NOT_IN_DB(db, db.image.name)
db.note.image_id.requires = IS_IN_DB(db, db.image.id, '%(title)s')
db.note.user_id.requires = IS_IN_DB(db, db.auth_user.id)
db.note.user_id.requires = IS_NOT_EMPTY()
db.note.email.requires = IS_EMAIL()
db.note.body_text.requires = IS_NOT_EMPTY()

db.note.image_id.writable = db.note.image_id.readable = False
