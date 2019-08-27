# The following lists of children should be iterated, and the names sent to the
# appropriate functions.
running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

def run(child_name):
    print(f"{child}, ran like a chicken!")
for child in running_kids:
    run(child)

def swing(child_name):
    print(f"{child}, swang really high!")
for child in swinging_kids:
    swing(child)

def slide(child_name):
    print(f"{child}, slide into first base!")
for child in sliding_kids:
    slide(child)

def hide_and_seek(child_name):
    print(f"{child}, played hide and seek like a hawk!")
for child in hiding_kids:
    hide_and_seek(child)

