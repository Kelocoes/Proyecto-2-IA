#
"""#Para mostra los tableros de los nodos
for i in range(len(minMax)):
    print("PROFUNDIDAD " + str(i) + " " + str(len(minMax[i])))
    for j in range(len(minMax[i])):
        nodo = minMax[i][j]
        print(np.array(nodo[0]))
"""

"""#Para mostrar los valores minimax de los nodos 
    for i in range(len(minMax)):
        print()
        for j in range(len(minMax[i])):
            nodo = minMax[i][j]
            print(nodo[2], end = ' ')    
"""


"""
for i in range(len(minMax)):
        print()
        #print("PROFUNDIDAD " + str(i) + " " + str(len(minMax[i])))
        for j in range(len(minMax[i])):
            nodo = minMax[i][j]
            if len(nodo[7]) != 0:
                print("padre: ",j,"hijos: ",nodo[7][0],nodo[7][1], end = ' ')
"""
