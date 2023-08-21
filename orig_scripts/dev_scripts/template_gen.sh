#!/bin/bash

plan_name_instance="Sof Prep 365 WOD"
total_num_workouts=420
temp_file="tmp.txt"
tz="America/Anchorage"
rand=${RANDOM}

gen_template () {
    echo -e "
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Google Inc//Google Calendar 70.9054//EN
" > $temp_file

    for ((i=1;i<=${total_num_workouts};i++)); do
        echo -e "
BEGIN:VEVENT
DTSTART;TZID=${tz}:\"\"\"+fix_date(init_date, ${i})+\"\"\"
DTEND;TZID=${tz}:\"\"\"+fix_date(init_date, ${i})+\"\"\"
UID:7qluq7tpnapsle40btklsiloq${rand}google.com
RECURRENCE-ID;TZID=${tz}:\"\"\"+fix_date(init_date, ${i})+\"\"\"
DESCRIPTION:<a href=\"(link)\" class=\"pastedDriveLink-0\">${i}.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:{${plan_name_instance}}
TRANSP:OPAQUE
ATTACH;FILENAME=${i}.png;FMTTYPE=image/png:(link)
END:VEVENT" >> $temp_file
    done

    echo -e "
END:VCALENDAR
\"\"\"
" >> $temp_file
}

gen_template