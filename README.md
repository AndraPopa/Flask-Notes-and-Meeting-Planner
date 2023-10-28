# Flask Notes and Meetings Planner

This is a simple Flask app that can be used to **keep track of notes and meetings.**

In order to run this project, you first have to assure you have python installed on your machine. In order to do this, just open a terminal session and type python3 --version if you are on a MAC or python --version if you use Windows.

Clone this repository and make sure you install the requirements: pip install -r requirements.txt.

Run the <code>main.py</code> file and the server will start on localhost:5000.

Then, you will be able to create an account and automatically login. The root endpoint is used for adding notes <code>120.0.0.1:5000/</code> and from there you can very easily navigate to the meetings endpoint <code>127.0.0.1:5000/meetings</code>.
Adding notes and meetings can be done very easily using the provided forms.