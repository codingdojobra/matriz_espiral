def constroi_matriz(linhas, colunas):
    itens = linhas * colunas
    i = 0
    k = 0
    matriz = [[NotImplemented for _ in range(colunas)] for _ in range(linhas)]
    numero = 1

    while itens > 0:
        matriz[i][k] = numero
        itens -= 1
        numero += 1

        if i == linhas-1:
            if k > 0:
                k -= 1

        if k == colunas-1:
            if i < linhas-1:
                i += 1

        if k < colunas-1:
            k += 1

        if k == 0:
            if i > 0:
                i -= 1

        print('i: ', i)
        print('K: ', k)

    return matriz
