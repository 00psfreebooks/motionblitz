import os

links_file = "links/tac-monst.txt"

gen_file="./newgen.py"

template_file = "./templates/8_week_template.py"

# make a copy of the template file
with open(template_file, "r") as f:
    template = f.readlines()

# if file does not exist, create it
if os.path.exists(gen_file):
    os.remove(gen_file)

with open(gen_file, "a") as f:
    f.writelines(template)


# how to remove content between substrings (to include removing the substrings) in a file
# sed -i 's/\bhttps\b.*\bsharing\b//' file.txt

# insert links in new template file
newlines = []

with open(links_file, "r") as f:
    links = f.readlines()
    
with open(gen_file, "r") as f:
    lines = f.readlines()

    i = 0
    for line in lines:
        a = False
        b = False
        
        if "href" in line:
            replace = ("href=\"" + links[i] + "\"").replace("\n", "")
            line = line.replace("href=\"\"", replace)
            a = True
        elif "FMTTYPE" in line:
            line = line.replace("FMTTYPE=image/png:", "FMTTYPE=image/png:" + links[i])
            
            # we know that this statement will always come after the href statement
            # so we can get away with increasing the index here without any fancy logic
            i += 1

        newlines.append(line)


# write newlines to file
with open(gen_file, "w") as f:
    f.writelines(newlines)
