import datetime
from doctest import Example
import sys


def fix_date(date, days_offset):
    return str(date + datetime.timedelta(days=days_offset-1)).replace(":", "").replace("-", "").replace(" ", "T")


def generate_workout_list(init_date):
    workout_list_first_30 = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Google Inc//Google Calendar 70.9054//EN

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 1)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 1)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 1)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w1-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w1-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
DESCRIPTION:<a href="" class="pastedDriveLink-0">w1-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w1-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w1-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w1-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-1">w1-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-1">w2-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w2-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w2-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
DESCRIPTION:<a href="" class="pastedDriveLink-0">w2-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-1">w2-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w2-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w2-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w5-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w5-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w5-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d3.png;FMTTYPE=image/png:
END:VEVENT
"""
    workout_list_last_30 = """
BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w5-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w5-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w5-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0" id="ow32708" __is_owner="true">w5-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-1">w6-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w6-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w6-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w6-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w6-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w6-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w6-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d7.png</a><br><br>you did it.&nbsp\;<br>now move on to the next mountain to conquer.
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d7.png;FMTTYPE=image/png:
END:VEVENT

END:VCALENDAR
"""
    filename = "HTK_Workout_Plan.ics"
    with open (filename, 'w') as f:
        f.write(workout_list_first_30)
        f.write(workout_list_last_30)
    f.close()
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