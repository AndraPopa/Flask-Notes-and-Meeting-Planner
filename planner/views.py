import datetime
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import current_user, login_required
from .models import Note, Meeting
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
    if request.method == 'POST':
        summary = request.form.get('summary')
        info = request.form.get('info')
        when = request.form.get('when')
        who = request.form.get('who')
        place = request.form.get('place')
        meeting_link = request.form.get('meeting_link')

        date_time_obj = datetime.datetime.strptime(when, "%Y-%m-%dT%H:%M")

        if len(info) < 3:
            flash('Meeting info is too short!', category='error')
        elif datetime.datetime.now() > date_time_obj:
            flash('Please add a meeting time in the future!', category='error')
        else:
            new_meeting = Meeting(
                summary=summary,
                info=info,
                when=date_time_obj,
                who=who,
                place=place,
                meeting_link=meeting_link,
                user_id=current_user.id
            )
            db.session.add(new_meeting)
            db.session.commit()

            flash('Meeting added!', category='success')
    return render_template('meetings.html', user=current_user)


@views.route('/delete-meeting', methods=['POST'])
def delete_meeting():
    meeting = json.loads(request.data)
    meeting_id = meeting['meetingId']
    meeting = Meeting.query.get(meeting_id)
    if meeting:
        if meeting.user_id == current_user.id:
            db.session.delete(meeting)
            db.session.commit()
    return jsonify({})
