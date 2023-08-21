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
DESCRIPTION:<a href="https://drive.google.com/file/d/15D_48OT71eTZfj5yECdaSlNiaKypk0HQ/view" class="pastedDriveLink-0">w1-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/15D_48OT71eTZfj5yECdaSlNiaKypk0HQ/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 2)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1H_rG4R0F6Qq5QVDkmY2lvLeO4upNrMEo/view" class="pastedDriveLink-0">w1-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1H_rG4R0F6Qq5QVDkmY2lvLeO4upNrMEo/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 3)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
DESCRIPTION:<a href="https://drive.google.com/file/d/1goNDGKBVrH7hNmPNanx59QplNLcNKjBr/view" class="pastedDriveLink-0">w1-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1goNDGKBVrH7hNmPNanx59QplNLcNKjBr/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 4)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Fky2S2Kt2UYwdqbBo8fL_EhFveUYd6mz/view" class="pastedDriveLink-0">w1-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Fky2S2Kt2UYwdqbBo8fL_EhFveUYd6mz/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 5)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1pGlMfsbi8jc76rOu0A83SI2x9nA57kxP/view" class="pastedDriveLink-0">w1-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1pGlMfsbi8jc76rOu0A83SI2x9nA57kxP/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 6)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1s4HjyWFmmthBi8RT83HxUCWxwLL8A59J/view" class="pastedDriveLink-0">w1-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1s4HjyWFmmthBi8RT83HxUCWxwLL8A59J/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 7)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1zPcIOLbIdLgKsHMe4PuRfuqJLZcw1ak1/view" class="pastedDriveLink-1">w1-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1zPcIOLbIdLgKsHMe4PuRfuqJLZcw1ak1/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 8)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1F-mIOGPJ_Ub60-cGgtRuV5S_VX2sT52E/view" class="pastedDriveLink-1">w2-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1F-mIOGPJ_Ub60-cGgtRuV5S_VX2sT52E/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 9)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1xl80oZ6HW3oFDuYTVyLk1pPkU78IPhvn/view" class="pastedDriveLink-0">w2-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1xl80oZ6HW3oFDuYTVyLk1pPkU78IPhvn/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 10)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1MhjN4JEO1kFCH9-pB8HOzZAqyonIg-Qe/view" class="pastedDriveLink-0">w2-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1MhjN4JEO1kFCH9-pB8HOzZAqyonIg-Qe/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 11)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
DESCRIPTION:<a href="https://drive.google.com/file/d/1LxuZ-49OIv76DRGuXJqdAcCOhB7C74kg/view" class="pastedDriveLink-0">w2-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1LxuZ-49OIv76DRGuXJqdAcCOhB7C74kg/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 12)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1C2jlzjm6OcC6b68p2Ilnlo9t_dz6dvqM/view" class="pastedDriveLink-1">w2-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1C2jlzjm6OcC6b68p2Ilnlo9t_dz6dvqM/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 13)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1dhltfVtQv0P_b-1Oi_7aH2FfzzMjar4p/view" class="pastedDriveLink-0">w2-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1dhltfVtQv0P_b-1Oi_7aH2FfzzMjar4p/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 14)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1RnrsRNyUXvi2jTN_xxL_1Anfk8sG9llP/view" class="pastedDriveLink-0">w2-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1RnrsRNyUXvi2jTN_xxL_1Anfk8sG9llP/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 15)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1KXkn6nS4koujM1Swa_GHOJ8QIf3o_fZ4/view" class="pastedDriveLink-0">w3-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1KXkn6nS4koujM1Swa_GHOJ8QIf3o_fZ4/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 16)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/17RjN_fkPPCThxEeZK1CBV01P4JjHd9n4/view" class="pastedDriveLink-0">w3-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/17RjN_fkPPCThxEeZK1CBV01P4JjHd9n4/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 17)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1WDNAFgAqALkiHD224Gq1sC5u2X_TJKNj/view" class="pastedDriveLink-0">w3-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1WDNAFgAqALkiHD224Gq1sC5u2X_TJKNj/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 18)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1cOkSB0rvweEFGJ8yMXx3VP704LcG0Q_v/view" class="pastedDriveLink-0">w3-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1cOkSB0rvweEFGJ8yMXx3VP704LcG0Q_v/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 19)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1VjVPf9EZY0N6vgPCfAZzGLwsh7hJ-QAC/view" class="pastedDriveLink-0">w3-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1VjVPf9EZY0N6vgPCfAZzGLwsh7hJ-QAC/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 20)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1YPen4rTBoGeFyJe9R7BAjrbXwohhJBIK/view" class="pastedDriveLink-0">w3-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1YPen4rTBoGeFyJe9R7BAjrbXwohhJBIK/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 21)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1VDlHCGDmzMfDbnWnSE-a5_vieDCJmn8S/view" class="pastedDriveLink-0">w3-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1VDlHCGDmzMfDbnWnSE-a5_vieDCJmn8S/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 22)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1v7Hca-h_CWEx6IApJ4kTvKBWFdxcR4k8/view" class="pastedDriveLink-0">w4-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1v7Hca-h_CWEx6IApJ4kTvKBWFdxcR4k8/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 23)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1oaWNTq72cVpLOCTvLLLUyBV1eL0YnBeK/view" class="pastedDriveLink-0">w4-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1oaWNTq72cVpLOCTvLLLUyBV1eL0YnBeK/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 24)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1nABzeKiiDADCdoEKZ25miZ22ZqHk7v0u/view" class="pastedDriveLink-0">w4-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1nABzeKiiDADCdoEKZ25miZ22ZqHk7v0u/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 25)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1VC70XSP9MQ0tBS4q8RWg_uBkuxDc7Et_/view" class="pastedDriveLink-0">w4-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1VC70XSP9MQ0tBS4q8RWg_uBkuxDc7Et_/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 26)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1fRt3M5TGEu10gW0uuDKZWoMqyWTvldqB/view" class="pastedDriveLink-0">w4-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1fRt3M5TGEu10gW0uuDKZWoMqyWTvldqB/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 27)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/163DFZyMexpESKq7jrxj04cSe8TV0yZ80/view" class="pastedDriveLink-0">w4-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/163DFZyMexpESKq7jrxj04cSe8TV0yZ80/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 28)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1c-3hh4xdwbIPmUkYSA1HJEHPXCOBxj1A/view" class="pastedDriveLink-0">w4-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1c-3hh4xdwbIPmUkYSA1HJEHPXCOBxj1A/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 29)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1CBfvzHGkvOInoK73LlkpkRnPMWqywCXM/view" class="pastedDriveLink-0">w5-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1CBfvzHGkvOInoK73LlkpkRnPMWqywCXM/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 30)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1_Y1e06ZkVo4MMO3tdUIWpCJemjPRANCn/view" class="pastedDriveLink-0">w5-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_Y1e06ZkVo4MMO3tdUIWpCJemjPRANCn/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 31)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Ay2yooNXNBaDcDA1E1i1Qp1ZnPdPThb_/view" class="pastedDriveLink-0">w5-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Ay2yooNXNBaDcDA1E1i1Qp1ZnPdPThb_/view

