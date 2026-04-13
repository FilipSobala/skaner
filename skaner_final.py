from enum import Enum

class Tokeny(Enum):
    IDENTYFIKATOR = 1
    LICZBA = 2
    OPERATOR = 3
    NAWIAS = 4
    PRZYPISANIE = 5
    SLOWO_KLUCZOWE = 6
    SREDNIK = 7

KEYWORDS = {"if", "else", "while", "int", "print", "double", "string"}

line = ""
position = 0
ch = None

def NextChar():
    global position, ch, line
    if position < len(line):
        ch = line[position]
        position += 1
    else:
        ch = None


def GetToken():
    global ch

    if ch is None:
        return

    if ch.isalpha():
        token = ''
        while ch is not None and ch.isalnum():
            token += ch
            NextChar()

        if token in KEYWORDS:
            print("Slowo kluczowe: ", token)
            file2.write(f'<b><span style="color: blue;">{token}</span></b>')
        else:
            print("Identyfikator: ", token)
            file2.write(f'<span style="color: orange;">{token}</span>')

    elif ch.isdigit():
        token = ''
        is_double = False
        while ch is not None and (ch.isdigit() or ch == '.'):
            if ch == '.':
                if is_double:
                    break
                is_double = True
            token += ch
            NextChar()

        if is_double:
            print("Liczba:", token)
            file2.write(f'<span style="color: cyan;">{token}</span>')
        else:
            print("Liczba:", token)
            file2.write(f'<span style="color: cyan;">{token}</span>')

    else:
        match ch:
            case '=':
                NextChar()
                if ch == '=':
                    NextChar()
                    print("Rownosc : ==")
                    file2.write('<b style="color: blue;">==</b>')
                else:
                    print("Przypisanie : =")
                    file2.write('<b style="color: blue;">=</b>')

            case '!':
                NextChar()
                if ch == '=':
                    NextChar()
                    print("Nierownosc: !=")
                    file2.write('<b style="color: black;">!=</b>')

            case '+':
                print("Dodawanie: ", ch)
                file2.write(f'<b style="color: black;">{ch}</b>')
                NextChar()
            case '-':
                print("Odejmowanie: ", ch)
                file2.write(f'<b style="color: black;">{ch}</b>')
                NextChar()
            case '*':
                print("Mnożenie: ", ch)
                file2.write(f'<b style="color: black;">{ch}</b>')
                NextChar()
            case '/':
                NextChar()
                if ch == '/':
                    comment = ''
                    NextChar()

                    while ch is not None and ch != '\n':
                        comment += ch
                        NextChar()

                    print("Komentarz:", comment)
                    file2.write(f'<span style="color: green;">//{comment}</span>')
                else:
                    print("Dzielenie: ", ch)
                    file2.write(f'<b style="color: black;">/</b>')
            case'<':
                print("mniejsze_wieksze: ", ch)
                file2.write(f'<b style="color: black;">{ch}</b>')
                NextChar()
            case '>':
                print("wieksze_mniejsze: ", ch)
                file2.write(f'<b style="color: black;">{ch}</b>')
                NextChar()

            case '(':
                print("Nawias_otwarcia: ", ch)
                file2.write(f'<b style="color: black;">{ch}</b>')
                NextChar()
            case ')':
                print("Nawias_zamkniecie: ", ch)
                file2.write(f'<b style="color: black;">{ch}</b>')
                NextChar()
            case '{':
                print("Klamra_otwarcie: ", ch)
                file2.write(f'<b style="color: black;">{ch}</b>')
                NextChar()
            case '}':
                print("Klamra_zamkniecie: ", ch)
                file2.write(f'<b style="color: black;">{ch}</b>')
                NextChar()
            case '[':
                print("Kwadratowy_otwarcie: ", ch)
                file2.write(f'<b style="color: black;">{ch}</b>')
                NextChar()
            case ']':
                print("Kwadratowy_zamkniecie: ", ch)
                file2.write(f'<b style="color: black;">{ch}</b>')
                NextChar()
            case ']':
                print("kropka: ", ch)
                file2.write(f'<b style="color: black;">{ch}</b>')
                NextChar()

            case ';':
                print("Średnik")
                file2.write('<b style="color: black;">;</b>')
                NextChar()
            case '.':
                print("Kropka")
                file2.write('<b style="color: black;">.</b>')
                NextChar()
            case '\n':
                file2.write('<br>')
                NextChar()
            case '\t':
                file2.write('\t')
                NextChar()
            case ' ':
                file2.write(' ')
                NextChar()
            case '"':
                string = ''
                NextChar()

                while ch is not None and ch != '"':
                    string += ch
                    NextChar()

                NextChar()

                print("String:", string)
                file2.write(f'<span style="color: red;">"{string}"</span>')
            case _:
                print("Blad:", ch)
                file2.write(f'<span style="color: red;">{ch}</span>')
                NextChar()


if __name__ == "__main__":
    with open('wyrazenie.txt', 'r', encoding='utf-8') as file:
        line = file.read()

    with open('kolorowany.html', 'w', encoding='utf-8') as file2:
        file2.write('<html>\n')
        file2.write('<pre>\n')

        position = 0
        ch = None

        NextChar()

        while ch is not None:
            GetToken()

        file2.write('\n</pre>')
        file2.write('\n</html>')