
stack = ["$", "S"]
M = [["S->CK", "S->CK", "S->fK", "S->CK", ""],
     ["K->aACK", "", "", "", "K->"],
     ["A->aP", "A->cfCP", "", "", ""],
     ["P->aP", "", "", "P->w", ""],
     ["C->aC", "C->cC", "", "C->w", ""]]
VN = ["S", "K", "A", "P", "C"]
X = "S"
VT = ["a", "c", "f", "w", "$"]
w = "fwcfcfawwc"+"$"
InSym = w[0]
k = 1
# w = "S->CK->aCk->acCk->acwK->acwaACK->acwaaPCK->acwaawCK->acwaawwK->acwaaww" "acwaaww"+"$"
# w = "S->fK->faACK->faACaACK->faACaAC->facfCPCaAC->facfwPCaAC->facfwwCaAC->facfwwwaAC->facfwwwaaPC->facfwwwaawC->facfwwwaaww" "facfwwwaaww"+"$"
# w = "S->fK->faACK->faaPCK->faawCK->faawcCK->faawccCK->faawccwK->faawccw" "faawccw"+"$"
# w = "fwcfcfawwc" "fwcfcfawwc"+"$"


def X_check(X, VN):
    cheked = False
    for i in VN:
        if X == i:
            cheked = True
    return cheked


try:
    while X != "$":
        var = True
        if not (X_check(X, VN) or X == "$"):
            if X == InSym:
                stack.pop()
                InSym = w[k]
                k += 1

            else:
                print("Программа сломалась в точке 1, Слово не принадлежит языку")
        else:
            if M[VN.index(X)][VT.index(InSym)] != "":
                stack.pop()
                var2 = M[VN.index(X)][VT.index(InSym)][::-1]
                for i in var2:
                    if i != ">" and var:
                        stack.append(i)
                    else:
                        var = False
                print(M[VN.index(X)][VT.index(InSym)])
            else:
                print("Программа сломалась в точке 2, Слово не принадлежит языку")
        X = stack[len(stack) - 1]
    print("Слово принадлежит языку")
except:
    pass




