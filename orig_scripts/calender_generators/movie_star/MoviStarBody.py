import datetime
from doctest import Example
import sys
import random

rand = random.randint(10000, 99999)

def fix_date(date, days_offset):
    return str(date + datetime.timedelta(days=days_offset-1)).replace(":", "").replace("-", "").replace(" ", "T")

def append(filename, data):
    with open(filename, "a") as f:
        f.write(data)

def make_workout(workout, init_date, offset):
    
    name = "Movie Star Body WOD"
    body = """
BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, offset)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, offset)+"""
UID:7qluq7tpnapsle40btklsiloq5"""+str(rand)+"""google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, offset)+"""
DESCRIPTION: """+workout+"""
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY: """+name+"""
TRANSP:OPAQUE
END:VEVENT

"""
    return body


def generate_workout_list(init_date):
    filename = "MovieStarBody.ics"
    phase1_len_weeks = 12
    phase2_len_weeks = 4


    phase1_workout1 = "- incline bench\\n - flat bench\\n - bicep curls\\n - skull crushers\\n - rear delts lifts"
    phase1_workout2 = "- bulgarian split squats\\n - nordic curls\\n - sissy squats\\n - calf raises\\n - farmer shrugs"
    phase1_workout3 = "- shoulder press\\n - pull ups\\n - flye press\\n - hammer curls\\n - lateral raises"
    phase1_workout4 = "- hanging knee raises\\n - ab wheel roll outs\\n - glutes & lower back"

    phase2_wokout1 = "- incline db bench\\n - machine bench or weighted push-ups\\n - machine curls or concentration curls\\n - tricep pushdowns\\n - bent over flyes"
    phase2_wokout2 = "- step ups or front squats\\n - romainian deadlifts\\n - ATG split squats or sissy squats or leg extensions\\n - seated calf raises\\n - cable shrugs"
    phase2_wokout3 = "- DB shoulder press\\n - arnold press\\n - weighted pull-ups\\n - sternum pull-ups\\n - incline press flye\\n - hammer rope curls\\n - triceps pushdowns\\n - lateral raises"

    header = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Google Inc//Google Calendar 70.9054//EN
"""

    footer = """END:VCALENDAR"""

    body = []

    for i in range(1, phase1_len_weeks+1):
        day1 = make_workout(phase1_workout1, init_date, (i*7)-6)
        day2 = make_workout("rest", init_date, (i*7)-6+1)
        day3 = make_workout(phase1_workout2, init_date, (i*7)-6+2)
        day4 = make_workout("rest", init_date, (i*7)-6+3)
        day5 = make_workout(phase1_workout3, init_date, (i*7)-6+4)
        day6 = make_workout(phase1_workout4, init_date, (i*7)-6+5)
        day7 = make_workout("rest", init_date, (i*7)-6+6)
        body.append(day1)
        body.append(day2)
        body.append(day3)
        body.append(day4)
        body.append(day5)
        body.append(day6)
        body.append(day7)

    for i in range(1, phase2_len_weeks+1):
        day1 = make_workout(phase2_wokout1, init_date, (phase1_len_weeks*7)+(i*7)-6)
        day2 = make_workout("rest", init_date, (phase1_len_weeks*7)+(i*7)-6+1)
        day3 = make_workout("rest", init_date, (phase1_len_weeks*7)+(i*7)-6+2)
        day4 = make_workout(phase2_wokout2, init_date, (phase1_len_weeks*7)+(i*7)-6+3)
        day5 = make_workout("rest", init_date, (phase1_len_weeks*7)+(i*7)-6+4)
        day6 = make_workout(phase2_wokout3, init_date, (phase1_len_weeks*7)+(i*7)-6+5)
        day7 = make_workout("rest", init_date, (phase1_len_weeks*7)+(i*7)-6+6)
        body.append(day1)
        body.append(day2)
        body.append(day3)
        body.append(day4)
        body.append(day5)
        body.append(day6)
        body.append(day7)

    append(filename, header)
    for day in body:
        append(filename, day)
    append(filename, footer)
    print("Generated: "+filename)

def main():
    example = datetime.datetime.now()
    example1 = example.strftime("%m-%d-%y")
    example2 = example.strftime("%I:%M%p")
    print("Example: "+example1+" @ "+example2)
    start_date = input("Enter Start Date (MM-DD-YY): ")
    workout_time = input("Enter Start Time (HH:MM:PM or AM): ")
    start_date = datetime.datetime.strptime(start_date, "%m-%d-%y")
    workout_time = datetime.datetime.strptime(workout_time, "%I:%M%p")
    init_date = start_date.replace(hour=workout_time.hour, minute=workout_time.minute)
    generate_workout_list(init_date)

main()