# Zadanie 8. Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
# z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k]. Napisać funkcję
# sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.

t=[6,5,2,3,10,9,5,3,4]
t_bool=[False for _ in t]
t_bool[0]=True
for i in range(len(t)):
    if t_bool[i]:
        j=2
        while j<len(t):
            if i+j<len(t):
                if t[i]%j==0:
