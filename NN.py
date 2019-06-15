def activation(n):
    # step function
    # activation(0.5) return 1
    # activation(-1.5) return 0
    if n > 0:
        return 1
    return 0

# w1, w2, w3 = 1, 1, -1.5 # a solution of AND operation
#w1, w2, w3 = 10, 10, -7 # a solution of OR operation
#w1, w2, w3 = 1, 1, -0.2 # a solution of XOR operation
w1, w2, w3 = 
data_points = [(0,0),(0,1),(1,0),(1,1)]
for x in data_points:
    sum_of_input = w1 * x[0] + w2 * x[1] + w3 * 1
    y = activation(sum_of_input)
    print(x, y)
    
##print(activation(0.5))
##print(activation(-1.5))
