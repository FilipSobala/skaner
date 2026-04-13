# skaner
Teoria kompilacji i kompilatory/skaner
| Nazwa tokenu     | Wzór (regex)                 | Opis |
|------------------|-----------------------------|------|
| IDENTYFIKATOR    | `[a-zA-Z_][a-zA-Z0-9_]*`    | Nazwy zmiennych i funkcji |
| LICZBA           | `\d+(\.\d+)?`              | Liczby całkowite i zmiennoprzecinkowe |
| STRING           | `".*?"`                    | Tekst w cudzysłowie |
| SLOWO_KLUCZOWE   | \b(if|else|while|int|double|string|print)\b | Słowa języka |
| OPERATOR         | \b(\+|\-|\*|\/|<|>|==|!=)\b  | Operatory arytmetyczne i logiczne |
| PRZYPISANIE      | `=`                         | Przypisanie wartości |
| NAWIAS           | \b(\(|\)|\{|\}|\[|\])\b        | Nawiasy |
| SREDNIK          | `;`                         | Koniec instrukcji |
| KOMENTARZ        | `//*`                      | Komentarz jednoliniowy |
