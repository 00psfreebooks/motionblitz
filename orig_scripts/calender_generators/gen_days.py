# read line from a file

new_file = "./days.txt"

start_day = 0
finish_day = 364

finish_day += 1


with open(new_file, "w") as f:
    for inc_num in range(start_day, finish_day):
        week_num = inc_num // 7 + 1
        
        day_of_week_num = inc_num % 7 + 1
        
        spec_string = "w" + str(week_num) + "-d" + str(day_of_week_num)
        str_rep = "\nBEGIN:VEVENT\nDTSTART;TZID=America/Anchorage:\"\"\"+fix_date(init_date, " + str(inc_num) + ")+\"\"\"\nDTEND;TZID=America/Anchorage:\"\"\"+fix_date(init_date, " + str(inc_num) + ")+\"\"\"\nUID:7qluq7tpnapsle40btklsiloq6google.com\nRECURRENCE-ID;TZID=America/Anchorage:\"\"\"+fix_date(init_date, " + str(inc_num) + ")+\"\"\"\nDESCRIPTION:<a href=\"\" class=\"pastedDriveLink-0\">"+ spec_string +".png</a>\nLOCATION:\nSEQUENCE:0\nSTATUS:CONFIRMED\nSUMMARY:HTK WOD\nTRANSP:OPAQUE\nATTACH;FILENAME="+ spec_string +".png;FMTTYPE=image/png:\nEND:VEVENT\n"
        f.write(str_rep)