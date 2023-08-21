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
DESCRIPTION:<a href="https://drive.google.com/file/d/13w6_XU_E7bM4KCHoYKUmKFB8UYUX6Fy9/view?usp=sharing" class="pastedDriveLink-0">w1-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/13w6_XU_E7bM4KCHoYKUmKFB8UYUX6Fy9/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1gMs_DJQQiQ9P7rLXnqWWh_2NSnOcF4QK/view?usp=sharing" class="pastedDriveLink-0">w1-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1gMs_DJQQiQ9P7rLXnqWWh_2NSnOcF4QK/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
DESCRIPTION:<a href="https://drive.google.com/file/d/11wTUbHJAqVY02siqIjqC1dSoPmIypI-f/view?usp=sharing" class="pastedDriveLink-0">w1-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/11wTUbHJAqVY02siqIjqC1dSoPmIypI-f/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1IKOFogCQYy48aqKVUxPDAW2oWLDL48P-/view?usp=sharing" class="pastedDriveLink-0">w1-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1IKOFogCQYy48aqKVUxPDAW2oWLDL48P-/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/12sCU42xCuAw2_FYjU4amc2HGmYbHv3GL/view?usp=sharing" class="pastedDriveLink-0">w1-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/12sCU42xCuAw2_FYjU4amc2HGmYbHv3GL/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1k1NllPSwH7zxkH3WwejyBWbp3g6CnMiZ/view?usp=sharing" class="pastedDriveLink-0">w1-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1k1NllPSwH7zxkH3WwejyBWbp3g6CnMiZ/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1FSdnFix4bJFwDMtz4z2eyCdsL3Z9bDYB/view?usp=sharing" class="pastedDriveLink-1">w1-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1FSdnFix4bJFwDMtz4z2eyCdsL3Z9bDYB/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1RFbAkHXYNIOdeu-IV9zSPgI7Y2OyZFVr/view?usp=sharing" class="pastedDriveLink-1">w2-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1RFbAkHXYNIOdeu-IV9zSPgI7Y2OyZFVr/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1gAjR6P7EIw9LkjGsYOmt13tjLzMv0DMe/view?usp=sharing" class="pastedDriveLink-0">w2-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1gAjR6P7EIw9LkjGsYOmt13tjLzMv0DMe/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1CaAURWcNFeueYEteR8wxElb3uq_q_Skb/view?usp=sharing" class="pastedDriveLink-0">w2-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1CaAURWcNFeueYEteR8wxElb3uq_q_Skb/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
DESCRIPTION:<a href="https://drive.google.com/file/d/1JPXFYWZB5rIjXDhstnJXWPifdu-lus3i/view?usp=sharing" class="pastedDriveLink-0">w2-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1JPXFYWZB5rIjXDhstnJXWPifdu-lus3i/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/18euvs-SBMSVFnrZiRubxDX1M3XkhHf4s/view?usp=sharing" class="pastedDriveLink-1">w2-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/18euvs-SBMSVFnrZiRubxDX1M3XkhHf4s/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ORtoZSe6vpicbOwxrwhz89PJ56AwzsYE/view?usp=sharing" class="pastedDriveLink-0">w2-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ORtoZSe6vpicbOwxrwhz89PJ56AwzsYE/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1e6JlOEwc-_LSR7EGzk0B7Mu9K7uo5ufE/view?usp=sharing" class="pastedDriveLink-0">w2-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1e6JlOEwc-_LSR7EGzk0B7Mu9K7uo5ufE/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1w_1mdsJoZDtzDg_l0kUb5rflplyNXaCM/view?usp=sharing" class="pastedDriveLink-0">w3-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1w_1mdsJoZDtzDg_l0kUb5rflplyNXaCM/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1jC9TX8EX4CUWrnJUS95Coizyww4Uu3Zp/view?usp=sharing" class="pastedDriveLink-0">w3-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1jC9TX8EX4CUWrnJUS95Coizyww4Uu3Zp/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Y4laY4N6MKRw5ynZVKQGZLl4z1l4RbJk/view?usp=sharing" class="pastedDriveLink-0">w3-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Y4laY4N6MKRw5ynZVKQGZLl4z1l4RbJk/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1AUJwv1JTvktK5IsmThJv8BIVgLjsBWlG/view?usp=sharing" class="pastedDriveLink-0">w3-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1AUJwv1JTvktK5IsmThJv8BIVgLjsBWlG/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Gjr5kBNUGvFX2jlpG4Nl5vVRR8TloArq/view?usp=sharing" class="pastedDriveLink-0">w3-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Gjr5kBNUGvFX2jlpG4Nl5vVRR8TloArq/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1bJHyVNz1H2iDvWLHsCKY0quk9CK0jwDW/view?usp=sharing" class="pastedDriveLink-0">w3-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1bJHyVNz1H2iDvWLHsCKY0quk9CK0jwDW/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1PaejswFf6frzPoGAzPBf_ohA3G9WNfH_/view?usp=sharing" class="pastedDriveLink-0">w3-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1PaejswFf6frzPoGAzPBf_ohA3G9WNfH_/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/13qf0cp0Xxf4qlC8ppL9tGF05v5ezUhZH/view?usp=sharing" class="pastedDriveLink-0">w4-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/13qf0cp0Xxf4qlC8ppL9tGF05v5ezUhZH/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ngeJp_GaNbF-wxRmSuBZaSxn8Z71zG48/view?usp=sharing" class="pastedDriveLink-0">w4-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ngeJp_GaNbF-wxRmSuBZaSxn8Z71zG48/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1cL50Tpw2gK7sbexYSnK5MlrjMplndcHe/view?usp=sharing" class="pastedDriveLink-0">w4-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1cL50Tpw2gK7sbexYSnK5MlrjMplndcHe/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1vMEPVryV5yk0FnRo0kE0LLGCKSkGqAhy/view?usp=sharing" class="pastedDriveLink-0">w4-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1vMEPVryV5yk0FnRo0kE0LLGCKSkGqAhy/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1eHZAiNskkc0Z4EshaWy4yrJ_gvjKEBos/view?usp=sharing" class="pastedDriveLink-0">w4-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1eHZAiNskkc0Z4EshaWy4yrJ_gvjKEBos/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Q7Eog8wDjnw1_djXbTdvxA0hyVkzmTD2/view?usp=sharing" class="pastedDriveLink-0">w4-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Q7Eog8wDjnw1_djXbTdvxA0hyVkzmTD2/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1XQo40bjNseuGZp3ojp_MVkzxVcvfCpc3/view?usp=sharing" class="pastedDriveLink-0">w4-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1XQo40bjNseuGZp3ojp_MVkzxVcvfCpc3/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/14StY0la0IyqqQFnn-pgPwlTcFvNchPZW/view?usp=sharing" class="pastedDriveLink-0">w5-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/14StY0la0IyqqQFnn-pgPwlTcFvNchPZW/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1hRsUkk1PHgNSlZ4oRcVyqVw8dM7vApzX/view?usp=sharing" class="pastedDriveLink-0">w5-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1hRsUkk1PHgNSlZ4oRcVyqVw8dM7vApzX/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1zL229cO0Lptd-Rnsm614BFiMgUKLWAPy/view?usp=sharing" class="pastedDriveLink-0">w5-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1zL229cO0Lptd-Rnsm614BFiMgUKLWAPy/view?usp=sharing

