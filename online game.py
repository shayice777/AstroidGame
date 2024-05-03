import random
import turtle
class Colors:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    RESET = '\033[39m'

players_names_list = []
random_names_list = ['eleven','mosha','sigalit','*#24$26',"shoko","margarita","yafa_blond","mikmak","simha"]
the_chosen_names_list = []
q_list = ["מי יש סיכוי גדול יותר לשכוח תאריכי יום הולדת ?" ,"מי יותר מצחיק ?" ,"מי יותר טוב בריקוד ?" , "מי שר יותר טוב ? " , "מי הדרמה קווין הכי גדולה ?" , "מי בדרך כלל מבזבז כסף על דברים שהוא לא צריך ?" ,  "מי בדרך כלל לוקח שליטה במצבים קשים ?" ,  "מי יותר משגע את ההורים שלה ?" , "למי יש יותר סיכוי לשרוד במתקפת זומבים ?" , "מי הכי מושך ?" , "מי יותר אוהב לאכול באוטו ?" ,"מי יותר מוזר או משוגע ?" ,"מי הכי פחדן ?"  ,"למי יש יותר סיכוי לעשות ניתוח פלסטי ?" , "למי יש יותר סיכוי לא להתקלח במשך שבוע ?"  , "למי יש יותר סיכוי להתחתן בגלל הכסף ?" ,  "למי יש יותר סיכוי להרוויח מיליון דולר ?" , " מי הכי משכנע ?" ,  "מי הכי עקשנן ?" ,  "מי הכי חברותי ? " , "מי יתחתן ראשון?" , "מי הכי נדיב ?" ,  "מי בעל דימוי עצמי גבוה ?"  , "מי הכי עצלן ?"  , "מי מתלבש הכי יפה ?" , "מי הכי ספונטני ? " ,"מי יותר אוהב חיות ?" , "למי יש יותר סיכוי להיאבד בחול ?" , "למי יש יותר סיכוי לברוח מהבית ?",  "למי יש יותר סיכוי לגור בחול ?"]



for i in range(3):
    x2 = random.choice(random_names_list)
    the_chosen_names_list.append(x2)
    random_names_list.remove(x2)
# guests
def guest(cyan,green,red,yellow):
    x = random.choice(q_list)
    print(yellow+players_names_list[0]+":",cyan+the_chosen_names_list[0],yellow+players_names_list[1]+":",green+the_chosen_names_list[1],yellow+players_names_list[2]+":",red+the_chosen_names_list[2])

    t = -1
    while t < 0:
        ans = input(yellow+x)
        if ans == the_chosen_names_list[0]:
            q_list.remove(x)
            return ans+":"+x
            t = 1
        elif ans == the_chosen_names_list[1]:
            q_list.remove(x)
            return ans + ":" + x
            t = 1
        elif ans == the_chosen_names_list[2]:
            q_list.remove(x)
            return ans + ":" + x
            t = 1



# player
for i in range(3):
    players_names_list.append(input("input your name: "))

def player(guest_function):
   hint_for_who = str(guest_function)
   hint_for_who = hint_for_who[0:-2]
   print(hint_for_who)
   guess_who_you_are = input("who are you:")

#Both
for i in range(len(q_list)):
    guest_function = guest(Colors.cyan,Colors.green,Colors.red,Colors.yellow)
    player(guest_function)



print(q_list)
