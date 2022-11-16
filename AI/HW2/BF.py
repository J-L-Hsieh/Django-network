class Problem :
    def __init__(self):
        self.input = input
        self.numTasks = len(input)

    def cost(self,ans):
        totalTime = 0
        for task, agent in enumerate(ans):
            totalTime += self.input[task][agent]
        return totalTime

input =[
    [0.43045255, 0.78681387, 0.07514408, 0.72583933, 0.52916145, 0.87483212, 0.34701621],
    [0.68704291, 0.45392742, 0.46862110, 0.67669006, 0.23817468, 0.87520581, 0.67311418],
    [0.38505150, 0.05974168, 0.11388629, 0.28978058, 0.66089373, 0.92592403, 0.70718757],
    [0.24975701, 0.16937649, 0.42003672, 0.88231235, 0.74635725, 0.59854858, 0.88631100],
    [0.64895582, 0.58909596, 0.99772334, 0.85522575, 0.33916707, 0.72873479, 0.26826203],
    [0.47939038, 0.88484586, 0.05122520, 0.83527995, 0.37219939, 0.20375257, 0.50482283],
    [0.58926554, 0.45176739, 0.25217475, 0.83548120, 0.41687026, 0.00293049, 0.23939052]
]

# 取出input總長
length = []
for i in range(len(input)):
    length.append(i)
# 進行排列組合,每一row中該取的欄位
def picker(length):
    if len(length) ==1:
        return[length]
    result = []
    for i in range(len(length)):
        remain = length[:i]+length[i+1:]
        remain_list = picker(remain)
        num = []
        for j in remain_list:
            num.append(length[i:i+1]+j)
        result += num
    return result
number = picker(length)
print(len(number))
# 將row中對應欄位之值取出相加,選出最小者
for i in number:
    sum = float(0)
    for j in i:
        sum += float(input[i.index(j)][j])
    if number.index(i) == 0 :
        min_sum = sum
        result = i
    elif min_sum > sum:
        min_sum = sum
        result = i

yourAssignment =result

solver = Problem()
print('Assignment : ' , yourAssignment )
print('Cost : ', solver.cost(result))

