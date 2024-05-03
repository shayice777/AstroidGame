# צבעי הטקסט
list_sen = []
input_count = int(input("How many sentences would you like?"))
for i in range(input_count):
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
        input_color = eval(input("input the color of the text:"))


    input_text = input("input your text:")

    list_sen.append(Colors.input_color + input_text)


for i in range(len(list_sen)):
    print(list_sen[i])