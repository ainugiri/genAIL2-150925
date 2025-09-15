DL
Deep Learning
Special form of Machine Learning
Learns from BIG DATA

Complex, high data -> learning -> DL model
Uses Neural Networks

Network of Neurons - mimics human brain
dots- node - neuron
lines - connection - synapse - carry weight


3 layers:
1. Input Layer - input data
2. Hidden Layer - multiple layers - process data - learn patterns
3. Output Layer - output prediction

input layer -> input data -> age, noowners, mileage, initialprice, make, model, fuel, transmission

wrt value, move from one node -> another node
while moving, weight is applied
inside the node, activation function -> mathematical operation -> decide to pass or not


output layer -> collate all the values from hidden layer -> final output
w.r.t value, decide the output
if 19924 ->  20000 -> classA
if 15000 ->  15000 -> classB
if 10000 ->  10000 -> classC



Feed Forward Neural Network
    data move in one direction - input to output
    no loop, no cycle

While training:
    forward pass - input to output
    backward pass - calculate error, adjust weights

input
1.5,
2.5,

17.5
16.7

actual output 200

from feed forward, calcaulate final value as 170
actual value 2--
error is 30
BACKWARD PROPAGE 
    FINE TUNE THE WEIGHTS, SO THAT 

