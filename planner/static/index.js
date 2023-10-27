function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deleteMeeting(meetingId) {
  fetch("/delete-meeting", {
    method: "POST",
    body: JSON.stringify({ meetingId: meetingId }),
  }).then((_res) => {
    window.location.href = "/meetings";
  });
}