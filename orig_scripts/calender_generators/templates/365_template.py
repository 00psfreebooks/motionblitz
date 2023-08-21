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
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 0)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 0)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 0)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w1-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 1)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 1)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 1)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w1-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w1-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w1-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w1-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w1-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w1-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w2-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w2-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w2-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w2-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w2-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w2-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w2-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w3-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w4-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w5-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w5-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w5-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w5-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w5-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w5-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w5-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w6-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w6-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w6-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w6-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w6-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w6-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w6-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w7-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w8-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w9-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w9-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 57)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 57)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 57)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w9-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w9-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 58)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 58)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 58)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w9-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w9-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 59)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 59)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 59)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w9-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w9-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 60)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 60)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 60)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w9-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w9-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 61)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 61)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 61)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w9-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w9-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 62)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 62)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 62)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w9-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w9-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 63)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 63)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 63)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w10-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w10-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 64)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 64)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 64)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w10-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w10-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 65)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 65)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 65)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w10-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w10-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 66)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 66)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 66)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w10-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w10-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 67)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 67)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 67)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w10-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w10-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 68)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 68)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 68)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w10-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w10-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 69)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 69)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 69)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w10-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w10-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 70)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 70)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 70)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w11-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w11-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 71)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 71)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 71)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w11-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w11-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 72)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 72)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 72)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w11-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w11-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 73)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 73)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 73)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w11-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w11-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 74)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 74)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 74)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w11-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w11-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 75)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 75)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 75)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w11-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w11-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 76)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 76)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 76)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w11-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w11-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 77)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 77)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 77)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w12-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w12-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 78)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 78)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 78)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w12-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w12-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 79)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 79)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 79)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w12-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w12-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 80)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 80)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 80)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w12-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w12-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 81)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 81)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 81)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w12-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w12-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 82)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 82)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 82)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w12-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w12-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 83)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 83)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 83)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w12-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w12-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 84)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 84)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 84)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w13-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w13-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 85)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 85)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 85)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w13-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w13-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 86)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 86)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 86)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w13-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w13-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 87)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 87)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 87)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w13-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w13-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 88)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 88)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 88)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w13-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w13-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 89)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 89)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 89)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w13-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w13-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 90)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 90)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 90)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w13-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w13-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 91)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 91)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 91)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w14-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w14-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 92)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 92)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 92)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w14-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w14-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 93)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 93)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 93)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w14-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w14-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 94)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 94)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 94)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w14-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w14-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 95)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 95)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 95)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w14-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w14-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 96)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 96)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 96)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w14-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w14-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 97)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 97)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 97)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w14-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w14-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 98)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 98)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 98)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w15-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w15-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 99)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 99)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 99)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w15-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w15-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 100)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 100)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 100)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w15-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w15-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 101)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 101)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 101)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w15-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w15-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 102)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 102)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 102)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w15-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w15-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 103)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 103)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 103)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w15-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w15-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 104)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 104)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 104)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w15-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w15-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 105)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 105)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 105)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w16-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w16-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 106)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 106)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 106)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w16-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w16-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 107)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 107)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 107)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w16-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w16-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 108)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 108)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 108)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w16-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w16-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 109)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 109)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 109)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w16-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w16-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 110)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 110)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 110)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w16-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w16-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 111)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 111)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 111)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w16-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w16-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 112)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 112)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 112)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w17-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w17-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 113)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 113)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 113)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w17-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w17-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 114)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 114)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 114)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w17-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w17-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 115)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 115)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 115)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w17-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w17-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 116)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 116)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 116)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w17-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w17-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 117)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 117)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 117)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w17-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w17-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 118)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 118)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 118)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w17-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w17-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 119)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 119)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 119)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w18-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w18-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 120)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 120)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 120)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w18-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w18-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 121)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 121)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 121)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w18-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w18-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 122)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 122)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 122)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w18-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w18-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 123)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 123)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 123)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w18-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w18-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 124)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 124)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 124)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w18-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w18-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 125)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 125)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 125)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w18-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w18-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 126)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 126)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 126)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w19-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w19-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 127)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 127)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 127)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w19-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w19-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 128)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 128)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 128)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w19-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w19-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 129)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 129)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 129)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w19-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w19-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 130)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 130)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 130)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w19-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w19-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 131)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 131)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 131)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w19-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w19-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 132)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 132)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 132)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w19-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w19-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 133)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 133)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 133)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w20-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w20-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 134)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 134)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 134)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w20-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w20-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 135)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 135)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 135)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w20-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w20-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 136)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 136)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 136)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w20-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w20-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 137)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 137)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 137)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w20-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w20-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 138)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 138)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 138)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w20-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w20-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 139)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 139)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 139)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w20-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w20-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 140)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 140)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 140)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w21-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w21-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 141)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 141)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 141)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w21-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w21-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 142)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 142)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 142)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w21-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w21-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 143)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 143)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 143)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w21-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w21-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 144)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 144)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 144)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w21-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w21-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 145)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 145)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 145)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w21-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w21-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 146)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 146)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 146)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w21-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w21-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 147)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 147)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 147)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w22-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w22-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 148)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 148)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 148)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w22-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w22-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 149)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 149)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 149)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w22-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w22-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 150)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 150)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 150)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w22-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w22-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 151)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 151)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 151)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w22-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w22-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 152)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 152)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 152)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w22-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w22-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 153)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 153)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 153)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w22-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w22-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 154)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 154)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 154)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w23-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w23-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 155)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 155)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 155)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w23-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w23-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 156)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 156)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 156)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w23-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w23-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 157)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 157)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 157)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w23-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w23-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 158)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 158)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 158)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w23-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w23-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 159)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 159)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 159)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w23-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w23-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 160)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 160)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 160)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w23-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w23-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 161)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 161)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 161)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w24-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w24-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 162)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 162)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 162)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w24-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w24-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 163)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 163)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 163)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w24-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w24-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 164)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 164)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 164)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w24-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w24-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 165)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 165)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 165)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w24-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w24-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 166)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 166)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 166)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w24-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w24-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 167)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 167)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 167)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w24-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w24-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 168)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 168)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 168)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w25-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w25-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 169)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 169)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 169)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w25-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w25-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 170)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 170)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 170)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w25-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w25-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 171)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 171)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 171)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w25-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w25-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 172)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 172)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 172)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w25-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w25-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 173)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 173)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 173)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w25-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w25-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 174)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 174)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 174)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w25-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w25-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 175)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 175)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 175)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w26-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w26-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 176)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 176)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 176)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w26-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w26-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 177)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 177)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 177)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w26-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w26-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 178)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 178)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 178)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w26-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w26-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 179)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 179)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 179)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w26-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w26-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 180)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 180)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 180)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w26-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w26-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 181)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 181)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 181)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w26-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w26-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 182)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 182)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 182)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w27-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w27-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 183)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 183)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 183)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w27-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w27-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 184)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 184)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 184)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w27-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w27-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 185)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 185)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 185)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w27-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w27-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 186)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 186)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 186)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w27-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w27-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 187)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 187)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 187)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w27-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w27-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 188)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 188)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 188)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w27-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w27-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 189)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 189)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 189)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w28-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w28-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 190)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 190)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 190)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w28-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w28-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 191)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 191)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 191)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w28-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w28-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 192)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 192)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 192)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w28-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w28-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 193)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 193)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 193)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w28-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w28-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 194)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 194)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 194)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w28-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w28-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 195)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 195)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 195)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w28-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w28-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 196)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 196)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 196)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w29-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w29-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 197)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 197)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 197)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w29-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w29-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 198)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 198)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 198)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w29-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w29-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 199)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 199)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 199)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w29-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w29-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 200)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 200)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 200)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w29-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w29-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 201)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 201)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 201)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w29-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w29-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 202)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 202)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 202)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w29-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w29-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 203)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 203)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 203)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w30-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w30-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 204)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 204)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 204)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w30-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w30-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 205)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 205)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 205)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w30-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w30-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 206)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 206)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 206)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w30-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w30-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 207)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 207)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 207)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w30-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w30-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 208)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 208)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 208)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w30-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w30-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 209)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 209)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 209)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w30-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w30-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 210)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 210)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 210)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w31-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w31-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 211)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 211)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 211)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w31-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w31-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 212)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 212)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 212)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w31-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w31-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 213)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 213)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 213)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w31-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w31-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 214)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 214)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 214)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w31-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w31-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 215)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 215)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 215)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w31-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w31-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 216)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 216)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 216)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w31-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w31-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 217)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 217)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 217)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w32-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w32-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 218)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 218)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 218)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w32-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w32-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 219)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 219)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 219)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w32-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w32-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 220)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 220)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 220)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w32-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w32-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 221)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 221)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 221)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w32-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w32-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 222)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 222)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 222)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w32-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w32-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 223)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 223)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 223)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w32-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w32-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 224)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 224)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 224)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w33-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w33-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 225)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 225)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 225)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w33-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w33-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 226)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 226)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 226)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w33-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w33-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 227)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 227)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 227)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w33-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w33-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 228)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 228)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 228)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w33-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w33-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 229)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 229)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 229)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w33-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w33-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 230)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 230)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 230)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w33-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w33-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 231)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 231)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 231)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w34-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w34-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 232)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 232)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 232)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w34-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w34-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 233)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 233)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 233)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w34-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w34-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 234)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 234)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 234)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w34-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w34-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 235)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 235)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 235)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w34-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w34-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 236)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 236)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 236)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w34-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w34-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 237)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 237)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 237)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w34-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w34-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 238)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 238)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 238)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w35-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w35-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 239)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 239)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 239)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w35-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w35-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 240)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 240)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 240)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w35-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w35-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 241)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 241)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 241)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w35-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w35-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 242)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 242)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 242)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w35-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w35-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 243)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 243)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 243)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w35-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w35-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 244)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 244)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 244)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w35-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w35-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 245)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 245)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 245)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w36-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w36-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 246)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 246)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 246)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w36-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w36-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 247)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 247)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 247)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w36-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w36-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 248)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 248)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 248)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w36-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w36-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 249)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 249)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 249)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w36-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w36-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 250)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 250)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 250)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w36-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w36-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 251)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 251)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 251)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w36-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w36-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 252)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 252)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 252)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w37-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w37-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 253)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 253)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 253)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w37-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w37-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 254)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 254)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 254)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w37-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w37-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 255)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 255)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 255)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w37-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w37-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 256)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 256)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 256)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w37-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w37-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 257)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 257)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 257)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w37-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w37-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 258)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 258)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 258)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w37-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w37-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 259)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 259)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 259)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w38-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w38-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 260)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 260)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 260)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w38-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w38-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 261)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 261)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 261)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w38-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w38-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 262)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 262)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 262)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w38-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w38-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 263)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 263)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 263)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w38-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w38-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 264)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 264)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 264)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w38-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w38-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 265)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 265)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 265)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w38-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w38-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 266)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 266)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 266)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w39-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w39-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 267)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 267)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 267)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w39-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w39-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 268)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 268)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 268)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w39-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w39-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 269)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 269)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 269)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w39-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w39-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 270)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 270)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 270)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w39-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w39-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 271)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 271)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 271)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w39-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w39-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 272)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 272)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 272)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w39-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w39-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 273)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 273)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 273)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w40-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w40-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 274)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 274)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 274)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w40-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w40-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 275)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 275)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 275)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w40-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w40-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 276)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 276)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 276)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w40-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w40-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 277)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 277)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 277)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w40-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w40-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 278)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 278)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 278)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w40-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w40-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 279)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 279)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 279)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w40-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w40-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 280)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 280)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 280)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w41-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w41-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 281)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 281)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 281)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w41-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w41-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 282)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 282)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 282)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w41-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w41-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 283)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 283)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 283)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w41-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w41-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 284)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 284)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 284)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w41-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w41-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 285)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 285)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 285)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w41-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w41-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 286)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 286)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 286)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w41-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w41-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 287)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 287)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 287)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w42-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w42-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 288)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 288)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 288)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w42-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w42-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 289)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 289)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 289)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w42-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w42-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 290)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 290)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 290)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w42-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w42-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 291)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 291)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 291)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w42-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w42-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 292)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 292)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 292)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w42-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w42-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 293)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 293)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 293)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w42-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w42-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 294)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 294)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 294)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w43-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w43-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 295)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 295)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 295)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w43-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w43-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 296)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 296)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 296)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w43-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w43-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 297)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 297)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 297)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w43-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w43-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 298)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 298)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 298)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w43-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w43-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 299)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 299)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 299)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w43-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w43-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 300)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 300)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 300)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w43-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w43-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 301)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 301)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 301)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w44-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w44-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 302)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 302)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 302)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w44-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w44-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 303)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 303)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 303)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w44-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w44-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 304)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 304)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 304)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w44-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w44-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 305)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 305)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 305)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w44-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w44-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 306)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 306)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 306)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w44-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w44-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 307)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 307)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 307)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w44-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w44-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 308)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 308)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 308)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w45-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w45-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 309)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 309)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 309)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w45-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w45-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 310)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 310)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 310)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w45-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w45-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 311)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 311)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 311)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w45-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w45-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 312)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 312)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 312)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w45-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w45-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 313)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 313)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 313)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w45-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w45-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 314)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 314)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 314)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w45-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w45-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 315)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 315)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 315)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w46-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w46-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 316)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 316)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 316)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w46-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w46-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 317)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 317)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 317)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w46-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w46-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 318)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 318)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 318)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w46-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w46-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 319)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 319)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 319)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w46-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w46-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 320)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 320)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 320)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w46-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w46-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 321)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 321)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 321)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w46-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w46-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 322)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 322)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 322)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w47-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w47-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 323)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 323)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 323)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w47-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w47-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 324)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 324)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 324)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w47-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w47-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 325)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 325)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 325)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w47-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w47-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 326)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 326)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 326)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w47-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w47-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 327)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 327)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 327)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w47-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w47-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 328)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 328)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 328)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w47-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w47-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 329)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 329)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 329)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w48-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w48-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 330)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 330)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 330)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w48-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w48-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 331)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 331)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 331)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w48-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w48-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 332)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 332)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 332)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w48-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w48-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 333)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 333)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 333)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w48-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w48-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 334)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 334)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 334)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w48-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w48-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 335)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 335)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 335)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w48-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w48-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 336)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 336)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 336)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w49-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w49-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 337)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 337)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 337)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w49-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w49-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 338)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 338)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 338)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w49-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w49-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 339)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 339)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 339)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w49-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w49-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 340)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 340)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 340)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w49-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w49-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 341)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 341)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 341)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w49-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w49-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 342)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 342)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 342)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w49-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w49-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 343)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 343)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 343)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w50-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w50-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 344)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 344)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 344)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w50-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w50-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 345)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 345)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 345)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w50-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w50-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 346)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 346)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 346)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w50-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w50-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 347)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 347)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 347)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w50-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w50-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 348)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 348)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 348)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w50-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w50-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 349)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 349)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 349)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w50-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w50-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 350)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 350)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 350)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w51-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w51-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 351)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 351)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 351)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w51-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w51-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 352)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 352)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 352)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w51-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w51-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 353)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 353)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 353)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w51-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w51-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 354)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 354)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 354)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w51-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w51-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 355)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 355)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 355)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w51-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w51-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 356)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 356)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 356)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w51-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w51-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 357)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 357)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 357)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w52-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w52-d1.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 358)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 358)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 358)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w52-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w52-d2.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 359)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 359)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 359)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w52-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w52-d3.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 360)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 360)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 360)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w52-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w52-d4.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 361)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 361)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 361)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w52-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w52-d5.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 362)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 362)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 362)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w52-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w52-d6.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 363)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 363)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 363)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w52-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w52-d7.png;FMTTYPE=image/png:
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 364)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 364)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 364)+"""
DESCRIPTION:<a href="" class="pastedDriveLink-0">w53-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w53-d1.png;FMTTYPE=image/png:
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