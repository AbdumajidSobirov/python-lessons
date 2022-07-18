son = int(input("ixtiyoriy sonni kiriting: \n >>>"))
for x  in range(9):
    if son%(x+2) == 0:
        print(f"{son} soni {x+2} ga qoldiqsiz o'linadi")