import datetime
from doctest import Example
import sys


def fix_date(date, days_offset):
    return str(date + datetime.timedelta(days=days_offset-1)).replace(":", "").replace("-", "").replace(" ", "T")


def generate_workout_list(init_date):
    workouts = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Google Inc//Google Calendar 70.9054//EN


BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 1)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 1)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 1)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Ygfk8rscPzu6fso_Q79ALN1hbQ0eY90B/view?usp=sharing" class="pastedDriveLink-0">1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Ygfk8rscPzu6fso_Q79ALN1hbQ0eY90B/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1qhnCMZ94TwN2bV-IEM0N6oBKXpeoD-Zp/view?usp=sharing" class="pastedDriveLink-0">2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1qhnCMZ94TwN2bV-IEM0N6oBKXpeoD-Zp/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1S7h1RfgxHSFVbXK7S4AzzhaBLYJD2wgW/view?usp=sharing" class="pastedDriveLink-0">3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1S7h1RfgxHSFVbXK7S4AzzhaBLYJD2wgW/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1MmlWP8O9A_o4lwKsN0FrUJAaMYwfpQCc/view?usp=sharing" class="pastedDriveLink-0">4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1MmlWP8O9A_o4lwKsN0FrUJAaMYwfpQCc/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1l9FJmHPe0WWb8a3l_AhUQv9osLO1bJls/view?usp=sharing" class="pastedDriveLink-0">5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1l9FJmHPe0WWb8a3l_AhUQv9osLO1bJls/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1UqKfG1Eqt5K5PI4IoVevQ7tqiP9p1wZK/view?usp=sharing" class="pastedDriveLink-0">6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1UqKfG1Eqt5K5PI4IoVevQ7tqiP9p1wZK/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1U13v6o9bt3Y-d9d3xrJzqXKlz_UN45gg/view?usp=sharing" class="pastedDriveLink-0">7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1U13v6o9bt3Y-d9d3xrJzqXKlz_UN45gg/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/12iMB937lFfm_WGRx_MDySnA3vFy8fdFk/view?usp=sharing" class="pastedDriveLink-0">8.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=8.png;FMTTYPE=image/png:https://drive.google.com/file/d/12iMB937lFfm_WGRx_MDySnA3vFy8fdFk/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1mXj5iJ60xgMxBvBYThl_ta2AVcrQBcVk/view?usp=sharing" class="pastedDriveLink-0">9.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=9.png;FMTTYPE=image/png:https://drive.google.com/file/d/1mXj5iJ60xgMxBvBYThl_ta2AVcrQBcVk/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1W7XUe9l-rs6zbX7cn3KzIoQtjr7QMPzg/view?usp=sharing" class="pastedDriveLink-0">10.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=10.png;FMTTYPE=image/png:https://drive.google.com/file/d/1W7XUe9l-rs6zbX7cn3KzIoQtjr7QMPzg/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1gXU35OzTbRIxxT6q80rnN-gIp5gkIx_e/view?usp=sharing" class="pastedDriveLink-0">11.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=11.png;FMTTYPE=image/png:https://drive.google.com/file/d/1gXU35OzTbRIxxT6q80rnN-gIp5gkIx_e/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1tfLlLH6iIhURZYeQ_uqIaYyRwdoE4eXz/view?usp=sharing" class="pastedDriveLink-0">12.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=12.png;FMTTYPE=image/png:https://drive.google.com/file/d/1tfLlLH6iIhURZYeQ_uqIaYyRwdoE4eXz/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/13zahSnorpiLPFhOVgRmJ9eL-YC2buGtW/view?usp=sharing" class="pastedDriveLink-0">13.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=13.png;FMTTYPE=image/png:https://drive.google.com/file/d/13zahSnorpiLPFhOVgRmJ9eL-YC2buGtW/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1j8PsB9BBuEuJv6pGbNOAGA4hmM9fVtf-/view?usp=sharing" class="pastedDriveLink-0">14.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=14.png;FMTTYPE=image/png:https://drive.google.com/file/d/1j8PsB9BBuEuJv6pGbNOAGA4hmM9fVtf-/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1agJVbokAHpsYJRu1pk6mXzceNQgjpPDY/view?usp=sharing" class="pastedDriveLink-0">15.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=15.png;FMTTYPE=image/png:https://drive.google.com/file/d/1agJVbokAHpsYJRu1pk6mXzceNQgjpPDY/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1g62iNUGP0OUBEiz6LcJ3Z71JRwWkPTh9/view?usp=sharing" class="pastedDriveLink-0">16.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=16.png;FMTTYPE=image/png:https://drive.google.com/file/d/1g62iNUGP0OUBEiz6LcJ3Z71JRwWkPTh9/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1yJbNMBkUmRDmAKLuSqG1MV_alN-5B7cl/view?usp=sharing" class="pastedDriveLink-0">17.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=17.png;FMTTYPE=image/png:https://drive.google.com/file/d/1yJbNMBkUmRDmAKLuSqG1MV_alN-5B7cl/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1eFMOyTOzStD2nqS6g83GeL3JzGONdUFc/view?usp=sharing" class="pastedDriveLink-0">18.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=18.png;FMTTYPE=image/png:https://drive.google.com/file/d/1eFMOyTOzStD2nqS6g83GeL3JzGONdUFc/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1qECdK6Pd4RyhDhpWohJqDd9HDU6kftNe/view?usp=sharing" class="pastedDriveLink-0">19.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=19.png;FMTTYPE=image/png:https://drive.google.com/file/d/1qECdK6Pd4RyhDhpWohJqDd9HDU6kftNe/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/12OzPfhwawsZKMrYxNnK1Ldc0ZAmTLKAi/view?usp=sharing" class="pastedDriveLink-0">20.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=20.png;FMTTYPE=image/png:https://drive.google.com/file/d/12OzPfhwawsZKMrYxNnK1Ldc0ZAmTLKAi/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1izXOo9ccPnzGMCMwLWoO1gSZ1RWuU3jj/view?usp=sharing" class="pastedDriveLink-0">21.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=21.png;FMTTYPE=image/png:https://drive.google.com/file/d/1izXOo9ccPnzGMCMwLWoO1gSZ1RWuU3jj/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1xqD2SAL1SC9XLTRlgjadn_-GrSwnXjUi/view?usp=sharing" class="pastedDriveLink-0">22.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=22.png;FMTTYPE=image/png:https://drive.google.com/file/d/1xqD2SAL1SC9XLTRlgjadn_-GrSwnXjUi/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1oaexViDnQE1FBjnuJK7jpfH2nBcqOqoq/view?usp=sharing" class="pastedDriveLink-0">23.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=23.png;FMTTYPE=image/png:https://drive.google.com/file/d/1oaexViDnQE1FBjnuJK7jpfH2nBcqOqoq/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1mFPnOGQEVYr5HeaA3OteKMn0wUdokCWx/view?usp=sharing" class="pastedDriveLink-0">24.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=24.png;FMTTYPE=image/png:https://drive.google.com/file/d/1mFPnOGQEVYr5HeaA3OteKMn0wUdokCWx/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Iy3j4eVMVlSFqayHWiruu3Xd8Wq_Rusa/view?usp=sharing" class="pastedDriveLink-0">25.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=25.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Iy3j4eVMVlSFqayHWiruu3Xd8Wq_Rusa/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1IkhXUhLXTGUNAvDhLaG4FELSRWWfGMkw/view?usp=sharing" class="pastedDriveLink-0">26.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=26.png;FMTTYPE=image/png:https://drive.google.com/file/d/1IkhXUhLXTGUNAvDhLaG4FELSRWWfGMkw/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1NHnYHazqBzGe7WvYh1Rk94PwJMPUwi63/view?usp=sharing" class="pastedDriveLink-0">27.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=27.png;FMTTYPE=image/png:https://drive.google.com/file/d/1NHnYHazqBzGe7WvYh1Rk94PwJMPUwi63/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1id5croepjgj2U_VEw08AGg_M2IYq6ryR/view?usp=sharing" class="pastedDriveLink-0">28.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=28.png;FMTTYPE=image/png:https://drive.google.com/file/d/1id5croepjgj2U_VEw08AGg_M2IYq6ryR/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Iorpb7gFIoHRu6SRQfT6rWqA1-ZVRbne/view?usp=sharing" class="pastedDriveLink-0">29.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=29.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Iorpb7gFIoHRu6SRQfT6rWqA1-ZVRbne/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1XW-a1M_URm_qIx9SdFaeXSSu3bS3Wv5t/view?usp=sharing" class="pastedDriveLink-0">30.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=30.png;FMTTYPE=image/png:https://drive.google.com/file/d/1XW-a1M_URm_qIx9SdFaeXSSu3bS3Wv5t/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1nkrpL3kh61g3YG_U-_4UgMGo5lYXaJGF/view?usp=sharing" class="pastedDriveLink-0">31.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=31.png;FMTTYPE=image/png:https://drive.google.com/file/d/1nkrpL3kh61g3YG_U-_4UgMGo5lYXaJGF/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Tk0BfjjNJCOkHAYmBlznXLovPxDEWvHc/view?usp=sharing" class="pastedDriveLink-0">32.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=32.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Tk0BfjjNJCOkHAYmBlznXLovPxDEWvHc/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1m6F4ygCg8474cQK-rJkneyKLLRyXdU_C/view?usp=sharing" class="pastedDriveLink-0">33.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=33.png;FMTTYPE=image/png:https://drive.google.com/file/d/1m6F4ygCg8474cQK-rJkneyKLLRyXdU_C/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1XfDw-3OE8YPJ3CgTsdA_vVcOj-m1Qanc/view?usp=sharing" class="pastedDriveLink-0">34.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=34.png;FMTTYPE=image/png:https://drive.google.com/file/d/1XfDw-3OE8YPJ3CgTsdA_vVcOj-m1Qanc/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/18RqVg2UKviUoIKduKGdKZN81NZLbSnxn/view?usp=sharing" class="pastedDriveLink-0">35.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=35.png;FMTTYPE=image/png:https://drive.google.com/file/d/18RqVg2UKviUoIKduKGdKZN81NZLbSnxn/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Ttk10aND90wJKc-OJOLfEhD8kgHIEUbl/view?usp=sharing" class="pastedDriveLink-0">36.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=36.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Ttk10aND90wJKc-OJOLfEhD8kgHIEUbl/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1-anHohO42PcOfkjgNpj8cvwp7GsK4BzB/view?usp=sharing" class="pastedDriveLink-0">37.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=37.png;FMTTYPE=image/png:https://drive.google.com/file/d/1-anHohO42PcOfkjgNpj8cvwp7GsK4BzB/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1L19AKQVqRmZKjRsSzrPz5dIZM6L8yryK/view?usp=sharing" class="pastedDriveLink-0">38.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=38.png;FMTTYPE=image/png:https://drive.google.com/file/d/1L19AKQVqRmZKjRsSzrPz5dIZM6L8yryK/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1hw65srH23o9xuN1zinvuFJZWsD8_4fVA/view?usp=sharing" class="pastedDriveLink-0">39.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=39.png;FMTTYPE=image/png:https://drive.google.com/file/d/1hw65srH23o9xuN1zinvuFJZWsD8_4fVA/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1-gSS3l0xRi-LAZ8TujQbHXVhhkD_Ohx9/view?usp=sharing" class="pastedDriveLink-0">40.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=40.png;FMTTYPE=image/png:https://drive.google.com/file/d/1-gSS3l0xRi-LAZ8TujQbHXVhhkD_Ohx9/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1JeV0LLG20zevhoQWgHzBFNZ_sNgV8KVI/view?usp=sharing" class="pastedDriveLink-0">41.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=41.png;FMTTYPE=image/png:https://drive.google.com/file/d/1JeV0LLG20zevhoQWgHzBFNZ_sNgV8KVI/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/12F9fysHccDDnWdbPhy8YhnzEVGsDO3kg/view?usp=sharing" class="pastedDriveLink-0">42.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=42.png;FMTTYPE=image/png:https://drive.google.com/file/d/12F9fysHccDDnWdbPhy8YhnzEVGsDO3kg/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1IlzrR21eLr5BZJLDK5IwtOCZJecSHd2Z/view?usp=sharing" class="pastedDriveLink-0">43.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=43.png;FMTTYPE=image/png:https://drive.google.com/file/d/1IlzrR21eLr5BZJLDK5IwtOCZJecSHd2Z/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1HplxOX392VPWWS6VBmH3gI8AC51BaAtv/view?usp=sharing" class="pastedDriveLink-0">44.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=44.png;FMTTYPE=image/png:https://drive.google.com/file/d/1HplxOX392VPWWS6VBmH3gI8AC51BaAtv/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Pk_wSSqlMSgWHtTjjjHXIqp3RSC-QJzJ/view?usp=sharing" class="pastedDriveLink-0">45.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=45.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Pk_wSSqlMSgWHtTjjjHXIqp3RSC-QJzJ/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/13qhU5o1Qbqm5MUMR9PSGUj9ZLNv4w-k2/view?usp=sharing" class="pastedDriveLink-0">46.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=46.png;FMTTYPE=image/png:https://drive.google.com/file/d/13qhU5o1Qbqm5MUMR9PSGUj9ZLNv4w-k2/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/16zCcEtP5OogFnWNbBOhDKNdILQzZolke/view?usp=sharing" class="pastedDriveLink-0">47.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=47.png;FMTTYPE=image/png:https://drive.google.com/file/d/16zCcEtP5OogFnWNbBOhDKNdILQzZolke/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Lv0Gt73nY6xV9CNyJYiUiaRbMk_mqsbG/view?usp=sharing" class="pastedDriveLink-0">48.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=48.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Lv0Gt73nY6xV9CNyJYiUiaRbMk_mqsbG/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1dOmMAFOzQnU4AB1PLcDmgE0-OQKF5XUU/view?usp=sharing" class="pastedDriveLink-0">49.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=49.png;FMTTYPE=image/png:https://drive.google.com/file/d/1dOmMAFOzQnU4AB1PLcDmgE0-OQKF5XUU/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1c71ndu4ifM-K8dCMXUym1k0njHRP7IhG/view?usp=sharing" class="pastedDriveLink-0">50.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=50.png;FMTTYPE=image/png:https://drive.google.com/file/d/1c71ndu4ifM-K8dCMXUym1k0njHRP7IhG/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/13ap2INcCreZhA8k5--cALqZY9T1AMMCv/view?usp=sharing" class="pastedDriveLink-0">51.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=51.png;FMTTYPE=image/png:https://drive.google.com/file/d/13ap2INcCreZhA8k5--cALqZY9T1AMMCv/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1HmhwPbaeiVsXHp4S9LNVPwlhgPRWW_ZW/view?usp=sharing" class="pastedDriveLink-0">52.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=52.png;FMTTYPE=image/png:https://drive.google.com/file/d/1HmhwPbaeiVsXHp4S9LNVPwlhgPRWW_ZW/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1HTltaB20qWZG1UnVLTqGHfN2PldJWc3e/view?usp=sharing" class="pastedDriveLink-0">53.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=53.png;FMTTYPE=image/png:https://drive.google.com/file/d/1HTltaB20qWZG1UnVLTqGHfN2PldJWc3e/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/15O89fu-q3ooQRFmvqThRSss0oLqRJ-mK/view?usp=sharing" class="pastedDriveLink-0">54.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=54.png;FMTTYPE=image/png:https://drive.google.com/file/d/15O89fu-q3ooQRFmvqThRSss0oLqRJ-mK/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1DoOw6cKoxr1JAgZG3EuIDrLs9c8PdAM8/view?usp=sharing" class="pastedDriveLink-0">55.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=55.png;FMTTYPE=image/png:https://drive.google.com/file/d/1DoOw6cKoxr1JAgZG3EuIDrLs9c8PdAM8/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ElXua0WErQNM4w_kXsvVzl_DY9CnUgvm/view?usp=sharing" class="pastedDriveLink-0">56.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=56.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ElXua0WErQNM4w_kXsvVzl_DY9CnUgvm/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 57)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 57)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 57)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1EhqqXX_ONuFawMD6uUvOWrjnjEWEISwH/view?usp=sharing" class="pastedDriveLink-0">57.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=57.png;FMTTYPE=image/png:https://drive.google.com/file/d/1EhqqXX_ONuFawMD6uUvOWrjnjEWEISwH/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 58)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 58)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 58)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1yyR4uDmtckmc_Ezi5h1czMNKmSVwKDVl/view?usp=sharing" class="pastedDriveLink-0">58.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=58.png;FMTTYPE=image/png:https://drive.google.com/file/d/1yyR4uDmtckmc_Ezi5h1czMNKmSVwKDVl/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 59)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 59)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 59)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1v17d5EFlr5u-I-rZdA-E0d7MkYHUqXky/view?usp=sharing" class="pastedDriveLink-0">59.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=59.png;FMTTYPE=image/png:https://drive.google.com/file/d/1v17d5EFlr5u-I-rZdA-E0d7MkYHUqXky/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 60)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 60)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 60)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1mimnF7qf-Mfe-JoTNJK5jXQEUhi4N1YT/view?usp=sharing" class="pastedDriveLink-0">60.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=60.png;FMTTYPE=image/png:https://drive.google.com/file/d/1mimnF7qf-Mfe-JoTNJK5jXQEUhi4N1YT/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 61)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 61)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 61)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1AGFertal3MTDJNxAKw0uUVHdG34JoIND/view?usp=sharing" class="pastedDriveLink-0">61.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=61.png;FMTTYPE=image/png:https://drive.google.com/file/d/1AGFertal3MTDJNxAKw0uUVHdG34JoIND/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 62)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 62)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 62)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1dBWdFk5Bl72vfUO3ocr2MscwxvYdmgBy/view?usp=sharing" class="pastedDriveLink-0">62.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=62.png;FMTTYPE=image/png:https://drive.google.com/file/d/1dBWdFk5Bl72vfUO3ocr2MscwxvYdmgBy/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 63)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 63)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 63)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1hvuWdvivJ8PACr20J4A7dvMdmDP3aUUz/view?usp=sharing" class="pastedDriveLink-0">63.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=63.png;FMTTYPE=image/png:https://drive.google.com/file/d/1hvuWdvivJ8PACr20J4A7dvMdmDP3aUUz/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 64)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 64)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 64)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1vmI8i-aU3rU6HP0oKMI1TClelGSMYFOo/view?usp=sharing" class="pastedDriveLink-0">64.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=64.png;FMTTYPE=image/png:https://drive.google.com/file/d/1vmI8i-aU3rU6HP0oKMI1TClelGSMYFOo/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 65)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 65)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 65)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1HoPHv8Lcb0BQQRjmxiOvxRt5Q0UJeHNV/view?usp=sharing" class="pastedDriveLink-0">65.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=65.png;FMTTYPE=image/png:https://drive.google.com/file/d/1HoPHv8Lcb0BQQRjmxiOvxRt5Q0UJeHNV/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 66)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 66)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 66)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1bKxDCeBNRoPvOTFjPNV8nTb8ssmLLVaL/view?usp=sharing" class="pastedDriveLink-0">66.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=66.png;FMTTYPE=image/png:https://drive.google.com/file/d/1bKxDCeBNRoPvOTFjPNV8nTb8ssmLLVaL/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 67)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 67)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 67)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1doIDTRldm0W-OSdEh3yrvwNzXmUaRX3Q/view?usp=sharing" class="pastedDriveLink-0">67.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=67.png;FMTTYPE=image/png:https://drive.google.com/file/d/1doIDTRldm0W-OSdEh3yrvwNzXmUaRX3Q/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 68)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 68)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 68)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1pbnaIOIM6eRhGn995kx3BTvBd1diLI0W/view?usp=sharing" class="pastedDriveLink-0">68.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=68.png;FMTTYPE=image/png:https://drive.google.com/file/d/1pbnaIOIM6eRhGn995kx3BTvBd1diLI0W/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 69)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 69)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 69)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1aNRC2DYpkjFFFB5p-j-yqtBtLghSiP2W/view?usp=sharing" class="pastedDriveLink-0">69.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=69.png;FMTTYPE=image/png:https://drive.google.com/file/d/1aNRC2DYpkjFFFB5p-j-yqtBtLghSiP2W/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 70)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 70)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 70)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1vraCshnTrLmhuOV7siCYmtYMwlOpQZLG/view?usp=sharing" class="pastedDriveLink-0">70.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=70.png;FMTTYPE=image/png:https://drive.google.com/file/d/1vraCshnTrLmhuOV7siCYmtYMwlOpQZLG/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 71)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 71)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 71)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1XeaP2t5fvIjGzeiSaQkhSoFxyUQccCiY/view?usp=sharing" class="pastedDriveLink-0">71.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=71.png;FMTTYPE=image/png:https://drive.google.com/file/d/1XeaP2t5fvIjGzeiSaQkhSoFxyUQccCiY/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 72)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 72)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 72)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1M079u8QNLiI8hEqSQb5OrFIovQoxCofp/view?usp=sharing" class="pastedDriveLink-0">72.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=72.png;FMTTYPE=image/png:https://drive.google.com/file/d/1M079u8QNLiI8hEqSQb5OrFIovQoxCofp/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 73)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 73)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 73)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1yWRW4O_e8tbky8fx4q2MScTqT-knnp_l/view?usp=sharing" class="pastedDriveLink-0">73.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=73.png;FMTTYPE=image/png:https://drive.google.com/file/d/1yWRW4O_e8tbky8fx4q2MScTqT-knnp_l/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 74)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 74)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 74)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1goELXp_5E2t1X-zgzpj54M3qJ-_cROvN/view?usp=sharing" class="pastedDriveLink-0">74.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=74.png;FMTTYPE=image/png:https://drive.google.com/file/d/1goELXp_5E2t1X-zgzpj54M3qJ-_cROvN/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 75)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 75)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 75)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1x7OI_0BFGFjbt_EDADRXs4CnXCbuaXnT/view?usp=sharing" class="pastedDriveLink-0">75.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=75.png;FMTTYPE=image/png:https://drive.google.com/file/d/1x7OI_0BFGFjbt_EDADRXs4CnXCbuaXnT/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 76)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 76)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 76)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1AGPV3X8a8N57XgNUJsfmu8LtHux6HPJ4/view?usp=sharing" class="pastedDriveLink-0">76.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=76.png;FMTTYPE=image/png:https://drive.google.com/file/d/1AGPV3X8a8N57XgNUJsfmu8LtHux6HPJ4/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 77)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 77)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 77)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ZSdkaudrYFOAOdnlqliwc07FREKQQffb/view?usp=sharing" class="pastedDriveLink-0">77.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=77.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ZSdkaudrYFOAOdnlqliwc07FREKQQffb/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 78)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 78)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 78)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ikPOGs7NaFA6bR4YtlbG6AQQAY_Kv02c/view?usp=sharing" class="pastedDriveLink-0">78.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=78.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ikPOGs7NaFA6bR4YtlbG6AQQAY_Kv02c/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 79)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 79)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 79)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1eYdRNrAcasjNk151QLGQphMPKLE7_8am/view?usp=sharing" class="pastedDriveLink-0">79.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=79.png;FMTTYPE=image/png:https://drive.google.com/file/d/1eYdRNrAcasjNk151QLGQphMPKLE7_8am/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 80)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 80)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 80)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/14p_wTWWh8YTGJ2nAEf1a45UdF3kSYB0N/view?usp=sharing" class="pastedDriveLink-0">80.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=80.png;FMTTYPE=image/png:https://drive.google.com/file/d/14p_wTWWh8YTGJ2nAEf1a45UdF3kSYB0N/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 81)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 81)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 81)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/15u3iuADWWVBdKotUUJrgRBv0jTooE5pC/view?usp=sharing" class="pastedDriveLink-0">81.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=81.png;FMTTYPE=image/png:https://drive.google.com/file/d/15u3iuADWWVBdKotUUJrgRBv0jTooE5pC/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 82)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 82)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 82)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1y_LGxWuG09jYUjk3_mmTcO33Ijm6fru0/view?usp=sharing" class="pastedDriveLink-0">82.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=82.png;FMTTYPE=image/png:https://drive.google.com/file/d/1y_LGxWuG09jYUjk3_mmTcO33Ijm6fru0/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 83)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 83)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 83)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1_vWXhLTanFd6085a96GOvCgf_c2EGo5l/view?usp=sharing" class="pastedDriveLink-0">83.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=83.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_vWXhLTanFd6085a96GOvCgf_c2EGo5l/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 84)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 84)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 84)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/199qg9r6SlTSIw3DvNHmjnlnQ76l2Oitb/view?usp=sharing" class="pastedDriveLink-0">84.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=84.png;FMTTYPE=image/png:https://drive.google.com/file/d/199qg9r6SlTSIw3DvNHmjnlnQ76l2Oitb/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 85)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 85)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 85)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1CtbslUcbrsdXInJn3nlB0vadAVp4PI1p/view?usp=sharing" class="pastedDriveLink-0">85.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=85.png;FMTTYPE=image/png:https://drive.google.com/file/d/1CtbslUcbrsdXInJn3nlB0vadAVp4PI1p/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 86)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 86)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 86)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1h8bHPguFqdYuef_nZ0jtW44Ob5vahqV3/view?usp=sharing" class="pastedDriveLink-0">86.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=86.png;FMTTYPE=image/png:https://drive.google.com/file/d/1h8bHPguFqdYuef_nZ0jtW44Ob5vahqV3/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 87)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 87)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 87)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1vZ-UxPSR79FUkVK6KpK1Lo0NWWvdzMW5/view?usp=sharing" class="pastedDriveLink-0">87.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=87.png;FMTTYPE=image/png:https://drive.google.com/file/d/1vZ-UxPSR79FUkVK6KpK1Lo0NWWvdzMW5/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 88)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 88)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 88)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/178cggIW70SJqG3S5kb6dCmDtFNa2bVbR/view?usp=sharing" class="pastedDriveLink-0">88.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=88.png;FMTTYPE=image/png:https://drive.google.com/file/d/178cggIW70SJqG3S5kb6dCmDtFNa2bVbR/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 89)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 89)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 89)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1y5UykYfMnKvlg1XHjNSUTK17PQl-px2r/view?usp=sharing" class="pastedDriveLink-0">89.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=89.png;FMTTYPE=image/png:https://drive.google.com/file/d/1y5UykYfMnKvlg1XHjNSUTK17PQl-px2r/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 90)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 90)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 90)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1j_-2HCXeKcTHSY-WluriJeaJUNdNOAQ8/view?usp=sharing" class="pastedDriveLink-0">90.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=90.png;FMTTYPE=image/png:https://drive.google.com/file/d/1j_-2HCXeKcTHSY-WluriJeaJUNdNOAQ8/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 91)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 91)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 91)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1XH27xN6LKf8sj15-6P3Z0vUeGDv7gXsL/view?usp=sharing" class="pastedDriveLink-0">91.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=91.png;FMTTYPE=image/png:https://drive.google.com/file/d/1XH27xN6LKf8sj15-6P3Z0vUeGDv7gXsL/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 92)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 92)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 92)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1yFTC1WfS8RUDWlSabsmYBd1pKzJiDJNs/view?usp=sharing" class="pastedDriveLink-0">92.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=92.png;FMTTYPE=image/png:https://drive.google.com/file/d/1yFTC1WfS8RUDWlSabsmYBd1pKzJiDJNs/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 93)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 93)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 93)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1rq7Cg3gEGU8XfPb6BC308UFpm7ea9vr_/view?usp=sharing" class="pastedDriveLink-0">93.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=93.png;FMTTYPE=image/png:https://drive.google.com/file/d/1rq7Cg3gEGU8XfPb6BC308UFpm7ea9vr_/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 94)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 94)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 94)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1l85eJxpElKEuc_BKB5Z5HwPcAnpuNitx/view?usp=sharing" class="pastedDriveLink-0">94.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=94.png;FMTTYPE=image/png:https://drive.google.com/file/d/1l85eJxpElKEuc_BKB5Z5HwPcAnpuNitx/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 95)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 95)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 95)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/10bh0MPdAMJMqCS4kujY40f39q3hvdc1c/view?usp=sharing" class="pastedDriveLink-0">95.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=95.png;FMTTYPE=image/png:https://drive.google.com/file/d/10bh0MPdAMJMqCS4kujY40f39q3hvdc1c/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 96)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 96)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 96)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1tucsEbW2oVSw48rxxGDZ8_LTBMt2Wq17/view?usp=sharing" class="pastedDriveLink-0">96.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=96.png;FMTTYPE=image/png:https://drive.google.com/file/d/1tucsEbW2oVSw48rxxGDZ8_LTBMt2Wq17/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 97)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 97)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 97)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1VnzkRAXtG9i3g_jEKu2EkJ130nCuLaNW/view?usp=sharing" class="pastedDriveLink-0">97.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=97.png;FMTTYPE=image/png:https://drive.google.com/file/d/1VnzkRAXtG9i3g_jEKu2EkJ130nCuLaNW/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 98)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 98)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 98)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1GHJs-F-4o9LaXJcRiojczNFdWA2zZtQM/view?usp=sharing" class="pastedDriveLink-0">98.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=98.png;FMTTYPE=image/png:https://drive.google.com/file/d/1GHJs-F-4o9LaXJcRiojczNFdWA2zZtQM/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 99)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 99)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 99)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1CVj2v9PJ01vwqlx7R3ainFOi6MpcEdfY/view?usp=sharing" class="pastedDriveLink-0">99.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=99.png;FMTTYPE=image/png:https://drive.google.com/file/d/1CVj2v9PJ01vwqlx7R3ainFOi6MpcEdfY/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 100)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 100)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 100)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1_ooo90IoBgvtQF0U-mo9gO8fSsyy_jHE/view?usp=sharing" class="pastedDriveLink-0">100.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=100.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_ooo90IoBgvtQF0U-mo9gO8fSsyy_jHE/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 101)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 101)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 101)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1wAQlcOAjRc4EKAft_ZFyz21z3GfjWKe8/view?usp=sharing" class="pastedDriveLink-0">101.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=101.png;FMTTYPE=image/png:https://drive.google.com/file/d/1wAQlcOAjRc4EKAft_ZFyz21z3GfjWKe8/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 102)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 102)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 102)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Gd8PcP3Zi6oFAPLd-1z1ZCUTgmZWFeVb/view?usp=sharing" class="pastedDriveLink-0">102.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=102.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Gd8PcP3Zi6oFAPLd-1z1ZCUTgmZWFeVb/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 103)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 103)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 103)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1rH4vn3pYB6tERsFbV7cxWspdLj9BHa-3/view?usp=sharing" class="pastedDriveLink-0">103.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=103.png;FMTTYPE=image/png:https://drive.google.com/file/d/1rH4vn3pYB6tERsFbV7cxWspdLj9BHa-3/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 104)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 104)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 104)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1z7IgY-y3FRMEnP2rLm_o1ZzCi41hUn89/view?usp=sharing" class="pastedDriveLink-0">104.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=104.png;FMTTYPE=image/png:https://drive.google.com/file/d/1z7IgY-y3FRMEnP2rLm_o1ZzCi41hUn89/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 105)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 105)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 105)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1wQ5-pwPEhY-niE_HN1Pct9B5GmtXH4ZU/view?usp=sharing" class="pastedDriveLink-0">105.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=105.png;FMTTYPE=image/png:https://drive.google.com/file/d/1wQ5-pwPEhY-niE_HN1Pct9B5GmtXH4ZU/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 106)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 106)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 106)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1g_qp7nLL6q5kfMwR-CMqyJlRP31F06k-/view?usp=sharing" class="pastedDriveLink-0">106.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=106.png;FMTTYPE=image/png:https://drive.google.com/file/d/1g_qp7nLL6q5kfMwR-CMqyJlRP31F06k-/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 107)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 107)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 107)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1KT1sl8DHbBzBvWTqL5IM8czbo4cZ8jU1/view?usp=sharing" class="pastedDriveLink-0">107.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=107.png;FMTTYPE=image/png:https://drive.google.com/file/d/1KT1sl8DHbBzBvWTqL5IM8czbo4cZ8jU1/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 108)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 108)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 108)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1u0td60RmEZckvBsZ9mmziqN1xsl0SqmR/view?usp=sharing" class="pastedDriveLink-0">108.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=108.png;FMTTYPE=image/png:https://drive.google.com/file/d/1u0td60RmEZckvBsZ9mmziqN1xsl0SqmR/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 109)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 109)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 109)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1HUVKDTsYCXU_8f60j-b7WGiUM0jM1ggU/view?usp=sharing" class="pastedDriveLink-0">109.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=109.png;FMTTYPE=image/png:https://drive.google.com/file/d/1HUVKDTsYCXU_8f60j-b7WGiUM0jM1ggU/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 110)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 110)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 110)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1lHp9YHJEgDlRwo3PaumK5870vFeipEuZ/view?usp=sharing" class="pastedDriveLink-0">110.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=110.png;FMTTYPE=image/png:https://drive.google.com/file/d/1lHp9YHJEgDlRwo3PaumK5870vFeipEuZ/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 111)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 111)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 111)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ZYvS36XhvTi9kpnmg5VC0RBJKo4n1moN/view?usp=sharing" class="pastedDriveLink-0">111.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=111.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ZYvS36XhvTi9kpnmg5VC0RBJKo4n1moN/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 112)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 112)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 112)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1hkk6BX-0whDDvi3M_XkEUM2LTb-gz-4J/view?usp=sharing" class="pastedDriveLink-0">112.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=112.png;FMTTYPE=image/png:https://drive.google.com/file/d/1hkk6BX-0whDDvi3M_XkEUM2LTb-gz-4J/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 113)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 113)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 113)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Tt_-qc7Na9G5QZ1X1VuWHy4igL_KksFW/view?usp=sharing" class="pastedDriveLink-0">113.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=113.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Tt_-qc7Na9G5QZ1X1VuWHy4igL_KksFW/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 114)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 114)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 114)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1glQBczPlbUz6StiVBQkfRY79eoAASJpe/view?usp=sharing" class="pastedDriveLink-0">114.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=114.png;FMTTYPE=image/png:https://drive.google.com/file/d/1glQBczPlbUz6StiVBQkfRY79eoAASJpe/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 115)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 115)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 115)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1wf3ymLDy-6TjdUDsu27CGbyc_v6yeyGR/view?usp=sharing" class="pastedDriveLink-0">115.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=115.png;FMTTYPE=image/png:https://drive.google.com/file/d/1wf3ymLDy-6TjdUDsu27CGbyc_v6yeyGR/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 116)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 116)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 116)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1-QyR5Fa1McIsc2w4rW6ek2BN71Ty0rUN/view?usp=sharing" class="pastedDriveLink-0">116.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=116.png;FMTTYPE=image/png:https://drive.google.com/file/d/1-QyR5Fa1McIsc2w4rW6ek2BN71Ty0rUN/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 117)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 117)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 117)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1K9o6V5ygtQJyTLl0BSFKwdsWdqoX0E4b/view?usp=sharing" class="pastedDriveLink-0">117.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=117.png;FMTTYPE=image/png:https://drive.google.com/file/d/1K9o6V5ygtQJyTLl0BSFKwdsWdqoX0E4b/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 118)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 118)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 118)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1W026qZa1McJ6hlD6z3Ue1VbI1O_D6xAN/view?usp=sharing" class="pastedDriveLink-0">118.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=118.png;FMTTYPE=image/png:https://drive.google.com/file/d/1W026qZa1McJ6hlD6z3Ue1VbI1O_D6xAN/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 119)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 119)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 119)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/10om1ysorNGmnWgOM_1mTzOUZUxCZv8bo/view?usp=sharing" class="pastedDriveLink-0">119.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=119.png;FMTTYPE=image/png:https://drive.google.com/file/d/10om1ysorNGmnWgOM_1mTzOUZUxCZv8bo/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 120)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 120)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 120)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1pvwryjnz3HX46QPisdTgb8Q2GnRie_Vr/view?usp=sharing" class="pastedDriveLink-0">120.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=120.png;FMTTYPE=image/png:https://drive.google.com/file/d/1pvwryjnz3HX46QPisdTgb8Q2GnRie_Vr/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 121)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 121)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 121)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1tRsqqOQNDbROFIHuAL-vgjfQ0EcP7QgL/view?usp=sharing" class="pastedDriveLink-0">121.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=121.png;FMTTYPE=image/png:https://drive.google.com/file/d/1tRsqqOQNDbROFIHuAL-vgjfQ0EcP7QgL/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 122)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 122)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 122)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Cu4j0PSw_OsVhDyM7rns-n0uvuM-U3sO/view?usp=sharing" class="pastedDriveLink-0">122.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=122.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Cu4j0PSw_OsVhDyM7rns-n0uvuM-U3sO/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 123)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 123)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 123)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1c1mhOhVewH0nOapHE1pEvxoG_cUcpY5T/view?usp=sharing" class="pastedDriveLink-0">123.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=123.png;FMTTYPE=image/png:https://drive.google.com/file/d/1c1mhOhVewH0nOapHE1pEvxoG_cUcpY5T/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 124)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 124)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 124)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1br67EOQCjReyKSDgPVyGvpcYgUND-rOv/view?usp=sharing" class="pastedDriveLink-0">124.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=124.png;FMTTYPE=image/png:https://drive.google.com/file/d/1br67EOQCjReyKSDgPVyGvpcYgUND-rOv/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 125)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 125)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 125)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/10xiGcdchyaxBSUq0_Ol1cIaGQOuTn6AJ/view?usp=sharing" class="pastedDriveLink-0">125.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=125.png;FMTTYPE=image/png:https://drive.google.com/file/d/10xiGcdchyaxBSUq0_Ol1cIaGQOuTn6AJ/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 126)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 126)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 126)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/18z1SB9wtFeqevQIYpglsj8OEMzndBLj8/view?usp=sharing" class="pastedDriveLink-0">126.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=126.png;FMTTYPE=image/png:https://drive.google.com/file/d/18z1SB9wtFeqevQIYpglsj8OEMzndBLj8/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 127)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 127)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 127)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1znhFavcFpR7VUWwKlba61depaYMAtWxq/view?usp=sharing" class="pastedDriveLink-0">127.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=127.png;FMTTYPE=image/png:https://drive.google.com/file/d/1znhFavcFpR7VUWwKlba61depaYMAtWxq/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 128)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 128)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 128)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1hbnQmeE-hHmm-YrSLa0yAN7Uuxnncsz-/view?usp=sharing" class="pastedDriveLink-0">128.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=128.png;FMTTYPE=image/png:https://drive.google.com/file/d/1hbnQmeE-hHmm-YrSLa0yAN7Uuxnncsz-/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 129)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 129)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 129)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1lottQ_av94XTGBpLVpOr0N690YLs7QZY/view?usp=sharing" class="pastedDriveLink-0">129.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=129.png;FMTTYPE=image/png:https://drive.google.com/file/d/1lottQ_av94XTGBpLVpOr0N690YLs7QZY/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 130)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 130)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 130)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1xvuqpjbWFg6l_ptecopg-Mm1cwdql4Jd/view?usp=sharing" class="pastedDriveLink-0">130.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=130.png;FMTTYPE=image/png:https://drive.google.com/file/d/1xvuqpjbWFg6l_ptecopg-Mm1cwdql4Jd/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 131)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 131)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 131)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1OQ-X0rqytGRY0wSm6MSglVMnjs2nc_78/view?usp=sharing" class="pastedDriveLink-0">131.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=131.png;FMTTYPE=image/png:https://drive.google.com/file/d/1OQ-X0rqytGRY0wSm6MSglVMnjs2nc_78/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 132)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 132)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 132)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/18QUYhHU4dsOrC-xjnMemuyVHZ3q_FRph/view?usp=sharing" class="pastedDriveLink-0">132.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=132.png;FMTTYPE=image/png:https://drive.google.com/file/d/18QUYhHU4dsOrC-xjnMemuyVHZ3q_FRph/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 133)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 133)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 133)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1HQ6jy4mENpXk364O_OlU9CzPbwhxyz3k/view?usp=sharing" class="pastedDriveLink-0">133.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=133.png;FMTTYPE=image/png:https://drive.google.com/file/d/1HQ6jy4mENpXk364O_OlU9CzPbwhxyz3k/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 134)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 134)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 134)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1aAuqmf_ugD8KR0GGTvmnz4pYvxImr5cC/view?usp=sharing" class="pastedDriveLink-0">134.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=134.png;FMTTYPE=image/png:https://drive.google.com/file/d/1aAuqmf_ugD8KR0GGTvmnz4pYvxImr5cC/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 135)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 135)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 135)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1iL5WZwj1Xn7C_qmsq7T6Pw24tPFpjJQ5/view?usp=sharing" class="pastedDriveLink-0">135.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=135.png;FMTTYPE=image/png:https://drive.google.com/file/d/1iL5WZwj1Xn7C_qmsq7T6Pw24tPFpjJQ5/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 136)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 136)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 136)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Zrlt6USClR5FtXGnjQ7BGmaH-6fz7SU0/view?usp=sharing" class="pastedDriveLink-0">136.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=136.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Zrlt6USClR5FtXGnjQ7BGmaH-6fz7SU0/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 137)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 137)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 137)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1GRdp_tkLh0LQJO2LWtv0PXOk54HdoIzr/view?usp=sharing" class="pastedDriveLink-0">137.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=137.png;FMTTYPE=image/png:https://drive.google.com/file/d/1GRdp_tkLh0LQJO2LWtv0PXOk54HdoIzr/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 138)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 138)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 138)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1q7YFcvpf8gCUJGfB1oZaXjo6cpsIkaSe/view?usp=sharing" class="pastedDriveLink-0">138.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=138.png;FMTTYPE=image/png:https://drive.google.com/file/d/1q7YFcvpf8gCUJGfB1oZaXjo6cpsIkaSe/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 139)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 139)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 139)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1s1kmOgBtMG8c74Je-QVBep0a4GUaJnLF/view?usp=sharing" class="pastedDriveLink-0">139.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=139.png;FMTTYPE=image/png:https://drive.google.com/file/d/1s1kmOgBtMG8c74Je-QVBep0a4GUaJnLF/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 140)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 140)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 140)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1WJ0GagZAr10pbf3CyDgHARyg2WfKILxp/view?usp=sharing" class="pastedDriveLink-0">140.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=140.png;FMTTYPE=image/png:https://drive.google.com/file/d/1WJ0GagZAr10pbf3CyDgHARyg2WfKILxp/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 141)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 141)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 141)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Ail2uIvGaWYazY9tofoFcoX4oQ4fU0ID/view?usp=sharing" class="pastedDriveLink-0">141.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=141.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Ail2uIvGaWYazY9tofoFcoX4oQ4fU0ID/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 142)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 142)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 142)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1P9si2HqGm8CSWOYKDgNoi9qQTMTF9ohD/view?usp=sharing" class="pastedDriveLink-0">142.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=142.png;FMTTYPE=image/png:https://drive.google.com/file/d/1P9si2HqGm8CSWOYKDgNoi9qQTMTF9ohD/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 143)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 143)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 143)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1iTYbllq18y0ZKTiXJPAvdZKnLM7pvR-F/view?usp=sharing" class="pastedDriveLink-0">143.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=143.png;FMTTYPE=image/png:https://drive.google.com/file/d/1iTYbllq18y0ZKTiXJPAvdZKnLM7pvR-F/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 144)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 144)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 144)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1qGFFs2uoZOEILcJPAwvHsTnXekqLp6S5/view?usp=sharing" class="pastedDriveLink-0">144.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=144.png;FMTTYPE=image/png:https://drive.google.com/file/d/1qGFFs2uoZOEILcJPAwvHsTnXekqLp6S5/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 145)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 145)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 145)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1W9BZgmfMrFo9Uh6y3Y4YR-y-x5Yyx3wY/view?usp=sharing" class="pastedDriveLink-0">145.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=145.png;FMTTYPE=image/png:https://drive.google.com/file/d/1W9BZgmfMrFo9Uh6y3Y4YR-y-x5Yyx3wY/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 146)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 146)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 146)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1YLdowu612HhwsAc4OS0Ip9LBm8lEmOVY/view?usp=sharing" class="pastedDriveLink-0">146.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=146.png;FMTTYPE=image/png:https://drive.google.com/file/d/1YLdowu612HhwsAc4OS0Ip9LBm8lEmOVY/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 147)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 147)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 147)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1LiNNS1KD8mXJsi_MhwRtwRd5HAzCoGl5/view?usp=sharing" class="pastedDriveLink-0">147.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=147.png;FMTTYPE=image/png:https://drive.google.com/file/d/1LiNNS1KD8mXJsi_MhwRtwRd5HAzCoGl5/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 148)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 148)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 148)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1nDOnEMCF5diU2QSfF1UNlLb_1kvVIrcK/view?usp=sharing" class="pastedDriveLink-0">148.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=148.png;FMTTYPE=image/png:https://drive.google.com/file/d/1nDOnEMCF5diU2QSfF1UNlLb_1kvVIrcK/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 149)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 149)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 149)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Ufv-WibD1UfoA477qlpEpTv9fxing9Fv/view?usp=sharing" class="pastedDriveLink-0">149.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=149.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Ufv-WibD1UfoA477qlpEpTv9fxing9Fv/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 150)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 150)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 150)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1foPK1DuVNfNqKDoNjxfLLFEJJ1F4kORi/view?usp=sharing" class="pastedDriveLink-0">150.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=150.png;FMTTYPE=image/png:https://drive.google.com/file/d/1foPK1DuVNfNqKDoNjxfLLFEJJ1F4kORi/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 151)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 151)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 151)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1w3ZPIHlGQ-AzQHgXAqu2MGryYQ0H99yr/view?usp=sharing" class="pastedDriveLink-0">151.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=151.png;FMTTYPE=image/png:https://drive.google.com/file/d/1w3ZPIHlGQ-AzQHgXAqu2MGryYQ0H99yr/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 152)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 152)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 152)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1mDavNKQEk7J9nkvE30JmlJPLBNFFJcNF/view?usp=sharing" class="pastedDriveLink-0">152.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=152.png;FMTTYPE=image/png:https://drive.google.com/file/d/1mDavNKQEk7J9nkvE30JmlJPLBNFFJcNF/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 153)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 153)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 153)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1DNe0CfASOdUIwtFebLQjwBwDVt5wnObJ/view?usp=sharing" class="pastedDriveLink-0">153.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=153.png;FMTTYPE=image/png:https://drive.google.com/file/d/1DNe0CfASOdUIwtFebLQjwBwDVt5wnObJ/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 154)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 154)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 154)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1eJTQr5PmGYOLTXVioIfD6gsh7VPGxmnH/view?usp=sharing" class="pastedDriveLink-0">154.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=154.png;FMTTYPE=image/png:https://drive.google.com/file/d/1eJTQr5PmGYOLTXVioIfD6gsh7VPGxmnH/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 155)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 155)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 155)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/16s8TNd5-QhVLGEuSfiTg3y27-u2Aqdvs/view?usp=sharing" class="pastedDriveLink-0">155.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=155.png;FMTTYPE=image/png:https://drive.google.com/file/d/16s8TNd5-QhVLGEuSfiTg3y27-u2Aqdvs/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 156)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 156)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 156)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1pIgKCVYQaMTGrrMtOAwNCfpNLBIHF6w9/view?usp=sharing" class="pastedDriveLink-0">156.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=156.png;FMTTYPE=image/png:https://drive.google.com/file/d/1pIgKCVYQaMTGrrMtOAwNCfpNLBIHF6w9/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 157)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 157)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 157)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1u5xa1AbJhzPvOd4ZbKXMuOeJYL27uqmY/view?usp=sharing" class="pastedDriveLink-0">157.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=157.png;FMTTYPE=image/png:https://drive.google.com/file/d/1u5xa1AbJhzPvOd4ZbKXMuOeJYL27uqmY/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 158)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 158)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 158)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1VpfJJt1hWmKKxRyEC6uFKtJyiBcl7E7b/view?usp=sharing" class="pastedDriveLink-0">158.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=158.png;FMTTYPE=image/png:https://drive.google.com/file/d/1VpfJJt1hWmKKxRyEC6uFKtJyiBcl7E7b/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 159)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 159)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 159)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1CFnDKW6U8R67X79fDYCpDzXNZ6kh5rUx/view?usp=sharing" class="pastedDriveLink-0">159.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=159.png;FMTTYPE=image/png:https://drive.google.com/file/d/1CFnDKW6U8R67X79fDYCpDzXNZ6kh5rUx/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 160)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 160)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 160)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1mec30XNDdcR5SC-VIz2sRrmm7-k126As/view?usp=sharing" class="pastedDriveLink-0">160.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=160.png;FMTTYPE=image/png:https://drive.google.com/file/d/1mec30XNDdcR5SC-VIz2sRrmm7-k126As/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 161)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 161)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 161)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1r2Gj46s90bliIZx9hjbrvzTooMOKRVF3/view?usp=sharing" class="pastedDriveLink-0">161.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=161.png;FMTTYPE=image/png:https://drive.google.com/file/d/1r2Gj46s90bliIZx9hjbrvzTooMOKRVF3/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 162)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 162)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 162)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Fbz0rq1s87M5oBEfTkv0BFkz8GMSyLhO/view?usp=sharing" class="pastedDriveLink-0">162.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=162.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Fbz0rq1s87M5oBEfTkv0BFkz8GMSyLhO/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 163)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 163)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 163)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1OtenBJ6jjBNoVN_jdrnmnprTsNsOe8Oa/view?usp=sharing" class="pastedDriveLink-0">163.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=163.png;FMTTYPE=image/png:https://drive.google.com/file/d/1OtenBJ6jjBNoVN_jdrnmnprTsNsOe8Oa/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 164)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 164)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 164)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Unzal1uXqm3KK-rK5-N1Sq9Mq-PmXrao/view?usp=sharing" class="pastedDriveLink-0">164.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=164.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Unzal1uXqm3KK-rK5-N1Sq9Mq-PmXrao/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 165)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 165)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 165)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/16J4OKvL6p7aZD_KqUxhcEDNX-hc4Ajk0/view?usp=sharing" class="pastedDriveLink-0">165.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=165.png;FMTTYPE=image/png:https://drive.google.com/file/d/16J4OKvL6p7aZD_KqUxhcEDNX-hc4Ajk0/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 166)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 166)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 166)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1bcIKzC-TONhMEns9MwZArvdOn11eEEg2/view?usp=sharing" class="pastedDriveLink-0">166.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=166.png;FMTTYPE=image/png:https://drive.google.com/file/d/1bcIKzC-TONhMEns9MwZArvdOn11eEEg2/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 167)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 167)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 167)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1pOhPWIwbj06E5agZIJHC97sP5zhvlC0k/view?usp=sharing" class="pastedDriveLink-0">167.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=167.png;FMTTYPE=image/png:https://drive.google.com/file/d/1pOhPWIwbj06E5agZIJHC97sP5zhvlC0k/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 168)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 168)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 168)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1SdTTwjC7p9gFxe3HtTLYqCNa6vQgM8xc/view?usp=sharing" class="pastedDriveLink-0">168.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=168.png;FMTTYPE=image/png:https://drive.google.com/file/d/1SdTTwjC7p9gFxe3HtTLYqCNa6vQgM8xc/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 169)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 169)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 169)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1TwhcFndEOWKa1z0paFj-gaUj4xS-_MyN/view?usp=sharing" class="pastedDriveLink-0">169.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=169.png;FMTTYPE=image/png:https://drive.google.com/file/d/1TwhcFndEOWKa1z0paFj-gaUj4xS-_MyN/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 170)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 170)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 170)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1kkqY1LsA07aX6e_hr6F50kEhpqK3iyqS/view?usp=sharing" class="pastedDriveLink-0">170.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=170.png;FMTTYPE=image/png:https://drive.google.com/file/d/1kkqY1LsA07aX6e_hr6F50kEhpqK3iyqS/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 171)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 171)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 171)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1cq08wxGPqJYq3pc02VfKaVqX3IOz1uAm/view?usp=sharing" class="pastedDriveLink-0">171.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=171.png;FMTTYPE=image/png:https://drive.google.com/file/d/1cq08wxGPqJYq3pc02VfKaVqX3IOz1uAm/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 172)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 172)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 172)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1EiilYmAkJs8eT1BN0I-Yf6fFGei50zRF/view?usp=sharing" class="pastedDriveLink-0">172.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=172.png;FMTTYPE=image/png:https://drive.google.com/file/d/1EiilYmAkJs8eT1BN0I-Yf6fFGei50zRF/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 173)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 173)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 173)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1_5W8VVR2oH9ffIn8xwWE1LBycblCEIGs/view?usp=sharing" class="pastedDriveLink-0">173.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=173.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_5W8VVR2oH9ffIn8xwWE1LBycblCEIGs/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 174)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 174)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 174)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1aNv6THGJpVEq3NjjAXv1X-F6XJ2rIDXA/view?usp=sharing" class="pastedDriveLink-0">174.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=174.png;FMTTYPE=image/png:https://drive.google.com/file/d/1aNv6THGJpVEq3NjjAXv1X-F6XJ2rIDXA/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 175)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 175)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 175)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1pmadStsfutJtnUixSlmQ6jSOZ490r6pV/view?usp=sharing" class="pastedDriveLink-0">175.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=175.png;FMTTYPE=image/png:https://drive.google.com/file/d/1pmadStsfutJtnUixSlmQ6jSOZ490r6pV/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 176)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 176)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 176)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1vIcejeWbA1zJZiqdXGJy0pwsxeeuZFOp/view?usp=sharing" class="pastedDriveLink-0">176.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=176.png;FMTTYPE=image/png:https://drive.google.com/file/d/1vIcejeWbA1zJZiqdXGJy0pwsxeeuZFOp/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 177)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 177)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 177)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1hpqmU7EG1a1lbl7__c0LJi2-m3wuW2Vt/view?usp=sharing" class="pastedDriveLink-0">177.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=177.png;FMTTYPE=image/png:https://drive.google.com/file/d/1hpqmU7EG1a1lbl7__c0LJi2-m3wuW2Vt/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 178)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 178)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 178)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1GaNAk8U79keTaaNEGu2k_ts8mt7YbSa4/view?usp=sharing" class="pastedDriveLink-0">178.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=178.png;FMTTYPE=image/png:https://drive.google.com/file/d/1GaNAk8U79keTaaNEGu2k_ts8mt7YbSa4/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 179)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 179)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 179)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1oHBsIPX0jycre4h5nijEN75QSfssu_Sl/view?usp=sharing" class="pastedDriveLink-0">179.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=179.png;FMTTYPE=image/png:https://drive.google.com/file/d/1oHBsIPX0jycre4h5nijEN75QSfssu_Sl/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 180)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 180)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 180)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ShAxaekZFdyl-apqcJbuQ4ya1N1dTBj5/view?usp=sharing" class="pastedDriveLink-0">180.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=180.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ShAxaekZFdyl-apqcJbuQ4ya1N1dTBj5/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 181)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 181)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 181)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1YyDpQxt-vd5NjX58_BJxdVJ8-_vjVoRq/view?usp=sharing" class="pastedDriveLink-0">181.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=181.png;FMTTYPE=image/png:https://drive.google.com/file/d/1YyDpQxt-vd5NjX58_BJxdVJ8-_vjVoRq/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 182)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 182)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 182)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Bzzq4ghZ5eYmgn7y_u3VSCMibqNmMgOG/view?usp=sharing" class="pastedDriveLink-0">182.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=182.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Bzzq4ghZ5eYmgn7y_u3VSCMibqNmMgOG/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 183)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 183)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 183)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1AYFvXyY4gE8-TdoLTyL_yAuhfky5gg3R/view?usp=sharing" class="pastedDriveLink-0">183.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=183.png;FMTTYPE=image/png:https://drive.google.com/file/d/1AYFvXyY4gE8-TdoLTyL_yAuhfky5gg3R/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 184)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 184)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 184)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1hUiUHUsVTxI0JrHfSQznyiiRylqNh2NX/view?usp=sharing" class="pastedDriveLink-0">184.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=184.png;FMTTYPE=image/png:https://drive.google.com/file/d/1hUiUHUsVTxI0JrHfSQznyiiRylqNh2NX/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 185)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 185)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 185)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1I9-LDqTVnaDLTGRnfCQ7al1WORF-q3ld/view?usp=sharing" class="pastedDriveLink-0">185.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=185.png;FMTTYPE=image/png:https://drive.google.com/file/d/1I9-LDqTVnaDLTGRnfCQ7al1WORF-q3ld/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 186)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 186)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 186)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1BJrkZtvNTdQ1E6Xa0aDA6ECRHjABe6Mu/view?usp=sharing" class="pastedDriveLink-0">186.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=186.png;FMTTYPE=image/png:https://drive.google.com/file/d/1BJrkZtvNTdQ1E6Xa0aDA6ECRHjABe6Mu/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 187)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 187)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 187)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Zq3fkU7X9h8uMu6gV4deYXIAjeMZgdrG/view?usp=sharing" class="pastedDriveLink-0">187.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=187.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Zq3fkU7X9h8uMu6gV4deYXIAjeMZgdrG/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 188)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 188)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 188)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1lyMHEdpaUo2RGJE9Bjby2cLWk6aLtKBR/view?usp=sharing" class="pastedDriveLink-0">188.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=188.png;FMTTYPE=image/png:https://drive.google.com/file/d/1lyMHEdpaUo2RGJE9Bjby2cLWk6aLtKBR/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 189)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 189)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 189)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1U2XDY4YA1rWoOgrT5Jn7BK3szEh-UItO/view?usp=sharing" class="pastedDriveLink-0">189.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=189.png;FMTTYPE=image/png:https://drive.google.com/file/d/1U2XDY4YA1rWoOgrT5Jn7BK3szEh-UItO/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 190)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 190)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 190)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1DhFsqf7HEfErfH-7R7tqOIqHnV3Fhgt7/view?usp=sharing" class="pastedDriveLink-0">190.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=190.png;FMTTYPE=image/png:https://drive.google.com/file/d/1DhFsqf7HEfErfH-7R7tqOIqHnV3Fhgt7/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 191)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 191)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 191)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1mJLDqO7Kv883gXsvn1BLluyv6XNVkwBw/view?usp=sharing" class="pastedDriveLink-0">191.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=191.png;FMTTYPE=image/png:https://drive.google.com/file/d/1mJLDqO7Kv883gXsvn1BLluyv6XNVkwBw/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 192)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 192)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 192)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/197xWVuaTbC1xSKrFS59s5_hbHaUSGCNE/view?usp=sharing" class="pastedDriveLink-0">192.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=192.png;FMTTYPE=image/png:https://drive.google.com/file/d/197xWVuaTbC1xSKrFS59s5_hbHaUSGCNE/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 193)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 193)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 193)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1pZQS38eQ0d3BmzUBBunoQwkPai09qUwl/view?usp=sharing" class="pastedDriveLink-0">193.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=193.png;FMTTYPE=image/png:https://drive.google.com/file/d/1pZQS38eQ0d3BmzUBBunoQwkPai09qUwl/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 194)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 194)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 194)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/10Qgoovt0apzFdhFg5MAWz9snxp2u-Mp1/view?usp=sharing" class="pastedDriveLink-0">194.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=194.png;FMTTYPE=image/png:https://drive.google.com/file/d/10Qgoovt0apzFdhFg5MAWz9snxp2u-Mp1/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 195)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 195)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 195)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1wy9K8YzWqv7QIjToXhdQoIehc66U0P-a/view?usp=sharing" class="pastedDriveLink-0">195.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=195.png;FMTTYPE=image/png:https://drive.google.com/file/d/1wy9K8YzWqv7QIjToXhdQoIehc66U0P-a/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 196)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 196)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 196)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Fs0N9mf636BczW5hASZlZohcxAIHlWnU/view?usp=sharing" class="pastedDriveLink-0">196.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=196.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Fs0N9mf636BczW5hASZlZohcxAIHlWnU/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 197)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 197)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 197)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/12WnysJ45gO93Z0jLnZD8bz4PiFU1uHgk/view?usp=sharing" class="pastedDriveLink-0">197.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=197.png;FMTTYPE=image/png:https://drive.google.com/file/d/12WnysJ45gO93Z0jLnZD8bz4PiFU1uHgk/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 198)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 198)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 198)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1YxAJBwXinbTrP5DvVH90XSrHyIOt_BtD/view?usp=sharing" class="pastedDriveLink-0">198.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=198.png;FMTTYPE=image/png:https://drive.google.com/file/d/1YxAJBwXinbTrP5DvVH90XSrHyIOt_BtD/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 199)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 199)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 199)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1n8muN6GkoRSOdOgr-TpuGg4RKm57U4Zn/view?usp=sharing" class="pastedDriveLink-0">199.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=199.png;FMTTYPE=image/png:https://drive.google.com/file/d/1n8muN6GkoRSOdOgr-TpuGg4RKm57U4Zn/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 200)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 200)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 200)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1HTYM8mftfeAiklCEMG8dI1mSQ_0IbkmB/view?usp=sharing" class="pastedDriveLink-0">200.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=200.png;FMTTYPE=image/png:https://drive.google.com/file/d/1HTYM8mftfeAiklCEMG8dI1mSQ_0IbkmB/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 201)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 201)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 201)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Ap4dKYVuRMHcqQmo176oEy4_qGE_iQF-/view?usp=sharing" class="pastedDriveLink-0">201.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=201.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Ap4dKYVuRMHcqQmo176oEy4_qGE_iQF-/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 202)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 202)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 202)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1tEgPSw1UNtB8oh5K_aTBe62iXGf1mNxi/view?usp=sharing" class="pastedDriveLink-0">202.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=202.png;FMTTYPE=image/png:https://drive.google.com/file/d/1tEgPSw1UNtB8oh5K_aTBe62iXGf1mNxi/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 203)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 203)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 203)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/16ELeigeVWsVt98L1BBdEUArVILcDFPee/view?usp=sharing" class="pastedDriveLink-0">203.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=203.png;FMTTYPE=image/png:https://drive.google.com/file/d/16ELeigeVWsVt98L1BBdEUArVILcDFPee/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 204)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 204)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 204)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1fNhiWzXEnUYgOyFodbBTOobirIHuWhJb/view?usp=sharing" class="pastedDriveLink-0">204.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=204.png;FMTTYPE=image/png:https://drive.google.com/file/d/1fNhiWzXEnUYgOyFodbBTOobirIHuWhJb/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 205)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 205)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 205)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/16CW2-YLbIzPzm4xDSk76MtcmvIGImw6Z/view?usp=sharing" class="pastedDriveLink-0">205.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=205.png;FMTTYPE=image/png:https://drive.google.com/file/d/16CW2-YLbIzPzm4xDSk76MtcmvIGImw6Z/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 206)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 206)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 206)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/12MX2v-bD-NUwPcfJ0wtnxGktld1jcIXo/view?usp=sharing" class="pastedDriveLink-0">206.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=206.png;FMTTYPE=image/png:https://drive.google.com/file/d/12MX2v-bD-NUwPcfJ0wtnxGktld1jcIXo/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 207)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 207)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 207)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ISvhaTYwdTcTgs4xqMDaJ-n1Ytgm8iY7/view?usp=sharing" class="pastedDriveLink-0">207.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=207.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ISvhaTYwdTcTgs4xqMDaJ-n1Ytgm8iY7/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 208)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 208)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 208)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1v-EkF4IUmgTyAS6SzOVL0FLKNPQVpB3C/view?usp=sharing" class="pastedDriveLink-0">208.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=208.png;FMTTYPE=image/png:https://drive.google.com/file/d/1v-EkF4IUmgTyAS6SzOVL0FLKNPQVpB3C/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 209)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 209)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 209)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1jbb9BAdYD3Lh488WxTpSdNaSMNrHgQ1L/view?usp=sharing" class="pastedDriveLink-0">209.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=209.png;FMTTYPE=image/png:https://drive.google.com/file/d/1jbb9BAdYD3Lh488WxTpSdNaSMNrHgQ1L/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 210)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 210)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 210)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1gqW0tahoW3gI33ccQSiT-3CVJD9-9ivl/view?usp=sharing" class="pastedDriveLink-0">210.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=210.png;FMTTYPE=image/png:https://drive.google.com/file/d/1gqW0tahoW3gI33ccQSiT-3CVJD9-9ivl/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 211)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 211)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 211)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1BX7UQDcuKEzTciO3v4G8D4Dl3sfmTN-7/view?usp=sharing" class="pastedDriveLink-0">211.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=211.png;FMTTYPE=image/png:https://drive.google.com/file/d/1BX7UQDcuKEzTciO3v4G8D4Dl3sfmTN-7/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 212)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 212)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 212)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1iaPC02yn2M5GgZjYNZKx_JKlGSObROjQ/view?usp=sharing" class="pastedDriveLink-0">212.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=212.png;FMTTYPE=image/png:https://drive.google.com/file/d/1iaPC02yn2M5GgZjYNZKx_JKlGSObROjQ/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 213)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 213)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 213)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1S6ql6zzN7B_xELQ62h_uL1zzTqC7KPzd/view?usp=sharing" class="pastedDriveLink-0">213.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=213.png;FMTTYPE=image/png:https://drive.google.com/file/d/1S6ql6zzN7B_xELQ62h_uL1zzTqC7KPzd/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 214)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 214)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 214)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Ufsj4Vbp7Z0wKwrgRBeyykujPvweYLPH/view?usp=sharing" class="pastedDriveLink-0">214.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=214.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Ufsj4Vbp7Z0wKwrgRBeyykujPvweYLPH/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 215)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 215)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 215)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1vnhXpwzXbRBoN6QqnhfBrM90edxXi_8n/view?usp=sharing" class="pastedDriveLink-0">215.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=215.png;FMTTYPE=image/png:https://drive.google.com/file/d/1vnhXpwzXbRBoN6QqnhfBrM90edxXi_8n/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 216)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 216)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 216)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1GNohJBQnZn5av9JMo4h6dpJ_EvNd5ACm/view?usp=sharing" class="pastedDriveLink-0">216.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=216.png;FMTTYPE=image/png:https://drive.google.com/file/d/1GNohJBQnZn5av9JMo4h6dpJ_EvNd5ACm/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 217)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 217)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 217)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1WmF5BAGMfD63bWB2WiXvOW31FayAzvAL/view?usp=sharing" class="pastedDriveLink-0">217.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=217.png;FMTTYPE=image/png:https://drive.google.com/file/d/1WmF5BAGMfD63bWB2WiXvOW31FayAzvAL/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 218)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 218)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 218)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1lrxF6ZFI-CG3_E8QdI_EUPd6rbgLaFFU/view?usp=sharing" class="pastedDriveLink-0">218.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=218.png;FMTTYPE=image/png:https://drive.google.com/file/d/1lrxF6ZFI-CG3_E8QdI_EUPd6rbgLaFFU/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 219)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 219)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 219)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1cav26nuagLhytEfMVsDHJe0I1P9_IZM6/view?usp=sharing" class="pastedDriveLink-0">219.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=219.png;FMTTYPE=image/png:https://drive.google.com/file/d/1cav26nuagLhytEfMVsDHJe0I1P9_IZM6/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 220)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 220)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 220)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1HY-dwrWkXiPPKtGZWh2-tJ6XVXIJFTS-/view?usp=sharing" class="pastedDriveLink-0">220.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=220.png;FMTTYPE=image/png:https://drive.google.com/file/d/1HY-dwrWkXiPPKtGZWh2-tJ6XVXIJFTS-/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 221)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 221)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 221)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1x09oqkZezqvhQ6W2HPyiSl21FzPNFF5Z/view?usp=sharing" class="pastedDriveLink-0">221.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=221.png;FMTTYPE=image/png:https://drive.google.com/file/d/1x09oqkZezqvhQ6W2HPyiSl21FzPNFF5Z/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 222)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 222)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 222)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1wenXN75H7uVqSH69O9_k29CgjGlI2Zrc/view?usp=sharing" class="pastedDriveLink-0">222.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=222.png;FMTTYPE=image/png:https://drive.google.com/file/d/1wenXN75H7uVqSH69O9_k29CgjGlI2Zrc/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 223)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 223)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 223)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1nHj-swVQseboGYgXyTlJ8BMVYXSuQ3R4/view?usp=sharing" class="pastedDriveLink-0">223.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=223.png;FMTTYPE=image/png:https://drive.google.com/file/d/1nHj-swVQseboGYgXyTlJ8BMVYXSuQ3R4/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 224)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 224)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 224)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1X4BgcS-pYfDRFLTEjxpT3L-m0K_r-KAE/view?usp=sharing" class="pastedDriveLink-0">224.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=224.png;FMTTYPE=image/png:https://drive.google.com/file/d/1X4BgcS-pYfDRFLTEjxpT3L-m0K_r-KAE/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 225)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 225)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 225)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ZewNtqm23H92GMHsQFDK05C5QnZTIc8T/view?usp=sharing" class="pastedDriveLink-0">225.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=225.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ZewNtqm23H92GMHsQFDK05C5QnZTIc8T/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 226)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 226)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 226)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1BYYWzXR6t4ypA23Iox2UVDKpd9d4AMS9/view?usp=sharing" class="pastedDriveLink-0">226.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=226.png;FMTTYPE=image/png:https://drive.google.com/file/d/1BYYWzXR6t4ypA23Iox2UVDKpd9d4AMS9/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 227)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 227)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 227)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1qYfQKYdnrVWKUf_MUeE0FsL3Gi_Oxgcq/view?usp=sharing" class="pastedDriveLink-0">227.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=227.png;FMTTYPE=image/png:https://drive.google.com/file/d/1qYfQKYdnrVWKUf_MUeE0FsL3Gi_Oxgcq/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 228)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 228)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 228)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1u2-iYx19VKFCxf3UJgFx6LnUq3DTx6GB/view?usp=sharing" class="pastedDriveLink-0">228.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=228.png;FMTTYPE=image/png:https://drive.google.com/file/d/1u2-iYx19VKFCxf3UJgFx6LnUq3DTx6GB/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 229)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 229)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 229)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1-_ww5r2cToKwu5HoBtslJCSs6TZtlerr/view?usp=sharing" class="pastedDriveLink-0">229.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=229.png;FMTTYPE=image/png:https://drive.google.com/file/d/1-_ww5r2cToKwu5HoBtslJCSs6TZtlerr/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 230)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 230)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 230)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/109AGqCv4VYjg2ina-P7T49JDyk2W4WCT/view?usp=sharing" class="pastedDriveLink-0">230.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=230.png;FMTTYPE=image/png:https://drive.google.com/file/d/109AGqCv4VYjg2ina-P7T49JDyk2W4WCT/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 231)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 231)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 231)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/12R0rZh9ojPsC_Rn91SiskzwlT05c_2z0/view?usp=sharing" class="pastedDriveLink-0">231.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=231.png;FMTTYPE=image/png:https://drive.google.com/file/d/12R0rZh9ojPsC_Rn91SiskzwlT05c_2z0/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 232)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 232)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 232)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/128bEGudctcpMPxTwm_cJCfL1Zkf3W3af/view?usp=sharing" class="pastedDriveLink-0">232.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=232.png;FMTTYPE=image/png:https://drive.google.com/file/d/128bEGudctcpMPxTwm_cJCfL1Zkf3W3af/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 233)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 233)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 233)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/18BEf8vMzZ16W22xBzUEmXLdck6q51-gE/view?usp=sharing" class="pastedDriveLink-0">233.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=233.png;FMTTYPE=image/png:https://drive.google.com/file/d/18BEf8vMzZ16W22xBzUEmXLdck6q51-gE/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 234)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 234)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 234)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1yU2-pLp4jqImR7QswRWw11851GBX6Fvi/view?usp=sharing" class="pastedDriveLink-0">234.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=234.png;FMTTYPE=image/png:https://drive.google.com/file/d/1yU2-pLp4jqImR7QswRWw11851GBX6Fvi/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 235)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 235)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 235)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1h1iZr7eXzKN-dF_8ugFnW2BHzMOEYZxf/view?usp=sharing" class="pastedDriveLink-0">235.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=235.png;FMTTYPE=image/png:https://drive.google.com/file/d/1h1iZr7eXzKN-dF_8ugFnW2BHzMOEYZxf/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 236)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 236)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 236)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/18f-qEe5V_8SI_L76EY-DA-iCIaXfNixH/view?usp=sharing" class="pastedDriveLink-0">236.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=236.png;FMTTYPE=image/png:https://drive.google.com/file/d/18f-qEe5V_8SI_L76EY-DA-iCIaXfNixH/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 237)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 237)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 237)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1NxJT9Lkqxi9NbFIrhxm8p3Jyx3PKIcEZ/view?usp=sharing" class="pastedDriveLink-0">237.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=237.png;FMTTYPE=image/png:https://drive.google.com/file/d/1NxJT9Lkqxi9NbFIrhxm8p3Jyx3PKIcEZ/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 238)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 238)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 238)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/18KaobpzPWAwNdmdUnt9AkvlAEzVXd8um/view?usp=sharing" class="pastedDriveLink-0">238.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=238.png;FMTTYPE=image/png:https://drive.google.com/file/d/18KaobpzPWAwNdmdUnt9AkvlAEzVXd8um/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 239)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 239)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 239)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1SQFL87XBGD9H3mOYBaMOgXqao-b_34Yd/view?usp=sharing" class="pastedDriveLink-0">239.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=239.png;FMTTYPE=image/png:https://drive.google.com/file/d/1SQFL87XBGD9H3mOYBaMOgXqao-b_34Yd/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 240)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 240)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 240)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1gh5JYGNrqyiw76OnzQxJ06LZMrTrQ_8h/view?usp=sharing" class="pastedDriveLink-0">240.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=240.png;FMTTYPE=image/png:https://drive.google.com/file/d/1gh5JYGNrqyiw76OnzQxJ06LZMrTrQ_8h/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 241)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 241)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 241)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1qb3D5uwJORAiTDpLQKvEXNrM1oxExrgu/view?usp=sharing" class="pastedDriveLink-0">241.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=241.png;FMTTYPE=image/png:https://drive.google.com/file/d/1qb3D5uwJORAiTDpLQKvEXNrM1oxExrgu/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 242)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 242)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 242)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1q39bbd33B_bhTYbXj7zHlcyWfZRlyONS/view?usp=sharing" class="pastedDriveLink-0">242.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=242.png;FMTTYPE=image/png:https://drive.google.com/file/d/1q39bbd33B_bhTYbXj7zHlcyWfZRlyONS/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 243)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 243)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 243)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1fXAARf1DFw-Jt08G_7I_xk5K33PBL-Q5/view?usp=sharing" class="pastedDriveLink-0">243.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=243.png;FMTTYPE=image/png:https://drive.google.com/file/d/1fXAARf1DFw-Jt08G_7I_xk5K33PBL-Q5/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 244)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 244)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 244)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1paIn6NNjBLy7DrLCkfA3bTIVFuI8OLAo/view?usp=sharing" class="pastedDriveLink-0">244.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=244.png;FMTTYPE=image/png:https://drive.google.com/file/d/1paIn6NNjBLy7DrLCkfA3bTIVFuI8OLAo/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 245)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 245)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 245)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1QrNEy84rLImvKixvnccdFB5X4n6ZdtQ4/view?usp=sharing" class="pastedDriveLink-0">245.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=245.png;FMTTYPE=image/png:https://drive.google.com/file/d/1QrNEy84rLImvKixvnccdFB5X4n6ZdtQ4/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 246)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 246)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 246)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1U-5UAS9aQxs5GwX_S5qcMnbAqFaYfhY6/view?usp=sharing" class="pastedDriveLink-0">246.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=246.png;FMTTYPE=image/png:https://drive.google.com/file/d/1U-5UAS9aQxs5GwX_S5qcMnbAqFaYfhY6/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 247)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 247)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 247)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1KNDiHmm4GRHDd2Bu99BagS2qVcCrxr_W/view?usp=sharing" class="pastedDriveLink-0">247.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=247.png;FMTTYPE=image/png:https://drive.google.com/file/d/1KNDiHmm4GRHDd2Bu99BagS2qVcCrxr_W/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 248)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 248)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 248)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1DwcGl_FpXgESjBa41gM0WuivimGekdBm/view?usp=sharing" class="pastedDriveLink-0">248.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=248.png;FMTTYPE=image/png:https://drive.google.com/file/d/1DwcGl_FpXgESjBa41gM0WuivimGekdBm/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 249)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 249)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 249)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1uGPK_DlhuAQmYK1h3fgFfeHWdDC45K7w/view?usp=sharing" class="pastedDriveLink-0">249.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=249.png;FMTTYPE=image/png:https://drive.google.com/file/d/1uGPK_DlhuAQmYK1h3fgFfeHWdDC45K7w/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 250)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 250)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 250)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1wzzpdBC7TNoq3DJ4_O1U3cIApZkgaHyn/view?usp=sharing" class="pastedDriveLink-0">250.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=250.png;FMTTYPE=image/png:https://drive.google.com/file/d/1wzzpdBC7TNoq3DJ4_O1U3cIApZkgaHyn/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 251)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 251)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 251)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1kWpuh6r78VZONHm5BPiUT-Y5nCaUt68s/view?usp=sharing" class="pastedDriveLink-0">251.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=251.png;FMTTYPE=image/png:https://drive.google.com/file/d/1kWpuh6r78VZONHm5BPiUT-Y5nCaUt68s/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 252)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 252)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 252)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1cdxVuWkl4j4dedychNcGz8uhVmkxwue1/view?usp=sharing" class="pastedDriveLink-0">252.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=252.png;FMTTYPE=image/png:https://drive.google.com/file/d/1cdxVuWkl4j4dedychNcGz8uhVmkxwue1/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 253)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 253)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 253)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1jCZjyWDo7aQHt4SezCCWj3YSbhB0Rl1k/view?usp=sharing" class="pastedDriveLink-0">253.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=253.png;FMTTYPE=image/png:https://drive.google.com/file/d/1jCZjyWDo7aQHt4SezCCWj3YSbhB0Rl1k/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 254)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 254)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 254)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1HqHINEgO6uc8rPTbCN5FhM7jx3Q6j3Ot/view?usp=sharing" class="pastedDriveLink-0">254.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=254.png;FMTTYPE=image/png:https://drive.google.com/file/d/1HqHINEgO6uc8rPTbCN5FhM7jx3Q6j3Ot/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 255)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 255)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 255)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/18jF9BpGMHLXmRX0zuex0pabMraDWKJUf/view?usp=sharing" class="pastedDriveLink-0">255.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=255.png;FMTTYPE=image/png:https://drive.google.com/file/d/18jF9BpGMHLXmRX0zuex0pabMraDWKJUf/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 256)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 256)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 256)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/15G0Tj1hJii2Y46Og6_c95mnJdnPdFn-P/view?usp=sharing" class="pastedDriveLink-0">256.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=256.png;FMTTYPE=image/png:https://drive.google.com/file/d/15G0Tj1hJii2Y46Og6_c95mnJdnPdFn-P/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 257)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 257)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 257)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1KlOoaohEVd7mvBkf7X7kScRsfrTM--kV/view?usp=sharing" class="pastedDriveLink-0">257.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=257.png;FMTTYPE=image/png:https://drive.google.com/file/d/1KlOoaohEVd7mvBkf7X7kScRsfrTM--kV/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 258)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 258)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 258)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1PfHV5MWSd_BiyXvpnJJzK_x5AkcNrw35/view?usp=sharing" class="pastedDriveLink-0">258.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=258.png;FMTTYPE=image/png:https://drive.google.com/file/d/1PfHV5MWSd_BiyXvpnJJzK_x5AkcNrw35/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 259)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 259)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 259)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Vq6HFiwl1VsNTLHCV30irdPI7HRJ7siM/view?usp=sharing" class="pastedDriveLink-0">259.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=259.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Vq6HFiwl1VsNTLHCV30irdPI7HRJ7siM/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 260)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 260)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 260)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1QVHKLwemsBbf9oi0bFbqOsMmk02nC_FT/view?usp=sharing" class="pastedDriveLink-0">260.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=260.png;FMTTYPE=image/png:https://drive.google.com/file/d/1QVHKLwemsBbf9oi0bFbqOsMmk02nC_FT/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 261)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 261)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 261)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1c4DTlKLqrJIU-oJE9LKmM7GMCnzJjUZ_/view?usp=sharing" class="pastedDriveLink-0">261.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=261.png;FMTTYPE=image/png:https://drive.google.com/file/d/1c4DTlKLqrJIU-oJE9LKmM7GMCnzJjUZ_/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 262)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 262)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 262)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1gwgEG5Dmzpq6sB9i9-n68miHGaBZD3CP/view?usp=sharing" class="pastedDriveLink-0">262.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=262.png;FMTTYPE=image/png:https://drive.google.com/file/d/1gwgEG5Dmzpq6sB9i9-n68miHGaBZD3CP/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 263)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 263)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 263)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1KEfgHd2maumzZ1Q_Kadrdw0LjzR4HzuI/view?usp=sharing" class="pastedDriveLink-0">263.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=263.png;FMTTYPE=image/png:https://drive.google.com/file/d/1KEfgHd2maumzZ1Q_Kadrdw0LjzR4HzuI/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 264)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 264)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 264)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1SR7ddsQNUbRy6nLw-DMc0L_Xfb1hpFbH/view?usp=sharing" class="pastedDriveLink-0">264.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=264.png;FMTTYPE=image/png:https://drive.google.com/file/d/1SR7ddsQNUbRy6nLw-DMc0L_Xfb1hpFbH/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 265)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 265)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 265)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1TkBvlYXtwdr564klMMjapSrDb8-_fqGi/view?usp=sharing" class="pastedDriveLink-0">265.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=265.png;FMTTYPE=image/png:https://drive.google.com/file/d/1TkBvlYXtwdr564klMMjapSrDb8-_fqGi/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 266)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 266)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 266)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1rF8t9catP_sS7u8Y8wZntBhENTd56UsP/view?usp=sharing" class="pastedDriveLink-0">266.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=266.png;FMTTYPE=image/png:https://drive.google.com/file/d/1rF8t9catP_sS7u8Y8wZntBhENTd56UsP/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 267)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 267)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 267)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1OnjSWamA05yQf_Kh_WjJx4kOg8OGe8bj/view?usp=sharing" class="pastedDriveLink-0">267.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=267.png;FMTTYPE=image/png:https://drive.google.com/file/d/1OnjSWamA05yQf_Kh_WjJx4kOg8OGe8bj/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 268)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 268)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 268)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/16Jc8PeQnpTRUEeS6_6jGJtiWktXcih3Y/view?usp=sharing" class="pastedDriveLink-0">268.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=268.png;FMTTYPE=image/png:https://drive.google.com/file/d/16Jc8PeQnpTRUEeS6_6jGJtiWktXcih3Y/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 269)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 269)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 269)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1U7J3ZMSu8QQsOzCZaX_G4-U1sG7eIudD/view?usp=sharing" class="pastedDriveLink-0">269.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=269.png;FMTTYPE=image/png:https://drive.google.com/file/d/1U7J3ZMSu8QQsOzCZaX_G4-U1sG7eIudD/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 270)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 270)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 270)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1TYzdxC6fHSItmYIje6b13uoqAsruqbNS/view?usp=sharing" class="pastedDriveLink-0">270.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=270.png;FMTTYPE=image/png:https://drive.google.com/file/d/1TYzdxC6fHSItmYIje6b13uoqAsruqbNS/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 271)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 271)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 271)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1_lhvOg4gOf_TjDiA4UOKAIf_XnAcVvHP/view?usp=sharing" class="pastedDriveLink-0">271.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=271.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_lhvOg4gOf_TjDiA4UOKAIf_XnAcVvHP/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 272)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 272)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 272)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1_lhvOg4gOf_TjDiA4UOKAIf_XnAcVvHP/view?usp=sharing" class="pastedDriveLink-0">272.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=272.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_lhvOg4gOf_TjDiA4UOKAIf_XnAcVvHP/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 273)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 273)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 273)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1_lhvOg4gOf_TjDiA4UOKAIf_XnAcVvHP/view?usp=sharing" class="pastedDriveLink-0">273.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=273.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_lhvOg4gOf_TjDiA4UOKAIf_XnAcVvHP/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 274)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 274)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 274)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1TXZ2EIz6C_m2WXbrPM5t9fiAMZ5OZE_i/view?usp=sharing" class="pastedDriveLink-0">274.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=274.png;FMTTYPE=image/png:https://drive.google.com/file/d/1TXZ2EIz6C_m2WXbrPM5t9fiAMZ5OZE_i/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 275)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 275)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 275)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/19ipEjgJS5X0acAzhD8kGewtmyonxfpqd/view?usp=sharing" class="pastedDriveLink-0">275.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=275.png;FMTTYPE=image/png:https://drive.google.com/file/d/19ipEjgJS5X0acAzhD8kGewtmyonxfpqd/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 276)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 276)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 276)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/118H0OmT5aOeospfD3V-J4ey1grzKdNss/view?usp=sharing" class="pastedDriveLink-0">276.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=276.png;FMTTYPE=image/png:https://drive.google.com/file/d/118H0OmT5aOeospfD3V-J4ey1grzKdNss/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 277)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 277)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 277)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Km5kLUuoBQYbXWzraorkGmQHKkrizl5k/view?usp=sharing" class="pastedDriveLink-0">277.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=277.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Km5kLUuoBQYbXWzraorkGmQHKkrizl5k/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 278)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 278)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 278)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/10ePbMlQomgITnnjJASK8ShNQBwc-LKof/view?usp=sharing" class="pastedDriveLink-0">278.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=278.png;FMTTYPE=image/png:https://drive.google.com/file/d/10ePbMlQomgITnnjJASK8ShNQBwc-LKof/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 279)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 279)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 279)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1hSZ4LCIY5B7RZeLM4b5XN8u38s17FvqF/view?usp=sharing" class="pastedDriveLink-0">279.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=279.png;FMTTYPE=image/png:https://drive.google.com/file/d/1hSZ4LCIY5B7RZeLM4b5XN8u38s17FvqF/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 280)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 280)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 280)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1MZZnikWXK2enZdtnZtPAIZ3o1Y04q_Gp/view?usp=sharing" class="pastedDriveLink-0">280.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=280.png;FMTTYPE=image/png:https://drive.google.com/file/d/1MZZnikWXK2enZdtnZtPAIZ3o1Y04q_Gp/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 281)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 281)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 281)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1UjOF1SP78lk_gXFt3e59alCJrBTssuEz/view?usp=sharing" class="pastedDriveLink-0">281.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=281.png;FMTTYPE=image/png:https://drive.google.com/file/d/1UjOF1SP78lk_gXFt3e59alCJrBTssuEz/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 282)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 282)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 282)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1r7e5a8wxs7UxD9bKa4xU9vnCnrlI7Y5I/view?usp=sharing" class="pastedDriveLink-0">282.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=282.png;FMTTYPE=image/png:https://drive.google.com/file/d/1r7e5a8wxs7UxD9bKa4xU9vnCnrlI7Y5I/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 283)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 283)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 283)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/15YmQxxaVt5sEMw3pOzFBvOpGyzj_TVsC/view?usp=sharing" class="pastedDriveLink-0">283.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=283.png;FMTTYPE=image/png:https://drive.google.com/file/d/15YmQxxaVt5sEMw3pOzFBvOpGyzj_TVsC/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 284)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 284)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 284)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1JpbyJ-l8UpzgTuX0ajgAAM2cFjFsJOPs/view?usp=sharing" class="pastedDriveLink-0">284.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=284.png;FMTTYPE=image/png:https://drive.google.com/file/d/1JpbyJ-l8UpzgTuX0ajgAAM2cFjFsJOPs/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 285)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 285)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 285)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1L3A56zJ4vHHS50n_WW_Loyx5d2NOyuVi/view?usp=sharing" class="pastedDriveLink-0">285.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=285.png;FMTTYPE=image/png:https://drive.google.com/file/d/1L3A56zJ4vHHS50n_WW_Loyx5d2NOyuVi/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 286)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 286)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 286)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1C8d_vhrttvWcURffRj0B7Duz0a_GV6uP/view?usp=sharing" class="pastedDriveLink-0">286.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=286.png;FMTTYPE=image/png:https://drive.google.com/file/d/1C8d_vhrttvWcURffRj0B7Duz0a_GV6uP/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 287)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 287)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 287)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1SB9e6ceWIuOYdoGPniHB3E5qZnVEmLib/view?usp=sharing" class="pastedDriveLink-0">287.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=287.png;FMTTYPE=image/png:https://drive.google.com/file/d/1SB9e6ceWIuOYdoGPniHB3E5qZnVEmLib/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 288)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 288)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 288)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1h_sZ5t0_hD5AjHxpfA-zjqlBegIScVmW/view?usp=sharing" class="pastedDriveLink-0">288.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=288.png;FMTTYPE=image/png:https://drive.google.com/file/d/1h_sZ5t0_hD5AjHxpfA-zjqlBegIScVmW/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 289)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 289)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 289)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1_K1P7K-TNC4YJURYm1xN3222e9fGetN7/view?usp=sharing" class="pastedDriveLink-0">289.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=289.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_K1P7K-TNC4YJURYm1xN3222e9fGetN7/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 290)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 290)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 290)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1u-YPnN7F3ZiqV76kjuv2vlMM2mT5ABg5/view?usp=sharing" class="pastedDriveLink-0">290.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=290.png;FMTTYPE=image/png:https://drive.google.com/file/d/1u-YPnN7F3ZiqV76kjuv2vlMM2mT5ABg5/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 291)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 291)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 291)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1dpwzF3j5M3FRrTunb-zmjJZpoFvm2kAZ/view?usp=sharing" class="pastedDriveLink-0">291.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=291.png;FMTTYPE=image/png:https://drive.google.com/file/d/1dpwzF3j5M3FRrTunb-zmjJZpoFvm2kAZ/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 292)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 292)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 292)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1bh-vcuJhKLyVo6jKno26aXKVPX5bFImv/view?usp=sharing" class="pastedDriveLink-0">292.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=292.png;FMTTYPE=image/png:https://drive.google.com/file/d/1bh-vcuJhKLyVo6jKno26aXKVPX5bFImv/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 293)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 293)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 293)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1hgixJ_F8JfbeTmsIfzp3Va-3XLXgwQOD/view?usp=sharing" class="pastedDriveLink-0">293.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=293.png;FMTTYPE=image/png:https://drive.google.com/file/d/1hgixJ_F8JfbeTmsIfzp3Va-3XLXgwQOD/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 294)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 294)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 294)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1lf96y-LojJJ5ZeQwDBg6ANFgb8LrwrmB/view?usp=sharing" class="pastedDriveLink-0">294.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=294.png;FMTTYPE=image/png:https://drive.google.com/file/d/1lf96y-LojJJ5ZeQwDBg6ANFgb8LrwrmB/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 295)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 295)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 295)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1EvMrNx68GHqUetDtrLZMX7pCFGizGrLf/view?usp=sharing" class="pastedDriveLink-0">295.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=295.png;FMTTYPE=image/png:https://drive.google.com/file/d/1EvMrNx68GHqUetDtrLZMX7pCFGizGrLf/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 296)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 296)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 296)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1gWOMwem5HAxwAMEiQ7I6aC3Fej65m9BF/view?usp=sharing" class="pastedDriveLink-0">296.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=296.png;FMTTYPE=image/png:https://drive.google.com/file/d/1gWOMwem5HAxwAMEiQ7I6aC3Fej65m9BF/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 297)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 297)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 297)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1zNKPenS7TaeAW4sszdvLegV3lfEB0DEP/view?usp=sharing" class="pastedDriveLink-0">297.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=297.png;FMTTYPE=image/png:https://drive.google.com/file/d/1zNKPenS7TaeAW4sszdvLegV3lfEB0DEP/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 298)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 298)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 298)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Fpf7LI4phmtXTAzmHTkDBYjQq0ilmJbk/view?usp=sharing" class="pastedDriveLink-0">298.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=298.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Fpf7LI4phmtXTAzmHTkDBYjQq0ilmJbk/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 299)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 299)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 299)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1QoM1-OFB8MX925t00nEYnv5naVjFKWqX/view?usp=sharing" class="pastedDriveLink-0">299.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=299.png;FMTTYPE=image/png:https://drive.google.com/file/d/1QoM1-OFB8MX925t00nEYnv5naVjFKWqX/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 300)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 300)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 300)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1QNdgDZFvGLHThl6ugnlO1hLl0hDC5arv/view?usp=sharing" class="pastedDriveLink-0">300.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=300.png;FMTTYPE=image/png:https://drive.google.com/file/d/1QNdgDZFvGLHThl6ugnlO1hLl0hDC5arv/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 301)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 301)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 301)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ZTCjWPrfMzCCsk7UvplJ7B-Be0nX_dt9/view?usp=sharing" class="pastedDriveLink-0">301.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=301.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ZTCjWPrfMzCCsk7UvplJ7B-Be0nX_dt9/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 302)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 302)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 302)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1-BavHlbm3EDu5tHkXXK1RaBV0JckjXU0/view?usp=sharing" class="pastedDriveLink-0">302.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=302.png;FMTTYPE=image/png:https://drive.google.com/file/d/1-BavHlbm3EDu5tHkXXK1RaBV0JckjXU0/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 303)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 303)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 303)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Fog17z4R42n58RAZ_cAbr8s4bDtXCfCb/view?usp=sharing" class="pastedDriveLink-0">303.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=303.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Fog17z4R42n58RAZ_cAbr8s4bDtXCfCb/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 304)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 304)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 304)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1GhlSMgY3w6riTUTrA9I09FUpRFKet1Tn/view?usp=sharing" class="pastedDriveLink-0">304.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=304.png;FMTTYPE=image/png:https://drive.google.com/file/d/1GhlSMgY3w6riTUTrA9I09FUpRFKet1Tn/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 305)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 305)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 305)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1r3lTUiBnzlDyTHOQqdENwaNbcstFOIld/view?usp=sharing" class="pastedDriveLink-0">305.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=305.png;FMTTYPE=image/png:https://drive.google.com/file/d/1r3lTUiBnzlDyTHOQqdENwaNbcstFOIld/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 306)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 306)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 306)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1mF0Mz2LxYPhvAT0h-kTKTprMwK0HWa8i/view?usp=sharing" class="pastedDriveLink-0">306.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=306.png;FMTTYPE=image/png:https://drive.google.com/file/d/1mF0Mz2LxYPhvAT0h-kTKTprMwK0HWa8i/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 307)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 307)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 307)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1CKxjE4O36ixNwEjFda2e89bSCjOgbUJ7/view?usp=sharing" class="pastedDriveLink-0">307.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=307.png;FMTTYPE=image/png:https://drive.google.com/file/d/1CKxjE4O36ixNwEjFda2e89bSCjOgbUJ7/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 308)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 308)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 308)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1QMw1y5aoJmBXY-uQvHZ06FOihbOaUOpQ/view?usp=sharing" class="pastedDriveLink-0">308.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=308.png;FMTTYPE=image/png:https://drive.google.com/file/d/1QMw1y5aoJmBXY-uQvHZ06FOihbOaUOpQ/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 309)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 309)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 309)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1OoJwJhHkmuhhUvsWJ4eTXDX7M6rvYVjK/view?usp=sharing" class="pastedDriveLink-0">309.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=309.png;FMTTYPE=image/png:https://drive.google.com/file/d/1OoJwJhHkmuhhUvsWJ4eTXDX7M6rvYVjK/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 310)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 310)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 310)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1RLfylSwCQd0H2baWjAc2sg8ZM3wKzjBR/view?usp=sharing" class="pastedDriveLink-0">310.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=310.png;FMTTYPE=image/png:https://drive.google.com/file/d/1RLfylSwCQd0H2baWjAc2sg8ZM3wKzjBR/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 311)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 311)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 311)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1JWF6TAhyeMI0HPel9slHk7H1C03sv9_C/view?usp=sharing" class="pastedDriveLink-0">311.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=311.png;FMTTYPE=image/png:https://drive.google.com/file/d/1JWF6TAhyeMI0HPel9slHk7H1C03sv9_C/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 312)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 312)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 312)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1UuOb8HG2NvAIxuRMClbZ_J8HToLKlWBj/view?usp=sharing" class="pastedDriveLink-0">312.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=312.png;FMTTYPE=image/png:https://drive.google.com/file/d/1UuOb8HG2NvAIxuRMClbZ_J8HToLKlWBj/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 313)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 313)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 313)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1-utH-cyp47JR4gBxLeQdc7hTuvJFg3Ty/view?usp=sharing" class="pastedDriveLink-0">313.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=313.png;FMTTYPE=image/png:https://drive.google.com/file/d/1-utH-cyp47JR4gBxLeQdc7hTuvJFg3Ty/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 314)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 314)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 314)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1NaX2KBd-Nm889MapW27Ca-ZthTyUg6k6/view?usp=sharing" class="pastedDriveLink-0">314.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=314.png;FMTTYPE=image/png:https://drive.google.com/file/d/1NaX2KBd-Nm889MapW27Ca-ZthTyUg6k6/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 315)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 315)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 315)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1WlfJP6W1W7_SYPcEA0SwmpExb71bBfiC/view?usp=sharing" class="pastedDriveLink-0">315.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=315.png;FMTTYPE=image/png:https://drive.google.com/file/d/1WlfJP6W1W7_SYPcEA0SwmpExb71bBfiC/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 316)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 316)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 316)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/133PwRWzmw0WKHnCxc-w5iQcgNR9Ux0o4/view?usp=sharing" class="pastedDriveLink-0">316.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=316.png;FMTTYPE=image/png:https://drive.google.com/file/d/133PwRWzmw0WKHnCxc-w5iQcgNR9Ux0o4/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 317)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 317)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 317)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/13rj7_N27c3YzD9ull5rTI-S5Kb5dNSvq/view?usp=sharing" class="pastedDriveLink-0">317.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=317.png;FMTTYPE=image/png:https://drive.google.com/file/d/13rj7_N27c3YzD9ull5rTI-S5Kb5dNSvq/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 318)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 318)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 318)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Xq0CvhdLJ7guzEqHQuskqYSLL2Kka4QX/view?usp=sharing" class="pastedDriveLink-0">318.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=318.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Xq0CvhdLJ7guzEqHQuskqYSLL2Kka4QX/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 319)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 319)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 319)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1nUTAmPS3eE0E5xHE8pOK-Ptga4_8xOQu/view?usp=sharing" class="pastedDriveLink-0">319.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=319.png;FMTTYPE=image/png:https://drive.google.com/file/d/1nUTAmPS3eE0E5xHE8pOK-Ptga4_8xOQu/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 320)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 320)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 320)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Ur1i6I9MTNew-DCB5kyAVcFiZkUxDPbX/view?usp=sharing" class="pastedDriveLink-0">320.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=320.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Ur1i6I9MTNew-DCB5kyAVcFiZkUxDPbX/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 321)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 321)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 321)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1vCjVnF_IbUOBcLWoGKv-Ec8mowElcikt/view?usp=sharing" class="pastedDriveLink-0">321.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=321.png;FMTTYPE=image/png:https://drive.google.com/file/d/1vCjVnF_IbUOBcLWoGKv-Ec8mowElcikt/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 322)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 322)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 322)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1TkZo9yAvJj-jqTlGbMTizpbVUccQxI9S/view?usp=sharing" class="pastedDriveLink-0">322.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=322.png;FMTTYPE=image/png:https://drive.google.com/file/d/1TkZo9yAvJj-jqTlGbMTizpbVUccQxI9S/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 323)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 323)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 323)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1tkYFaDkOI2Xy6EqMet9kQOAtjVBV8D7m/view?usp=sharing" class="pastedDriveLink-0">323.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=323.png;FMTTYPE=image/png:https://drive.google.com/file/d/1tkYFaDkOI2Xy6EqMet9kQOAtjVBV8D7m/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 324)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 324)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 324)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1e1VyTgH4bmYvqure23eayXtQbkwI8MDt/view?usp=sharing" class="pastedDriveLink-0">324.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=324.png;FMTTYPE=image/png:https://drive.google.com/file/d/1e1VyTgH4bmYvqure23eayXtQbkwI8MDt/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 325)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 325)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 325)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/11a5P2knvc4WuzrcHUVNFwHFHJqpPJFGX/view?usp=sharing" class="pastedDriveLink-0">325.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=325.png;FMTTYPE=image/png:https://drive.google.com/file/d/11a5P2knvc4WuzrcHUVNFwHFHJqpPJFGX/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 326)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 326)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 326)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1xKJikLOUli1tE-RWZszQduiLn39t4mIv/view?usp=sharing" class="pastedDriveLink-0">326.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=326.png;FMTTYPE=image/png:https://drive.google.com/file/d/1xKJikLOUli1tE-RWZszQduiLn39t4mIv/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 327)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 327)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 327)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1DoO_lJdRBl7MWvDzowYN7Kt3b_mPoKOZ/view?usp=sharing" class="pastedDriveLink-0">327.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=327.png;FMTTYPE=image/png:https://drive.google.com/file/d/1DoO_lJdRBl7MWvDzowYN7Kt3b_mPoKOZ/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 328)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 328)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 328)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/14pqph6HsnNcakTkV1jak5-4zCTYNXdCN/view?usp=sharing" class="pastedDriveLink-0">328.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=328.png;FMTTYPE=image/png:https://drive.google.com/file/d/14pqph6HsnNcakTkV1jak5-4zCTYNXdCN/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 329)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 329)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 329)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/12woMqqZ3Ge38FuVlBK3GcTkdqr6LFOFO/view?usp=sharing" class="pastedDriveLink-0">329.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=329.png;FMTTYPE=image/png:https://drive.google.com/file/d/12woMqqZ3Ge38FuVlBK3GcTkdqr6LFOFO/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 330)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 330)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 330)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1SQWicfvgQW8bUi9653xdEAGlIPUPJrTl/view?usp=sharing" class="pastedDriveLink-0">330.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=330.png;FMTTYPE=image/png:https://drive.google.com/file/d/1SQWicfvgQW8bUi9653xdEAGlIPUPJrTl/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 331)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 331)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 331)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1_hjnDmY6Q57Edt1dmSCocVFuwcq9KXhY/view?usp=sharing" class="pastedDriveLink-0">331.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=331.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_hjnDmY6Q57Edt1dmSCocVFuwcq9KXhY/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 332)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 332)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 332)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ciuNRZ-vu7yvqVp9QUKDZVy-h8wwzyJa/view?usp=sharing" class="pastedDriveLink-0">332.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=332.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ciuNRZ-vu7yvqVp9QUKDZVy-h8wwzyJa/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 333)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 333)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 333)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1lU96kmfu2mKUOfacSZMGNwZaH__Lquue/view?usp=sharing" class="pastedDriveLink-0">333.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=333.png;FMTTYPE=image/png:https://drive.google.com/file/d/1lU96kmfu2mKUOfacSZMGNwZaH__Lquue/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 334)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 334)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 334)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1dhrS24Sy_5e8GF8-iVPVEFj98-L-abqV/view?usp=sharing" class="pastedDriveLink-0">334.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=334.png;FMTTYPE=image/png:https://drive.google.com/file/d/1dhrS24Sy_5e8GF8-iVPVEFj98-L-abqV/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 335)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 335)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 335)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1cnB0XoP4Gwqw7Zeni-_W2uUwmzo7YzTj/view?usp=sharing" class="pastedDriveLink-0">335.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=335.png;FMTTYPE=image/png:https://drive.google.com/file/d/1cnB0XoP4Gwqw7Zeni-_W2uUwmzo7YzTj/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 336)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 336)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 336)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1vz06H31jLM9KKi4ZtUA7Qkff2U22cyD1/view?usp=sharing" class="pastedDriveLink-0">336.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=336.png;FMTTYPE=image/png:https://drive.google.com/file/d/1vz06H31jLM9KKi4ZtUA7Qkff2U22cyD1/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 337)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 337)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 337)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1dcGmb3bx_HPIBVec62g5VlrjlZ57C41Z/view?usp=sharing" class="pastedDriveLink-0">337.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=337.png;FMTTYPE=image/png:https://drive.google.com/file/d/1dcGmb3bx_HPIBVec62g5VlrjlZ57C41Z/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 338)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 338)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 338)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1_O7mcQuAbTj3RciQrEhArvC5cZBNKueh/view?usp=sharing" class="pastedDriveLink-0">338.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=338.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_O7mcQuAbTj3RciQrEhArvC5cZBNKueh/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 339)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 339)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 339)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1rJBojUSSIPq07TaDAnFXkX_3SfqCiTCD/view?usp=sharing" class="pastedDriveLink-0">339.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=339.png;FMTTYPE=image/png:https://drive.google.com/file/d/1rJBojUSSIPq07TaDAnFXkX_3SfqCiTCD/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 340)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 340)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 340)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1YQJPz0HBwNVzjd2MITEv4bU3p3gjPqoM/view?usp=sharing" class="pastedDriveLink-0">340.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=340.png;FMTTYPE=image/png:https://drive.google.com/file/d/1YQJPz0HBwNVzjd2MITEv4bU3p3gjPqoM/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 341)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 341)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 341)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1F9jtRcVwpZ4o6J6nQxsw4QEypZ6OBdhV/view?usp=sharing" class="pastedDriveLink-0">341.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=341.png;FMTTYPE=image/png:https://drive.google.com/file/d/1F9jtRcVwpZ4o6J6nQxsw4QEypZ6OBdhV/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 342)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 342)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 342)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1XJVrihHuh8mLOQddcuttlz80sgIhhHRv/view?usp=sharing" class="pastedDriveLink-0">342.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=342.png;FMTTYPE=image/png:https://drive.google.com/file/d/1XJVrihHuh8mLOQddcuttlz80sgIhhHRv/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 343)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 343)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 343)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1kMC---vYfQyFzVuaNXNtztFh0Q0TBPwA/view?usp=sharing" class="pastedDriveLink-0">343.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=343.png;FMTTYPE=image/png:https://drive.google.com/file/d/1kMC---vYfQyFzVuaNXNtztFh0Q0TBPwA/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 344)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 344)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 344)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1-oVTChFssdfTOEDoy0nxldBw1FApe2x1/view?usp=sharing" class="pastedDriveLink-0">344.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=344.png;FMTTYPE=image/png:https://drive.google.com/file/d/1-oVTChFssdfTOEDoy0nxldBw1FApe2x1/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 345)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 345)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 345)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1A5yMjJ-8jIv1KLFklIF9APm2goHVQkZ0/view?usp=sharing" class="pastedDriveLink-0">345.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=345.png;FMTTYPE=image/png:https://drive.google.com/file/d/1A5yMjJ-8jIv1KLFklIF9APm2goHVQkZ0/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 346)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 346)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 346)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1lovvyxl9p70kjnOrAf7o3QWgNe4twsIz/view?usp=sharing" class="pastedDriveLink-0">346.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=346.png;FMTTYPE=image/png:https://drive.google.com/file/d/1lovvyxl9p70kjnOrAf7o3QWgNe4twsIz/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 347)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 347)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 347)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1edefwWWTRODg8RJDLm5ig_arVZPmhQ90/view?usp=sharing" class="pastedDriveLink-0">347.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=347.png;FMTTYPE=image/png:https://drive.google.com/file/d/1edefwWWTRODg8RJDLm5ig_arVZPmhQ90/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 348)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 348)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 348)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1iqWVI67hx8u5iw-I_Tr07RdZqhSJushB/view?usp=sharing" class="pastedDriveLink-0">348.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=348.png;FMTTYPE=image/png:https://drive.google.com/file/d/1iqWVI67hx8u5iw-I_Tr07RdZqhSJushB/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 349)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 349)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 349)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1FZT51ladMmWYNq3uy4YeX99Xejd2ZtDp/view?usp=sharing" class="pastedDriveLink-0">349.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=349.png;FMTTYPE=image/png:https://drive.google.com/file/d/1FZT51ladMmWYNq3uy4YeX99Xejd2ZtDp/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 350)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 350)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 350)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1kgiSiMga24817OVkpp4QqfcbdLAfmQb2/view?usp=sharing" class="pastedDriveLink-0">350.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=350.png;FMTTYPE=image/png:https://drive.google.com/file/d/1kgiSiMga24817OVkpp4QqfcbdLAfmQb2/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 351)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 351)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 351)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/18RClSs0E3D9HuQFK6BnCJWcPqRyMcso0/view?usp=sharing" class="pastedDriveLink-0">351.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=351.png;FMTTYPE=image/png:https://drive.google.com/file/d/18RClSs0E3D9HuQFK6BnCJWcPqRyMcso0/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 352)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 352)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 352)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1yLAbOHZMPVZeFwUyCzAptjHSJIhuOjds/view?usp=sharing" class="pastedDriveLink-0">352.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=352.png;FMTTYPE=image/png:https://drive.google.com/file/d/1yLAbOHZMPVZeFwUyCzAptjHSJIhuOjds/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 353)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 353)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 353)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Te_H3miHiaL82jHwmPokwqUxF-iwvA4p/view?usp=sharing" class="pastedDriveLink-0">353.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=353.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Te_H3miHiaL82jHwmPokwqUxF-iwvA4p/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 354)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 354)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 354)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Mepv4i1m7mK8UbutugeBkdouqQBrqT7o/view?usp=sharing" class="pastedDriveLink-0">354.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=354.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Mepv4i1m7mK8UbutugeBkdouqQBrqT7o/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 355)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 355)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 355)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1_pthWkHJ1uiPLy_ys8UeWGgTZTS28DKC/view?usp=sharing" class="pastedDriveLink-0">355.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=355.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_pthWkHJ1uiPLy_ys8UeWGgTZTS28DKC/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 356)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 356)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 356)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1mr5-EoItdRKfKH4v_pfYTuqTPUf4-372/view?usp=sharing" class="pastedDriveLink-0">356.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=356.png;FMTTYPE=image/png:https://drive.google.com/file/d/1mr5-EoItdRKfKH4v_pfYTuqTPUf4-372/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 357)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 357)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 357)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1w_hjixzKwx-i2sDQcaKrdPWeuz564yMR/view?usp=sharing" class="pastedDriveLink-0">357.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=357.png;FMTTYPE=image/png:https://drive.google.com/file/d/1w_hjixzKwx-i2sDQcaKrdPWeuz564yMR/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 358)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 358)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 358)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ZUwBKuP9eGnqNMRZhK_b6Z_QBjU7NZpi/view?usp=sharing" class="pastedDriveLink-0">358.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=358.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ZUwBKuP9eGnqNMRZhK_b6Z_QBjU7NZpi/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 359)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 359)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 359)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1R_NZes5xk8pK123Fdql6QVaZmJOd_3N9/view?usp=sharing" class="pastedDriveLink-0">359.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=359.png;FMTTYPE=image/png:https://drive.google.com/file/d/1R_NZes5xk8pK123Fdql6QVaZmJOd_3N9/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 360)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 360)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 360)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1dT_YmN7vjQvjo_VAOI9jHbHDctF4SExK/view?usp=sharing" class="pastedDriveLink-0">360.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=360.png;FMTTYPE=image/png:https://drive.google.com/file/d/1dT_YmN7vjQvjo_VAOI9jHbHDctF4SExK/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 361)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 361)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 361)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1xMwFxIHGFjZeQY5EEomk1GsfltJPoHu6/view?usp=sharing" class="pastedDriveLink-0">361.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=361.png;FMTTYPE=image/png:https://drive.google.com/file/d/1xMwFxIHGFjZeQY5EEomk1GsfltJPoHu6/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 362)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 362)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 362)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1NkgE-PbLtyoDQ7N7O3lm9yaWmDBEnMcB/view?usp=sharing" class="pastedDriveLink-0">362.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=362.png;FMTTYPE=image/png:https://drive.google.com/file/d/1NkgE-PbLtyoDQ7N7O3lm9yaWmDBEnMcB/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 363)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 363)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 363)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1IUlYjxvvVXC3lTy9SIqKvGFEpKb-va9X/view?usp=sharing" class="pastedDriveLink-0">363.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=363.png;FMTTYPE=image/png:https://drive.google.com/file/d/1IUlYjxvvVXC3lTy9SIqKvGFEpKb-va9X/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 364)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 364)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 364)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1llnsA1vrA1YjpB-BMn1ax8hBpwbvFgjq/view?usp=sharing" class="pastedDriveLink-0">364.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=364.png;FMTTYPE=image/png:https://drive.google.com/file/d/1llnsA1vrA1YjpB-BMn1ax8hBpwbvFgjq/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 365)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 365)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 365)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/11JN170D4Sq6k0uKxKvKWR0jz1Ba9iWzk/view?usp=sharing" class="pastedDriveLink-0">365.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=365.png;FMTTYPE=image/png:https://drive.google.com/file/d/11JN170D4Sq6k0uKxKvKWR0jz1Ba9iWzk/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 366)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 366)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 366)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Eg_CPWVo6RKpRKPrvjmLAzv-LDKXFSso/view?usp=sharing" class="pastedDriveLink-0">366.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=366.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Eg_CPWVo6RKpRKPrvjmLAzv-LDKXFSso/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 367)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 367)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 367)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1eBTsVBi3gsVMuZxwT0hY5B2G_rAOAdn-/view?usp=sharing" class="pastedDriveLink-0">367.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=367.png;FMTTYPE=image/png:https://drive.google.com/file/d/1eBTsVBi3gsVMuZxwT0hY5B2G_rAOAdn-/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 368)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 368)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 368)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1i4p_k4j3A1UTdz2PNrjDPRl0YV9N2FWs/view?usp=sharing" class="pastedDriveLink-0">368.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=368.png;FMTTYPE=image/png:https://drive.google.com/file/d/1i4p_k4j3A1UTdz2PNrjDPRl0YV9N2FWs/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 369)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 369)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 369)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1LbUyBzgMpz8ztBFEpDuJ5b1A28CbSLBc/view?usp=sharing" class="pastedDriveLink-0">369.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=369.png;FMTTYPE=image/png:https://drive.google.com/file/d/1LbUyBzgMpz8ztBFEpDuJ5b1A28CbSLBc/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 370)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 370)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 370)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1lJpd3TglxFNeSkNDjvA9B5QmSgXKW6XN/view?usp=sharing" class="pastedDriveLink-0">370.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=370.png;FMTTYPE=image/png:https://drive.google.com/file/d/1lJpd3TglxFNeSkNDjvA9B5QmSgXKW6XN/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 371)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 371)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 371)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1oZtfbKWGSj1YoBwkDC0cbLe0CORh7Kgp/view?usp=sharing" class="pastedDriveLink-0">371.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=371.png;FMTTYPE=image/png:https://drive.google.com/file/d/1oZtfbKWGSj1YoBwkDC0cbLe0CORh7Kgp/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 372)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 372)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 372)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/14LBePxkctnX5tQHRaB-AtJB2rUkA5L2R/view?usp=sharing" class="pastedDriveLink-0">372.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=372.png;FMTTYPE=image/png:https://drive.google.com/file/d/14LBePxkctnX5tQHRaB-AtJB2rUkA5L2R/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 373)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 373)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 373)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1UN3n04vUOY493hyZjVFJ09XEk0-jXfr5/view?usp=sharing" class="pastedDriveLink-0">373.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=373.png;FMTTYPE=image/png:https://drive.google.com/file/d/1UN3n04vUOY493hyZjVFJ09XEk0-jXfr5/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 374)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 374)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 374)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1-qYkAtcfl6nrECZ-41izEZIj_Oo4k0LR/view?usp=sharing" class="pastedDriveLink-0">374.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=374.png;FMTTYPE=image/png:https://drive.google.com/file/d/1-qYkAtcfl6nrECZ-41izEZIj_Oo4k0LR/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 375)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 375)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 375)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1PKtwALoaBoYHIHGgqePdqGmv85DLf3dG/view?usp=sharing" class="pastedDriveLink-0">375.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=375.png;FMTTYPE=image/png:https://drive.google.com/file/d/1PKtwALoaBoYHIHGgqePdqGmv85DLf3dG/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 376)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 376)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 376)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1gqXypSN1to1c28MRfhVeUYRI1VXlfgWh/view?usp=sharing" class="pastedDriveLink-0">376.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=376.png;FMTTYPE=image/png:https://drive.google.com/file/d/1gqXypSN1to1c28MRfhVeUYRI1VXlfgWh/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 377)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 377)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 377)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1LwnivX3_2i6-X7qcoQ_GMJShSg7Tnyjg/view?usp=sharing" class="pastedDriveLink-0">377.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=377.png;FMTTYPE=image/png:https://drive.google.com/file/d/1LwnivX3_2i6-X7qcoQ_GMJShSg7Tnyjg/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 378)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 378)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 378)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1dOYaQLNO5m3GonsbMBpGPxcbIgku9_-V/view?usp=sharing" class="pastedDriveLink-0">378.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=378.png;FMTTYPE=image/png:https://drive.google.com/file/d/1dOYaQLNO5m3GonsbMBpGPxcbIgku9_-V/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 379)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 379)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 379)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1nhYkBlYN8yqz5NWlcJiF4oJv3WpzrIsp/view?usp=sharing" class="pastedDriveLink-0">379.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=379.png;FMTTYPE=image/png:https://drive.google.com/file/d/1nhYkBlYN8yqz5NWlcJiF4oJv3WpzrIsp/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 380)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 380)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 380)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1yZqiLQsCN8GPQPFL39aAgRf2TdrfUNPw/view?usp=sharing" class="pastedDriveLink-0">380.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=380.png;FMTTYPE=image/png:https://drive.google.com/file/d/1yZqiLQsCN8GPQPFL39aAgRf2TdrfUNPw/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 381)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 381)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 381)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1krU_ZETMyJ2K6XRUElPJcJsS7kPQygLa/view?usp=sharing" class="pastedDriveLink-0">381.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=381.png;FMTTYPE=image/png:https://drive.google.com/file/d/1krU_ZETMyJ2K6XRUElPJcJsS7kPQygLa/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 382)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 382)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 382)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1f2S4lXrLCkIU9f2AZ_SoYcRdldsCvkqr/view?usp=sharing" class="pastedDriveLink-0">382.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=382.png;FMTTYPE=image/png:https://drive.google.com/file/d/1f2S4lXrLCkIU9f2AZ_SoYcRdldsCvkqr/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 383)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 383)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 383)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1gZ0ZVtMB9-WgM9LFrdrLN7FuzDcxtyka/view?usp=sharing" class="pastedDriveLink-0">383.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=383.png;FMTTYPE=image/png:https://drive.google.com/file/d/1gZ0ZVtMB9-WgM9LFrdrLN7FuzDcxtyka/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 384)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 384)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 384)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1SNIiKHEAuv29R79GakpwXnv83y9eSr1j/view?usp=sharing" class="pastedDriveLink-0">384.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=384.png;FMTTYPE=image/png:https://drive.google.com/file/d/1SNIiKHEAuv29R79GakpwXnv83y9eSr1j/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 385)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 385)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 385)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/11Mil7UyzDwU_eYH5N3-U28deNBVQoHSF/view?usp=sharing" class="pastedDriveLink-0">385.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=385.png;FMTTYPE=image/png:https://drive.google.com/file/d/11Mil7UyzDwU_eYH5N3-U28deNBVQoHSF/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 386)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 386)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 386)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/16qzOvHVebYUVu9OzMdfKrPQrUQMy5k9B/view?usp=sharing" class="pastedDriveLink-0">386.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=386.png;FMTTYPE=image/png:https://drive.google.com/file/d/16qzOvHVebYUVu9OzMdfKrPQrUQMy5k9B/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 387)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 387)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 387)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1IEgktaKbgUO0SCuqMkevizvQ28og-9as/view?usp=sharing" class="pastedDriveLink-0">387.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=387.png;FMTTYPE=image/png:https://drive.google.com/file/d/1IEgktaKbgUO0SCuqMkevizvQ28og-9as/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 388)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 388)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 388)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1tV52KwOJaL7YSRd0CwlRaPNGhprLdBNA/view?usp=sharing" class="pastedDriveLink-0">388.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=388.png;FMTTYPE=image/png:https://drive.google.com/file/d/1tV52KwOJaL7YSRd0CwlRaPNGhprLdBNA/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 389)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 389)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 389)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1OBycTylVOqYlIwVg4CjwjEw_-VpA7N-y/view?usp=sharing" class="pastedDriveLink-0">389.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=389.png;FMTTYPE=image/png:https://drive.google.com/file/d/1OBycTylVOqYlIwVg4CjwjEw_-VpA7N-y/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 390)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 390)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 390)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ly3Uc70WpoJHE4UBW0LwkYPTX0sA5TK1/view?usp=sharing" class="pastedDriveLink-0">390.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=390.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ly3Uc70WpoJHE4UBW0LwkYPTX0sA5TK1/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 391)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 391)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 391)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1tGIXiaj4H2nI5YiB0TzVnoX0wdBv0uyl/view?usp=sharing" class="pastedDriveLink-0">391.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=391.png;FMTTYPE=image/png:https://drive.google.com/file/d/1tGIXiaj4H2nI5YiB0TzVnoX0wdBv0uyl/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 392)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 392)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 392)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1TkdUNk-VhXW7z5jAtas6RwtuyAD6dQ1f/view?usp=sharing" class="pastedDriveLink-0">392.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=392.png;FMTTYPE=image/png:https://drive.google.com/file/d/1TkdUNk-VhXW7z5jAtas6RwtuyAD6dQ1f/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 393)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 393)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 393)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1X4kmviVVmEcwhFboSytoIh9DGeeQT_bc/view?usp=sharing" class="pastedDriveLink-0">393.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=393.png;FMTTYPE=image/png:https://drive.google.com/file/d/1X4kmviVVmEcwhFboSytoIh9DGeeQT_bc/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 394)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 394)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 394)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/14sBTTaB0ZymHrOh5dBW0P0W75q_X9gr4/view?usp=sharing" class="pastedDriveLink-0">394.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=394.png;FMTTYPE=image/png:https://drive.google.com/file/d/14sBTTaB0ZymHrOh5dBW0P0W75q_X9gr4/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 395)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 395)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 395)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/167XkPzH4uy4x9a6dGggrFSAwdreJSPDD/view?usp=sharing" class="pastedDriveLink-0">395.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=395.png;FMTTYPE=image/png:https://drive.google.com/file/d/167XkPzH4uy4x9a6dGggrFSAwdreJSPDD/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 396)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 396)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 396)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1YTp3-L2b-0nQ0coMO94QElsH9TsDEDvZ/view?usp=sharing" class="pastedDriveLink-0">396.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=396.png;FMTTYPE=image/png:https://drive.google.com/file/d/1YTp3-L2b-0nQ0coMO94QElsH9TsDEDvZ/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 397)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 397)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 397)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Nrraw79b2HW-eUixWaQgxGrsksm8yjNH/view?usp=sharing" class="pastedDriveLink-0">397.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=397.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Nrraw79b2HW-eUixWaQgxGrsksm8yjNH/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 398)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 398)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 398)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1geMLGNebrk6w_KCpyw_vWELmwVUbACht/view?usp=sharing" class="pastedDriveLink-0">398.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=398.png;FMTTYPE=image/png:https://drive.google.com/file/d/1geMLGNebrk6w_KCpyw_vWELmwVUbACht/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 399)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 399)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 399)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1UIMdG1j7QskRTZFxJyN1hPM9O3O2hgkA/view?usp=sharing" class="pastedDriveLink-0">399.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=399.png;FMTTYPE=image/png:https://drive.google.com/file/d/1UIMdG1j7QskRTZFxJyN1hPM9O3O2hgkA/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 400)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 400)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 400)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/19Hc3-MMWCWzSPARQb6Nmex8XLGtkkOhj/view?usp=sharing" class="pastedDriveLink-0">400.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=400.png;FMTTYPE=image/png:https://drive.google.com/file/d/19Hc3-MMWCWzSPARQb6Nmex8XLGtkkOhj/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 401)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 401)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 401)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1RbghUkm813rB_QigDOCUdIiMH0-6zXDl/view?usp=sharing" class="pastedDriveLink-0">401.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=401.png;FMTTYPE=image/png:https://drive.google.com/file/d/1RbghUkm813rB_QigDOCUdIiMH0-6zXDl/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 402)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 402)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 402)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/18ENp6F01Pcdp-pItELb65x7EEG4PKSVg/view?usp=sharing" class="pastedDriveLink-0">402.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=402.png;FMTTYPE=image/png:https://drive.google.com/file/d/18ENp6F01Pcdp-pItELb65x7EEG4PKSVg/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 403)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 403)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 403)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1E35ngkj3zQDQM9gO7_UdafSINS2VkDaq/view?usp=sharing" class="pastedDriveLink-0">403.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=403.png;FMTTYPE=image/png:https://drive.google.com/file/d/1E35ngkj3zQDQM9gO7_UdafSINS2VkDaq/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 404)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 404)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 404)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/11K8_QYzRjVCieJzLlQCwqwx00urPyEkt/view?usp=sharing" class="pastedDriveLink-0">404.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=404.png;FMTTYPE=image/png:https://drive.google.com/file/d/11K8_QYzRjVCieJzLlQCwqwx00urPyEkt/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 405)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 405)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 405)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1M4D1CMSwPpsbN24L83zb8ecVvuH1P0Dd/view?usp=sharing" class="pastedDriveLink-0">405.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=405.png;FMTTYPE=image/png:https://drive.google.com/file/d/1M4D1CMSwPpsbN24L83zb8ecVvuH1P0Dd/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 406)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 406)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 406)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1O7G_QMCjvFSrfP_YbInF7B1QSYTKAvrF/view?usp=sharing" class="pastedDriveLink-0">406.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=406.png;FMTTYPE=image/png:https://drive.google.com/file/d/1O7G_QMCjvFSrfP_YbInF7B1QSYTKAvrF/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 407)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 407)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 407)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1zpxOnclRUdMP6w0FP6WSbHnM5Y4Mr_Zt/view?usp=sharing" class="pastedDriveLink-0">407.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=407.png;FMTTYPE=image/png:https://drive.google.com/file/d/1zpxOnclRUdMP6w0FP6WSbHnM5Y4Mr_Zt/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 408)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 408)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 408)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1YPgu7lXAxD64FBDJa1s5TTTeizEI9swa/view?usp=sharing" class="pastedDriveLink-0">408.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=408.png;FMTTYPE=image/png:https://drive.google.com/file/d/1YPgu7lXAxD64FBDJa1s5TTTeizEI9swa/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 409)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 409)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 409)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1aJh4P8Ks6qwKhLJ6KeEvuePlm6Wfq9qc/view?usp=sharing" class="pastedDriveLink-0">409.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=409.png;FMTTYPE=image/png:https://drive.google.com/file/d/1aJh4P8Ks6qwKhLJ6KeEvuePlm6Wfq9qc/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 410)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 410)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 410)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1BB-FRVfYvqP49_lvt2bmIUzFLKKbPDYa/view?usp=sharing" class="pastedDriveLink-0">410.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=410.png;FMTTYPE=image/png:https://drive.google.com/file/d/1BB-FRVfYvqP49_lvt2bmIUzFLKKbPDYa/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 411)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 411)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 411)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Wee8Jln9Tcq1qz8qX8vWp58jNREALhg8/view?usp=sharing" class="pastedDriveLink-0">411.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=411.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Wee8Jln9Tcq1qz8qX8vWp58jNREALhg8/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 412)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 412)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 412)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/11fbFON7hRm2snAniCIi4lYNs9p8LCyY_/view?usp=sharing" class="pastedDriveLink-0">412.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=412.png;FMTTYPE=image/png:https://drive.google.com/file/d/11fbFON7hRm2snAniCIi4lYNs9p8LCyY_/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 413)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 413)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 413)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1v8Xs53qxm7d3n-A6DZkFbuJ1t1wDnBmo/view?usp=sharing" class="pastedDriveLink-0">413.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=413.png;FMTTYPE=image/png:https://drive.google.com/file/d/1v8Xs53qxm7d3n-A6DZkFbuJ1t1wDnBmo/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 414)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 414)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 414)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/117o4wXQVVz1ZKXgI6O60eZrQiO43aN4i/view?usp=sharing" class="pastedDriveLink-0">414.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=414.png;FMTTYPE=image/png:https://drive.google.com/file/d/117o4wXQVVz1ZKXgI6O60eZrQiO43aN4i/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 415)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 415)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 415)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1qaJs0BqK23se6J3bfe1dZb8HQcRabfPS/view?usp=sharing" class="pastedDriveLink-0">415.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=415.png;FMTTYPE=image/png:https://drive.google.com/file/d/1qaJs0BqK23se6J3bfe1dZb8HQcRabfPS/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 416)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 416)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 416)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Qg6094xYFbFJj0Tj37SR5gBZyGU4-XR3/view?usp=sharing" class="pastedDriveLink-0">416.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=416.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Qg6094xYFbFJj0Tj37SR5gBZyGU4-XR3/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 417)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 417)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 417)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/173Wu6VjqwEaouw9rujCTjebTNuRgt9Px/view?usp=sharing" class="pastedDriveLink-0">417.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=417.png;FMTTYPE=image/png:https://drive.google.com/file/d/173Wu6VjqwEaouw9rujCTjebTNuRgt9Px/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 418)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 418)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 418)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1bytC327TYL9UvdnR1tY_xwaJajSFusaR/view?usp=sharing" class="pastedDriveLink-0">418.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=418.png;FMTTYPE=image/png:https://drive.google.com/file/d/1bytC327TYL9UvdnR1tY_xwaJajSFusaR/view?usp=sharing
END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 419)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 419)+"""
UID:7qluq7tpnapsle40btklsiloq8782google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 419)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1BPvj57-KIM-d3ymszCRZB83sBm8oBMMd/view?usp=sharing" class="pastedDriveLink-0">419.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Sof Prep 365 WOD
TRANSP:OPAQUE
ATTACH;FILENAME=419.png;FMTTYPE=image/png:https://drive.google.com/file/d/1BPvj57-KIM-d3ymszCRZB83sBm8oBMMd/view?usp=sharing
END:VEVENT

END:VCALENDAR
"""
    filename = "SofPrep365.ics"
    with open (filename, 'w') as f:
        f.write(workouts)
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