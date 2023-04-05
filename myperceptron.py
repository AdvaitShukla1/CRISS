import math
x_input=[0.1,0.5,0.2]
w_weights=[0.3,0.4,0.6]
threshold=0.5
def step(weighted_sum):
    if weighted_sum > threshold:
        return 1
    else:
        return 0
def perceptron():
    weighted_sum=0
    for x,w in zip(x_input,w_weights):
        weighted_sum+=x*w
    return step(weighted_sum)
output=perceptron()
print("Output:"+str(output))
input_data=[(0.26,1),(0.2,0),(0.48,1),(0.3,0)]
def cross_entropy(input_data):
    loss=0
    n=len(input_data)
    for entry in input_data:
        w_sum=entry[0]
        y=entry[1]
        loss+=-(y*math.log10(w_sum)+(1-y)*math.log10(1-w_sum))
        return(loss/n)
