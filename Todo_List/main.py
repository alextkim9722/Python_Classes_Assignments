from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditor
import os


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
ckeditor = CKEditor(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    finished = db.Column(db.Integer(), nullable=False)


class CreateTaskForm(FlaskForm):
    title = StringField('Task title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', all_tasks=tasks)


@app.route('/new-task', methods=['GET', 'POST'])
def add_new_task():
    form = CreateTaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            finished=0
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create-task.html', form=form)


@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get(task_id)
    edit_form = CreateTaskForm(
        title=task.title,
        description=task.description,
        finished=0
    )
    if edit_form.validate_on_submit():
        task.title = edit_form.title.data
        task.description = edit_form.description.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("create-task.html", form=edit_form, is_edit=True)


@app.route("/finish_task/<int:task_id>", methods=["GET", "POST"])
def finish_task(task_id):
    task = Task.query.get(task_id)
    if task.finished == 1:
        task.finished = 0
    else:
        task.finished = 1
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task_to_delete = Task.query.get(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
