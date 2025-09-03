operations_list = []

def train(n, q):
    for operation in operations_list:
        letter = operation[0]
        range_ = operation[1]
        
        if letter == "A":
            charge = operation[2]
            for i in range(int(range_)):
                train_list[i] = int(charge)
                print(train_list)

        if letter == "C":
            vagon = int(operation[1])
            print(train_list[vagon - 1])
    

n = int(input())
q = int(input())

train_list = [0] * n

for i in range(q):
    operation = input().split()
    operations_list.append(operation)


train(n, q)

