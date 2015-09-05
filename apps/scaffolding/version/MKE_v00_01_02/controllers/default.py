# -*- coding: utf-8 -*-
def index():
    images = db().select(db.image.ALL, orderby=db.image.name)
    image_counter = 0
    return dict(images=images, image_number=image_counter)

@auth.requires_login()
def show():
    image = db.image(request.args(0,cast=int)) or redirect(URL('index'))
    db.note.image_id.default = image.id
    form = SQLFORM(db.note)
    if form.process().accepted:
        response.flash = 'Your note was displayed'
    posts = db(db.note.image_id==image.id).select()
    return dict(image=image, posts=posts, form=form)

def download():
    return response.download(request, db)

def user():
    return dict(form=auth())

@auth.requires_membership('manager')
def manage():
    grid = SQLFORM.smartgrid(db.image, linked_tables=['image'])
    return dict(grid=grid)

def overview():
    return response.render()

def introduction():
    return response.render()

def about():
    return response.render()

def contact():
    return response.render()
