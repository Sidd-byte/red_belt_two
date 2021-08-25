from red_belt_app import app
from flask import render_template, redirect, request, session, flash
from red_belt_app.models.art import Show

@app.route('/new')
def new_art():
    return render_template('add_art.html')

@app.route('/new', methods = ['post'])
def create_show():

    if not Show.validate_show(request.form):
        return redirect('/new')

    data = {
        'title' : request.form['title'],
        'description' : request.form['description'],
        'price' : request.form['price'],
        'user_id' : session['logged_user']
    }
    new_art_id = Show.save(data)
    return redirect('/dashboard')


@app.route('/show/<int:id>/edit')
def edit_page(id):
    data = {
        'id' : id
    }
    art = Show.get_art(data)
    return render_template('edit_art.html', art = art)

# @app.route('/show/<int:id>/edit')
# def update_page(id):
#     if not Show.validate_show(request.form):
#         return redirect(f'/show/{id}/edit')

#     data = {
#         'title' : request.form['title'],
#         'description' : request.form['description'],
#         'price' : request.form['price'],
#         'user_id' : session['logged_user']
#     }

#     Show.update(data)
#     return redirect('/dashboard')



@app.route('/show/<int:id>/delete')
def edit_page(id):
    data = {
        'id' : id
    }
    Show.delete(data)
    return redirect('/dashboard')