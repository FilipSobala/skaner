from enum import Enum,auto

class Token(Enum):
    t_identyfikator = auto()
    t_liczba=auto()
    t_plus=auto()
    t_minus=auto()
    t_mnozenie=auto()
    t_dzielenie=auto()
    t_otwarcie=auto()
    t_zamkniecie=auto()
    t_przypisanie=auto()

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
    elif ch.isdigit():
        token=''
        while  ch is not None and ch.isdigit():
            token+=ch
            NextChar()
        print('Liczba: '+token)
    else:
        match ch:
            case '+' : 
                print('Plus')
            case '-' : 
                print('Minus')
            case '*' : 
                print('Mnożenie')
            case '/' : 
                print('Dzielenie')
            case '(' : 
                print('Otwarcie_nawiasu')
            case ')' : 
                print('Zamkniecie_nawiasu')
            case '=' : 
                print('Przypisanie')
            case _:
                print('Blad: '+ch)
        NextChar()

if __name__ == "__main__":
    with open('wyrazenie.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        position=0
        ch=None
        NextChar()
        while ch!=None:
            SkipSpaces()
            GetToken()
        print('end of line')

            