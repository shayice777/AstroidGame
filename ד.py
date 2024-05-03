import turtle

# רשימת האותיות בעברית
abc_list = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ל', 'מ', 'נ', 'ס', 'ע', 'פ', 'צ', 'ק', 'ר', 'ש', 'ת']

# פונקציה שמדפיסה את האות על המסך
def print_letter(letter):
    turtle.write(letter, font=("Arial", 16, "normal"))

# רשום פונקציה עבור כל אות ב-ABC
for letter in abc_list:
    turtle.onkeypress(lambda l=letter: print_letter(l), letter.lower())

# התחל את האזכור לאירועים
turtle.listen()

# שאר הקוד
turtle.mainloop()
