import datetime
from doctest import Example
import sys
import climage


def fix_date(date, days_offset):
    return str(date + datetime.timedelta(days=days_offset-1)).replace(":", "").replace("-", "").replace(" ", "T")


def generate_workout_list(init_date):
    workout_list_first_30 = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Google Inc//Google Calendar 70.9054//EN

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 1)+"""
DTEND:"""+fix_date(init_date, 1)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 1)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1vmMBOAfGiA8bl4X_Bk1LOxYd5s4_qld5/view?usp=share_link" class="pastedDriveLink-0">w1-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1vmMBOAfGiA8bl4X_Bk1LOxYd5s4_qld5/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 2)+"""
DTEND:"""+fix_date(init_date, 2)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 2)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1_Xl6Fo7L80HE2kwUf8SVA4AbfPAH38EO/view?usp=share_link" class="pastedDriveLink-0">w1-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_Xl6Fo7L80HE2kwUf8SVA4AbfPAH38EO/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 3)+"""
DTEND:"""+fix_date(init_date, 3)+"""
RECURRENCE-ID:"""+fix_date(init_date, 3)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
DESCRIPTION:<a href="https://drive.google.com/file/d/17LyXGqBkUEgztfLLuxUmmWduuspPwhOy/view?usp=share_link" class="pastedDriveLink-0">w1-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/17LyXGqBkUEgztfLLuxUmmWduuspPwhOy/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 4)+"""
DTEND:"""+fix_date(init_date, 4)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 4)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1WfefD8d4anflLBBfpnPneAIJ4wNPtHs0/view?usp=share_link" class="pastedDriveLink-0">w1-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1WfefD8d4anflLBBfpnPneAIJ4wNPtHs0/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 5)+"""
DTEND:"""+fix_date(init_date, 5)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 5)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Ic2HUNP6P2CTKvpLpi4g1aGqaoIpNvbH/view?usp=share_link" class="pastedDriveLink-0">w1-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Ic2HUNP6P2CTKvpLpi4g1aGqaoIpNvbH/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 6)+"""
DTEND:"""+fix_date(init_date, 6)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 6)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1kQxW-KhYRBf0Eh8uUO4m7MfU7scFTnJC/view?usp=share_link" class="pastedDriveLink-0">w1-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1kQxW-KhYRBf0Eh8uUO4m7MfU7scFTnJC/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 7)+"""
DTEND:"""+fix_date(init_date, 7)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 7)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1tT4SoFYwA0Yt1FVwAY539vTaEA80sJc1/view?usp=share_link" class="pastedDriveLink-1">w1-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w1-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1tT4SoFYwA0Yt1FVwAY539vTaEA80sJc1/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 8)+"""
DTEND:"""+fix_date(init_date, 8)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 8)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ysKdqKIfPLboa_hPZ-mXFIstou7-lDDE/view?usp=share_link" class="pastedDriveLink-1">w2-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ysKdqKIfPLboa_hPZ-mXFIstou7-lDDE/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 9)+"""
DTEND:"""+fix_date(init_date, 9)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 9)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/11MKD_JMqZVQO9XEeME2QqByIozwvGrps/view?usp=share_link" class="pastedDriveLink-0">w2-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/11MKD_JMqZVQO9XEeME2QqByIozwvGrps/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 10)+"""
DTEND:"""+fix_date(init_date, 10)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 10)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1DlHNeMd8nfLX36w8WkY1d3i3TjW8CHwo/view?usp=share_link" class="pastedDriveLink-0">w2-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1DlHNeMd8nfLX36w8WkY1d3i3TjW8CHwo/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 11)+"""
DTEND:"""+fix_date(init_date, 11)+"""
RECURRENCE-ID:"""+fix_date(init_date, 11)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
DESCRIPTION:<a href="https://drive.google.com/file/d/1_zDMMnxw19oa_VydFhlKy97A1aNS_qMI/view?usp=share_link" class="pastedDriveLink-0">w2-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_zDMMnxw19oa_VydFhlKy97A1aNS_qMI/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 12)+"""
DTEND:"""+fix_date(init_date, 12)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 12)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/16unzOpfw0meuz16FgclD4l08t3ZD1Ucd/view?usp=share_link" class="pastedDriveLink-1">w2-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/16unzOpfw0meuz16FgclD4l08t3ZD1Ucd/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 13)+"""
DTEND:"""+fix_date(init_date, 13)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 13)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1qpa88qDGsAL5DGcjuGp7qFwqDZ_ZL_9Q/view?usp=share_link" class="pastedDriveLink-0">w2-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1qpa88qDGsAL5DGcjuGp7qFwqDZ_ZL_9Q/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 14)+"""
DTEND:"""+fix_date(init_date, 14)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 14)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1khdoWrR0kHzytjK4ZhVKku33X4C9RKtj/view?usp=share_link" class="pastedDriveLink-0">w2-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w2-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1khdoWrR0kHzytjK4ZhVKku33X4C9RKtj/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 15)+"""
DTEND:"""+fix_date(init_date, 15)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 15)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1VMsdGN9bm3R5UIDRFFhhPeSMJlsjrS80/view?usp=share_link" class="pastedDriveLink-0">w3-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1VMsdGN9bm3R5UIDRFFhhPeSMJlsjrS80/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 16)+"""
DTEND:"""+fix_date(init_date, 16)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 16)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1zBowErF2-7OBB8KAYU7E2XRtEH3gSlqw/view?usp=share_link" class="pastedDriveLink-0">w3-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1zBowErF2-7OBB8KAYU7E2XRtEH3gSlqw/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 17)+"""
DTEND:"""+fix_date(init_date, 17)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 17)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1kIBL7ASjdqvKtEObDVoZXB27h3xBwHaQ/view?usp=share_link" class="pastedDriveLink-0">w3-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1kIBL7ASjdqvKtEObDVoZXB27h3xBwHaQ/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 18)+"""
DTEND:"""+fix_date(init_date, 18)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 18)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1llS0bIWi3QWUKPSzrjY_vBuXjs-TAYtY/view?usp=share_link" class="pastedDriveLink-0">w3-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1llS0bIWi3QWUKPSzrjY_vBuXjs-TAYtY/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 19)+"""
DTEND:"""+fix_date(init_date, 19)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 19)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Wlu61VtxiV0WC54AZsIkQzuOGjq88X9M/view?usp=share_link" class="pastedDriveLink-0">w3-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Wlu61VtxiV0WC54AZsIkQzuOGjq88X9M/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 20)+"""
DTEND:"""+fix_date(init_date, 20)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 20)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1CJw3u6CsChVZbeRq0LqCTW0Q6IkM5o8C/view?usp=share_link" class="pastedDriveLink-0">w3-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1CJw3u6CsChVZbeRq0LqCTW0Q6IkM5o8C/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 21)+"""
DTEND:"""+fix_date(init_date, 21)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 21)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1sObhzVUUaeyYk8db9hhD9JiX_ReD8god/view?usp=share_link" class="pastedDriveLink-0">w3-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w3-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1sObhzVUUaeyYk8db9hhD9JiX_ReD8god/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 22)+"""
DTEND:"""+fix_date(init_date, 22)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 22)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Zc7bkWV1Zm0HspOefwMukWlVxRYpb_xC/view?usp=share_link" class="pastedDriveLink-0">w4-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Zc7bkWV1Zm0HspOefwMukWlVxRYpb_xC/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 23)+"""
DTEND:"""+fix_date(init_date, 23)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 23)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Qpindw7n12lGCDIvWclEyBK68fn8SV20/view?usp=share_link" class="pastedDriveLink-0">w4-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Qpindw7n12lGCDIvWclEyBK68fn8SV20/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 24)+"""
DTEND:"""+fix_date(init_date, 24)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 24)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1vnUEg-v0v3ycVUb84YSBj5JWpsT_7SlS/view?usp=share_link" class="pastedDriveLink-0">w4-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1vnUEg-v0v3ycVUb84YSBj5JWpsT_7SlS/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 25)+"""
DTEND:"""+fix_date(init_date, 25)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 25)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1NscBj3r96oEcuq7qfkahEDAxDQ_Qt6yj/view?usp=share_link" class="pastedDriveLink-0">w4-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1NscBj3r96oEcuq7qfkahEDAxDQ_Qt6yj/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 26)+"""
DTEND:"""+fix_date(init_date, 26)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 26)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1cd62p82SCp4t1fxlXu4-IARtp_0Z57pf/view?usp=share_link" class="pastedDriveLink-0">w4-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1cd62p82SCp4t1fxlXu4-IARtp_0Z57pf/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 27)+"""
DTEND:"""+fix_date(init_date, 27)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 27)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1nb5ZPcEGQewXTEqo1pNEjBwPkzrJ2OMh/view?usp=share_link" class="pastedDriveLink-0">w4-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1nb5ZPcEGQewXTEqo1pNEjBwPkzrJ2OMh/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 28)+"""
DTEND:"""+fix_date(init_date, 28)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 28)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1iKYGZ4H72m0X0EJfgol1qElEN0dqiWxO/view?usp=share_link" class="pastedDriveLink-0">w4-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w4-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1iKYGZ4H72m0X0EJfgol1qElEN0dqiWxO/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 29)+"""
DTEND:"""+fix_date(init_date, 29)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 29)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1ptvA5L1sjKKDe1CJe6i8NuZk5nKahjLq/view?usp=share_link" class="pastedDriveLink-0">w5-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1ptvA5L1sjKKDe1CJe6i8NuZk5nKahjLq/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 30)+"""
DTEND:"""+fix_date(init_date, 30)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 30)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1rXKLebwGK5EqEj154LaY8NzJ-2T0LMgi/view?usp=share_link" class="pastedDriveLink-0">w5-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1rXKLebwGK5EqEj154LaY8NzJ-2T0LMgi/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 31)+"""
DTEND:"""+fix_date(init_date, 31)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 31)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1lX-3RyUtFmeh2te_wJcsKd01rsUeNlW5/view?usp=share_link" class="pastedDriveLink-0">w5-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1lX-3RyUtFmeh2te_wJcsKd01rsUeNlW5/view?usp=share_link

END:VEVENT
"""
    workout_list_last_30 = """
BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 32)+"""
DTEND:"""+fix_date(init_date, 32)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 32)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1JdO6WFoGcfOxRkKOcmzVUYoh6qPArqvx/view?usp=share_link" class="pastedDriveLink-0">w5-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1JdO6WFoGcfOxRkKOcmzVUYoh6qPArqvx/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 33)+"""
DTEND:"""+fix_date(init_date, 33)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 33)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1dehCfNiJaEq8a-6n1G-f5O5YhZbDmHJN/view?usp=share_link" class="pastedDriveLink-0">w5-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1dehCfNiJaEq8a-6n1G-f5O5YhZbDmHJN/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 34)+"""
DTEND:"""+fix_date(init_date, 34)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 34)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1tmlLzAT0EvHW5GOYqjF68fzNHVajAgk_/view?usp=share_link" class="pastedDriveLink-0">w5-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1tmlLzAT0EvHW5GOYqjF68fzNHVajAgk_/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 35)+"""
DTEND:"""+fix_date(init_date, 35)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 35)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1LaL4Z_8njKnglGyTmus57eIARkfculhV/view?usp=share_link" class="pastedDriveLink-0" id="ow32708" __is_owner="true">w5-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w5-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1LaL4Z_8njKnglGyTmus57eIARkfculhV/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 36)+"""
DTEND:"""+fix_date(init_date, 36)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 36)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1YW43cIhEujs46Rw6YyRZP4Kw_ixuj96W/view?usp=share_link" class="pastedDriveLink-1">w6-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1YW43cIhEujs46Rw6YyRZP4Kw_ixuj96W/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 37)+"""
DTEND:"""+fix_date(init_date, 37)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 37)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1XwTvhzlHlaD6uCOaXHgZTrzSrz-ueh71/view?usp=share_link" class="pastedDriveLink-0">w6-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1XwTvhzlHlaD6uCOaXHgZTrzSrz-ueh71/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 38)+"""
DTEND:"""+fix_date(init_date, 38)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 38)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/175PZO0UkICGEvNrfUIVbLeK_Ysh-DU7x/view?usp=share_link" class="pastedDriveLink-0">w6-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/175PZO0UkICGEvNrfUIVbLeK_Ysh-DU7x/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 39)+"""
DTEND:"""+fix_date(init_date, 39)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 39)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1LBk6aDgRJzhkMNNXp8al6Kt-7rN9Jqg-/view?usp=share_link" class="pastedDriveLink-0">w6-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1LBk6aDgRJzhkMNNXp8al6Kt-7rN9Jqg-/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 40)+"""
DTEND:"""+fix_date(init_date, 40)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 40)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1DxgQbH-fGkqJRcrg3PXTpEfsVFkh5o5o/view?usp=share_link" class="pastedDriveLink-0">w6-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1DxgQbH-fGkqJRcrg3PXTpEfsVFkh5o5o/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 41)+"""
DTEND:"""+fix_date(init_date, 41)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 41)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/12Z_9jiDJE1yMrh9Bdd1s2nnV0giZn1qv/view?usp=share_link" class="pastedDriveLink-0">w6-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/12Z_9jiDJE1yMrh9Bdd1s2nnV0giZn1qv/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 42)+"""
DTEND:"""+fix_date(init_date, 42)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 42)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/15ZvII-vUGR1KJhDnZjCO-qWEovEk-EbS/view?usp=share_link" class="pastedDriveLink-0">w6-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w6-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/15ZvII-vUGR1KJhDnZjCO-qWEovEk-EbS/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 43)+"""
DTEND:"""+fix_date(init_date, 43)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 43)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1-5THNdKwKxWgcPD6HxrTobEgcrPstJ27/view?usp=share_link" class="pastedDriveLink-0">w7-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1-5THNdKwKxWgcPD6HxrTobEgcrPstJ27/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 44)+"""
DTEND:"""+fix_date(init_date, 44)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 44)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1VDuFBvKKKOJSvOeeK5f9HASqvWehpbCa/view?usp=share_link" class="pastedDriveLink-0">w7-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/1VDuFBvKKKOJSvOeeK5f9HASqvWehpbCa/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 45)+"""
DTEND:"""+fix_date(init_date, 45)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 45)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1sTS4QAYGUZm42PdnAWbRnqzGQK0B5lhD/view?usp=share_link" class="pastedDriveLink-0">w7-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1sTS4QAYGUZm42PdnAWbRnqzGQK0B5lhD/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 46)+"""
DTEND:"""+fix_date(init_date, 46)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 46)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1_kM4p3rHwVmsoHoZTiKe0ChkgZPi0dIC/view?usp=share_link" class="pastedDriveLink-0">w7-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1_kM4p3rHwVmsoHoZTiKe0ChkgZPi0dIC/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 47)+"""
DTEND:"""+fix_date(init_date, 47)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 47)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1OVRSyCKTL5txtNiFxFQwdCZoALXf9JEF/view?usp=share_link" class="pastedDriveLink-0">w7-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1OVRSyCKTL5txtNiFxFQwdCZoALXf9JEF/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 48)+"""
DTEND:"""+fix_date(init_date, 48)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 48)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1nPp4DsbWwtbhCrrhlBE0iFGPg_1yocIj/view?usp=share_link" class="pastedDriveLink-0">w7-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1nPp4DsbWwtbhCrrhlBE0iFGPg_1yocIj/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 49)+"""
DTEND:"""+fix_date(init_date, 49)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 49)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1hEKwYMsyv-B-TUsPLS3C0AMIvnMNsKNy/view?usp=share_link" class="pastedDriveLink-0">w7-d7.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w7-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1hEKwYMsyv-B-TUsPLS3C0AMIvnMNsKNy/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 50)+"""
DTEND:"""+fix_date(init_date, 50)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 50)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1OaTfMl78K0KNerssPhax0Gk-QNCZweeE/view?usp=share_link" class="pastedDriveLink-0">w8-d1.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d1.png;FMTTYPE=image/png:https://drive.google.com/file/d/1OaTfMl78K0KNerssPhax0Gk-QNCZweeE/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 51)+"""
DTEND:"""+fix_date(init_date, 51)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 51)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/14mRpM3z2zqM-MrbRAsaAUx-0EiaAzBbD/view?usp=share_link" class="pastedDriveLink-0">w8-d2.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d2.png;FMTTYPE=image/png:https://drive.google.com/file/d/14mRpM3z2zqM-MrbRAsaAUx-0EiaAzBbD/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 52)+"""
DTEND:"""+fix_date(init_date, 52)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 52)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1Dza3GG5OSKkX5A7xz3Ep42ANMsC89G-Q/view?usp=share_link" class="pastedDriveLink-0">w8-d3.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d3.png;FMTTYPE=image/png:https://drive.google.com/file/d/1Dza3GG5OSKkX5A7xz3Ep42ANMsC89G-Q/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 53)+"""
DTEND:"""+fix_date(init_date, 53)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 53)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1RDCYxpibsGxAo-en9faxA6BRUhM7Igkz/view?usp=share_link" class="pastedDriveLink-0">w8-d4.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d4.png;FMTTYPE=image/png:https://drive.google.com/file/d/1RDCYxpibsGxAo-en9faxA6BRUhM7Igkz/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 54)+"""
DTEND:"""+fix_date(init_date, 54)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 54)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1vg07tcggLLUlow1ErcOFo96CDlKRi0cz/view?usp=share_link" class="pastedDriveLink-0">w8-d5.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d5.png;FMTTYPE=image/png:https://drive.google.com/file/d/1vg07tcggLLUlow1ErcOFo96CDlKRi0cz/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 55)+"""
DTEND:"""+fix_date(init_date, 55)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 55)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1GKPGOU8w1YQjYF2fdR98hoB1WxDPH3V7/view?usp=share_link" class="pastedDriveLink-0">w8-d6.png</a>
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d6.png;FMTTYPE=image/png:https://drive.google.com/file/d/1GKPGOU8w1YQjYF2fdR98hoB1WxDPH3V7/view?usp=share_link

END:VEVENT

BEGIN:VEVENT
DTSTART:"""+fix_date(init_date, 56)+"""
DTEND:"""+fix_date(init_date, 56)+"""
UID:7qluq7tpnapsle40btklsiloq6google.com
RECURRENCE-ID:"""+fix_date(init_date, 56)+"""
DESCRIPTION:<a href="https://drive.google.com/file/d/1omXm7L5gv7M0JblibwQg0MQBmQB7hydW/view?usp=share_link" class="pastedDriveLink-0">w8-d7.png</a><br><br>you did it.&nbsp\;<br>now move on to the next mountain to conquer.
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:HTK WOD
TRANSP:OPAQUE
ATTACH;FILENAME=w8-d7.png;FMTTYPE=image/png:https://drive.google.com/file/d/1omXm7L5gv7M0JblibwQg0MQBmQB7hydW/view?usp=share_link

END:VEVENT

END:VCALENDAR
"""
    filename = "HTK_Built_Different_GYM_Workout_Plan.ics"
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