END:VEVENT
"""
    workout_list_last_30 = """
BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 32)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1yG6tFhiqF6B8Ewpwckr_lc7Zr_oFeBTF/view" class="pastedDriveLink-0">w5-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1yG6tFhiqF6B8Ewpwckr_lc7Zr_oFeBTF/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 33)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/16u58MJEdiWwfNoHHEnnibR-DwA5MLORu/view" class="pastedDriveLink-0">w5-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/16u58MJEdiWwfNoHHEnnibR-DwA5MLORu/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 34)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1F-os4HhkUHFCWO_mWl7OBpMTgvAhd5CC/view" class="pastedDriveLink-0">w5-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1F-os4HhkUHFCWO_mWl7OBpMTgvAhd5CC/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 35)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1huhqOi8iEzG6CD5muWGkKYld4bTBqmbI/view" class="pastedDriveLink-0" id="ow32708" __is_owner="true">w5-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1huhqOi8iEzG6CD5muWGkKYld4bTBqmbI/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 36)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1VP3P9G4EyX9GxzcUdeZttVIKjpJQrYGq/view" class="pastedDriveLink-1">w6-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1VP3P9G4EyX9GxzcUdeZttVIKjpJQrYGq/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 37)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/11iGr-LWLQ1M4jicug8ASCyJAwDyrohYR/view" class="pastedDriveLink-0">w6-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/11iGr-LWLQ1M4jicug8ASCyJAwDyrohYR/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 38)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1XwdzuEXORO9ZkFgsjc2Z49N7HSD-3n2Y/view" class="pastedDriveLink-0">w6-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1XwdzuEXORO9ZkFgsjc2Z49N7HSD-3n2Y/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 39)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1UD3y8IeGrtm47XIraFSIq6kgDp68TvRz/view" class="pastedDriveLink-0">w6-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1UD3y8IeGrtm47XIraFSIq6kgDp68TvRz/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 40)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/12y1-6ZS5DFZNmC0fjrgMaFltpYPXCHpx/view" class="pastedDriveLink-0">w6-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/12y1-6ZS5DFZNmC0fjrgMaFltpYPXCHpx/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 41)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1-UFCUPfr8HIrRPobXAu_jZYNAgRboV09/view" class="pastedDriveLink-0">w6-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1-UFCUPfr8HIrRPobXAu_jZYNAgRboV09/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 42)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1joSDUbnxWynG7xzfCYzVxBpoDfGBH1GW/view" class="pastedDriveLink-0">w6-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1joSDUbnxWynG7xzfCYzVxBpoDfGBH1GW/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 43)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1UIjY4pGgk-qbn3YnbKLOc6HOHu1dVy-O/view" class="pastedDriveLink-0">w7-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1UIjY4pGgk-qbn3YnbKLOc6HOHu1dVy-O/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 44)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1UIjY4pGgk-qbn3YnbKLOc6HOHu1dVy-O/view" class="pastedDriveLink-0">w7-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1UIjY4pGgk-qbn3YnbKLOc6HOHu1dVy-O/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 45)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1arnUyIXYyOLdZHgRTN9Zo1Aoa2y_0X8x/view" class="pastedDriveLink-0">w7-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1arnUyIXYyOLdZHgRTN9Zo1Aoa2y_0X8x/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 46)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1j6DUHM0f-85t8cIAxEgLOIAV8bxTibcX/view" class="pastedDriveLink-0">w7-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1j6DUHM0f-85t8cIAxEgLOIAV8bxTibcX/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 47)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1HVx0R7Tst2J_1OHlone6Qr1UzS9kA5Gb/view" class="pastedDriveLink-0">w7-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1HVx0R7Tst2J_1OHlone6Qr1UzS9kA5Gb/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 48)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1j6NgB72fzY7_F65aIrYnHTyjCyZ2m4E1/view" class="pastedDriveLink-0">w7-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1j6NgB72fzY7_F65aIrYnHTyjCyZ2m4E1/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 49)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1EPRcLH0o9oJSqJuu86FZO3oU4EblEnDP/view" class="pastedDriveLink-0">w7-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1EPRcLH0o9oJSqJuu86FZO3oU4EblEnDP/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 50)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1nQy-SYE7GXYziagsm3DuoPRi2sTEHK3w/view" class="pastedDriveLink-0">w8-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1nQy-SYE7GXYziagsm3DuoPRi2sTEHK3w/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 51)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1jTg-Gn2GmAbfOobI0jSHdOgZjY-ZH26c/view" class="pastedDriveLink-0">w8-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1jTg-Gn2GmAbfOobI0jSHdOgZjY-ZH26c/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 52)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Dd81bJrY5V0nuk2VZfbWwJoQWMlZLAhS/view" class="pastedDriveLink-0">w8-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Dd81bJrY5V0nuk2VZfbWwJoQWMlZLAhS/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 53)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Clh0CtA2H5pzusV78O3EMy5k3V2lFNHE/view" class="pastedDriveLink-0">w8-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Clh0CtA2H5pzusV78O3EMy5k3V2lFNHE/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 54)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/191y3p5Abau4pOSBkBWpQV_u2J4GGITj1/view" class="pastedDriveLink-0">w8-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/191y3p5Abau4pOSBkBWpQV_u2J4GGITj1/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 55)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Gf3otw2IqdawfSr1XtdGB6DZj5Mq17UD/view" class="pastedDriveLink-0">w8-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Gf3otw2IqdawfSr1XtdGB6DZj5Mq17UD/view

END:VEVENT

BEGIN:VEVENT
DTSTART;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
DTEND;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID;TZID=America/Anchorage:"""+fix_date(init_date, 56)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1NkgSWIuPxa5DV4jZtDPxvvqV25B3Sp8a/view" class="pastedDriveLink-0">w8-d7.png</a><br><br>you did it.&nbsp\;<br>now move on to the next mountain to conquer.
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1NkgSWIuPxa5DV4jZtDPxvvqV25B3Sp8a/view
END:VEVENT

END:VCALENDAR
"""
    filename = "HTK_Tactical_Monster_Workout_Plan.ics"
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