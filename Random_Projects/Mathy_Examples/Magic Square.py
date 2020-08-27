x = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    for f in range(1, 10):
                        for g in range(1, 10):
                            for h in range(1, 10):
                                for i in range(1, 10):
                                    Row1 = a + b + c
                                    Row2 = d + e + f
                                    Row3 = g + h + i
                                    Col1 = a + d + g
                                    Col2 = b + e + h
                                    Col3 = c + f + i
                                    Dia1 = a + e + i
                                    Dia2 = g + e + c

                                    if Row1 == Row2 == Row3 == Col1 == Col2 == Col3 == Dia1 == Dia2 and a + b + c + d + e + f + g + h + i == 45:
                                        if a != b and a != c and a != d and a != e and a !=f and a != g and a != h and a != i:
                                            if b != c and b != d and b != e and b != f and b != g and b != h and b != i:
                                                if c != d and c != e and c != f and c != g and c != h and c != i:
                                                    if d != e and d != f and d != g and d != h and d != i:
                                                        if e != f and e != g and e != h and e != i:
                                                            if f != g and f != h and f != i:
                                                                if g != h and g != i:
                                                                    if h != i:
                                                                        x += 1
                                                                        print ("this is the " + str(x) + " solution")
                                                                        print (a, b, c)
                                                                        print (d, e, f)
                                                                        print (g, h, i)


print ("Magic Square Finished")
