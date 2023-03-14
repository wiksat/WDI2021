# def move(n, fro, to, use):
#     if n == 1:
#         # print(fro, "->", use)
#         print(fro, "->", to)
#         # print(use, "->", to)
#     else:
#         move(n-1, fro, use, to)
#         print(fro, "->", to)
#         move(n-1, use, to, fro)
#
#
# move(3, "A", "B", "C")

#chcemy przenieść z A na B przez C

def przenies (ile, skad, dokad, przez):
    print("nowa")
    if ile > 0:
        #A C B
      przenies (ile-1, skad, przez, dokad)
      print (skad, "->", dokad)
        #C B A
      przenies (ile-1, przez, dokad, skad)

przenies (3, "A", "B", "C")