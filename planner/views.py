from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import current_user, login_required
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        summary = request.form.get('summary')
        note_data = request.form.get('data')
        if len(note_data) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(
                summary=summary,
                data=note_data,
                user_id=current_user.id
            )
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template('home.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    note_id = note['noteId']
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})


@views.route('/meetings', methods=['GET', 'POST'])
@login_required
def meetings():
    return render_template('meetings.html', user=current_user)
