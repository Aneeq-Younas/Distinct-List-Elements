def elent (n):

    final = [[ ]]
    for i in n:

        new_final = []
        for x in final:

            for b in range (len(x)+1 ):
                new_final.append(x [:b] + [i] + x[b: ])
                final = new_final
    return final

lst = [5,6,7,8,9]

print("The original numbers of list: \n ", lst)
print("The distinct numbers of list: \n ", elent(lst))
