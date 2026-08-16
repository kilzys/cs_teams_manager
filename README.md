<div align="center">

## CS Team Manager
</div>
Created as a hobby to pass time and enhance my understanding in Python. The program objective is to manage the points from competitive teams (inspired on *VRS*).

- [Features](#features)
- [Database and Excel](#databasetxt-and-hltvxlsx)
- [Known Limitations](#known-limitations)
- [Installation and Use](#installation-and-use)
<br>
<br>

## Features
- Create a new team;
- Delete a team;
- Edit a team manually *(points, victories, loses, name, etc)*;
- Add/Remove points based on win and loss, including a streak feature;
- Persistent data;
- Excel containing the data.
<br>

## database.txt and hltv.xlsx
Each line on the database is considered a team **(which can trigger an error that I'll explain on [Known Limitations](#known-limitations).)**. The expected format that the code use is:
```python
team_name,0,0,0,0,0  # expected
Vitality,10,5,2,132,1 # example of use
```
Each part of this line means:
*team_name, wins, streak, loses, points, majors*

When the user chooses to exit the program, *main* then calls another function that uses the data inside **database.txt** to generate an excel file called **hltv.xlsx**


## Known Limitations
The database parser treats every line in database.txt as a team entry like I previously mentioned. For that reason, a blank line (including a trailing empty line at the end of the file) will break the program. 

For that reason the minimum working dataset is 1 team with no blank lines.


## Installation and Use
Install the required packages:
```bash
pip install -r requirements.txt
```

Open **database.txt** and insert at least one team, e.g, `team_name,0,0,0,0,0`. Then run:
```bash
python main.py
```

