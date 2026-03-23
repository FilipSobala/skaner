from enum import Enum

class tokeny(Enum):
    identyfikator=1
    liczba=2
    znak=3
    nawias=4
    przypisanie=5


line=""
position = 0
ch = None

def NextChar():
    global position, ch, line
    if position <len(line):
        ch = line[position]
        position += 1
    else:
        ch= None
def SkipSpaces():
    global ch
    while ch==' ':
        NextChar()

def GetToken():
    global ch
    if ch == None:
        return
    if ch.isalpha():
        token=''
        while ch is not None and ch.isalnum():
            token+=ch
            NextChar()
        print('Identyfikator: '+token)
        file2.write('<span style="color: orange;">'+token+'</span>')
    elif ch.isdigit():
        token=''
        while  ch is not None and ch.isdigit():
            token+=ch
            NextChar()
        print('Liczba: '+token)
        file2.write(token)
    else:
        match ch:
            case '+' : 
                print('Plus')
                file2.write('<b><span style="color: green;">+</span></b>')
            case '-' : 
                print('Minus')
                file2.write('<b><span style="color: green;">-</span></b>')
            case '*' : 
                print('Mnożenie')
                file2.write('<b><span style="color: green;">*</span></b>')
            case '/' : 
                print('Dzielenie')
                file2.write('<b><span style="color: green;">/</span></b>')
            case '(' : 
                print('Otwarcie_nawiasu')
                file2.write('<b><span style="color: yellow;">(</span></b>')
            case ')' : 
                print('Zamkniecie_nawiasu')
                file2.write('<b><span style="color: yellow;">)</span></b>')
            case '=' : 
                print('Przypisanie')
                file2.write('<b><span style="color: blue;">=</span></b>')
            case _:
                print('Blad: '+ch)
                file2.write('<span style="color: red;">'+ch+'</span>')
        NextChar()


if __name__ == "__main__":
    with open('wyrazenie.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('kolorowany.html', 'w', encoding='utf-8') as file2:
        file2.write('<html>\n')
        for line in lines:
            file2.write('<p>')
            position=0
            ch=None
            NextChar()
            while ch!=None:
                SkipSpaces()
                GetToken()
            print('end of line')
            file2.write('</p>\n')
        file2.write('</html>')

            