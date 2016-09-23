from flask import Flask, render_template, request, flash, url_for, redirect
from db_model import *


app = Flask(__name__)
app.config['SECRET_KEY'] = "ssshhh"


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/add", methods=['GET', 'POST'])
def add_user_story():
    if request.method == 'POST':
        user_story = UserStory.create(**request.form.to_dict())
        flash('User Story created')
    return render_template("add_edit.html", user_story="user_story", event='Create')


'''@app.route('/edit/<story>', methods=['GET', 'POST'])
def edit_user_story(story):
    editke = UserStory.get(UserStory.id == story)
    if request.method == 'POST':
        UserStory.update(**request.form.to_dict())
        return redirect('/')
    return render_template('add_edit.html', user_story=editke, event='Edit')
'''
@app.route('/edit/<story_id>', methods=['GET', 'POST'])
def edit_user_story(story_id):
    if request.method == 'POST':
        UserStory.update(**request.form.to_dict()).where(UserStory.id == story_id).execute()
        flash('User Story updated.')
    return render_template("add_edit.html", user_story=UserStory.get(UserStory.id == story_id), event='Edit')

@app.route('/list')
def list_user_stories():
    data = UserStory.select()
    return render_template('list.html', data=data)


@app.route('/del/<story_id>', methods=['GET'])
def del_user_story(story_id):
    UserStory.delete().where(UserStory.id == story_id).execute()
    return redirect('/list')

if __name__ == '__main__':
    db.connect()
    create_tables()
    app.run(debug=True)