END:VEVENT
"""
    workout_list_last_30 = """
BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1lc_FZ_mif9UAxob9RPajbyABJrKpr-3j/view?usp=sharing" class="pastedDriveLink-0">w5-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1lc_FZ_mif9UAxob9RPajbyABJrKpr-3j/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1hmkiYXefUwIQjMTHIM7YadX2JmZHpn7x/view?usp=sharing" class="pastedDriveLink-0">w5-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1hmkiYXefUwIQjMTHIM7YadX2JmZHpn7x/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1qSmAphapX8t-Vsz39xcg6hZvXnCyTsb4/view?usp=sharing" class="pastedDriveLink-0">w5-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1qSmAphapX8t-Vsz39xcg6hZvXnCyTsb4/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/10Lo6Kfyisw9QLm2oxpftB6C2KhxUbJo9/view?usp=sharing" class="pastedDriveLink-0" id="ow32708" __is_owner="true">w5-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/10Lo6Kfyisw9QLm2oxpftB6C2KhxUbJo9/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1yg5V8bHfaDxuXdYPKaG7ICgv4CyEbDWV/view?usp=sharing" class="pastedDriveLink-1">w6-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1yg5V8bHfaDxuXdYPKaG7ICgv4CyEbDWV/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1LFJWKJkfCS5MyullFj71v46akojtMe4Z/view?usp=sharing" class="pastedDriveLink-0">w6-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1LFJWKJkfCS5MyullFj71v46akojtMe4Z/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1-5ca9d-2dFDxHyRh2_UnGsI_hwsInnYn/view?usp=sharing" class="pastedDriveLink-0">w6-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1-5ca9d-2dFDxHyRh2_UnGsI_hwsInnYn/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/11GGQdeI-1NkWkTD5UvWrYrbBhcYDJscL/view?usp=sharing" class="pastedDriveLink-0">w6-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/11GGQdeI-1NkWkTD5UvWrYrbBhcYDJscL/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1A-QFjNE6O_6gd1TFn4Ov6QNpWc3s6NKv/view?usp=sharing" class="pastedDriveLink-0">w6-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1A-QFjNE6O_6gd1TFn4Ov6QNpWc3s6NKv/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/167Lr4-K0Ysr_A5xlY_dJnWk6HIR-596d/view?usp=sharing" class="pastedDriveLink-0">w6-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/167Lr4-K0Ysr_A5xlY_dJnWk6HIR-596d/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/167Lr4-K0Ysr_A5xlY_dJnWk6HIR-596d/view?usp=sharing" class="pastedDriveLink-0">w6-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/167Lr4-K0Ysr_A5xlY_dJnWk6HIR-596d/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1aPHdP6hYEyXO303Srh3SliarVzSYI9ds/view?usp=sharing" class="pastedDriveLink-0">w7-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1aPHdP6hYEyXO303Srh3SliarVzSYI9ds/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1opw_5z8G2MU2KQI6U-ZSTOo8Eqy16Cfv/view?usp=sharing" class="pastedDriveLink-0">w7-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1opw_5z8G2MU2KQI6U-ZSTOo8Eqy16Cfv/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1thp-TtCj3NIsihy7bGXFRnk1RXIrxNbW/view?usp=sharing" class="pastedDriveLink-0">w7-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1thp-TtCj3NIsihy7bGXFRnk1RXIrxNbW/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1cAfO6ouCpu9iNsKDVIut5ismGMkiDVXc/view?usp=sharing" class="pastedDriveLink-0">w7-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1cAfO6ouCpu9iNsKDVIut5ismGMkiDVXc/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1S2CJxnF_d1rtSKfKThxDH4OX5sWv_-xL/view?usp=sharing" class="pastedDriveLink-0">w7-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1S2CJxnF_d1rtSKfKThxDH4OX5sWv_-xL/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1zBnCMakD2KVq0ItF9ur89OPKXMp6UwVK/view?usp=sharing" class="pastedDriveLink-0">w7-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1zBnCMakD2KVq0ItF9ur89OPKXMp6UwVK/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1xM58ayLxakRRbULOciu1BQGjNrRcVdmN/view?usp=sharing" class="pastedDriveLink-0">w7-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1xM58ayLxakRRbULOciu1BQGjNrRcVdmN/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1uIp0o4mYKj0WOLVrvNlwzQQtucCeev4V/view?usp=sharing" class="pastedDriveLink-0">w8-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1uIp0o4mYKj0WOLVrvNlwzQQtucCeev4V/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ltuh-m3uvCyyprz-V66-VKjrRzORzrDF/view?usp=sharing" class="pastedDriveLink-0">w8-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ltuh-m3uvCyyprz-V66-VKjrRzORzrDF/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1nwYLSn8uTAx5egdGl8ACCcgjBnoyudeF/view?usp=sharing" class="pastedDriveLink-0">w8-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1nwYLSn8uTAx5egdGl8ACCcgjBnoyudeF/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1e_aPnKchWGnTBa88kFmmMBfxWKyje0dQ/view?usp=sharing" class="pastedDriveLink-0">w8-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1e_aPnKchWGnTBa88kFmmMBfxWKyje0dQ/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1VbKksqO0AVCHvOcNiRRo-CuyZksqOpHN/view?usp=sharing" class="pastedDriveLink-0">w8-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1VbKksqO0AVCHvOcNiRRo-CuyZksqOpHN/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1FiH0VZrXJje98TjlcEr92zWfII_lZvBa/view?usp=sharing" class="pastedDriveLink-0">w8-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1FiH0VZrXJje98TjlcEr92zWfII_lZvBa/view?usp=sharing

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/101NvXwD09kFCaX9uNnv5Sdg8ATNB5CHt/view?usp=sharing" class="pastedDriveLink-0">w8-d7.png</a><br><br>you did it.&nbsp\;<br>now move on to the next mountain to conquer.
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/101NvXwD09kFCaX9uNnv5Sdg8ATNB5CHt/view?usp=sharing

END:VEVENT

END:VCALENDAR
"""
    filename = "HTK_Built_Different_HOME_Workout_Plan.ics"
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