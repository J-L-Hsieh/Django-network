from audioop import reverse
import random
import re

class GA:
    def __init__(self,input):
        self.input = input
        self.length = len(input)


    def cost(self, ans):
        totalTime = 0
        for task, agent in enumerate(ans):
            totalTime += self.input[task][agent]
        return totalTime


    def gene_algorithma(self):
        count = 0
        parent = self.mk_parent()
        # print(len(parent))
        cost_value = self.fitness(parent,len(parent))
        parent_sort,cost_sort = self.dict_number_cost(parent,cost_value)
        min_cost = cost_sort[0]
        parent_original = parent_sort[:20]
        while count < 50:
            children = self.crossover(parent_original)
            next_parent = [*parent_original,*children]
            cost_value = self.fitness(next_parent,len(next_parent))
            parent_sort,cost_sort = self.dict_number_cost(next_parent,cost_value)
            parent_original = parent_sort[:20]
            min_assignment = parent_sort[0]
            if cost_sort[0] < min_cost :
                min_cost = cost_sort[0]
                count = 0
            else:
                count +=1
            print('min_assignment:',min_assignment,'min_cost:',min_cost)
            print('------------------------------------------')
        return(min_assignment,min_cost)

    def mk_parent(self):
        parent = []
        count = []
        for i in range(self.length):
            count.append(i)
        for i in range(0,500):
            random.shuffle(count)
            parent.append(count.copy())
        return parent


    def fitness(self,parent,parent_length):
        cost_value = []
        fitness = []
        parent_list = []
        for i,parent in enumerate(parent[:parent_length]):
            cost_value.append(self.cost(parent))
        # print('-------------------------------------')
        min_cost_value = min(cost_value)
        max_cost_value = max(cost_value)
        range_cost_value = max_cost_value - min_cost_value
        # print(range_cost_value)

        for i,cost in enumerate(cost_value):
            fitness.append((max(float(3/10*range_cost_value),pow(10,-5)))+float(max_cost_value - cost))
        return cost_value

    def dict_number_cost(self,parent,cost):
        cost_sort,parent_sort = zip(*sorted(zip(cost,parent)))
        return (parent_sort,cost_sort)

    def crossover(self,parent_original):
        length_list = []
        change_num = round(self.length/4)
        for i in range(self.length):
            length_list.append(i)
        # print(length_list)
        children = []
        mutation = []

        for i in range(0,len(parent_original),2):
            children_even = [*parent_original[i][:change_num],*parent_original[i+1][change_num:-change_num],*parent_original[i][-change_num:]]
            children_odd = [*parent_original[i+1][:change_num],*parent_original[i][change_num:-change_num],*parent_original[i+1][-change_num:]]
            children.append(children_even)
            children.append(children_odd)
            loss_odd = []
            loss_even = []
            for j in length_list:
                if j not in children_even:
                    loss_even.append(j)
                if j not in children_odd:
                    loss_odd.append(j)
            position_even = list(map(lambda x : parent_original[i+1].index(x),loss_even))
            position_odd = list(map(lambda x : parent_original[i].index(x),loss_odd))
            for k in range(len(loss_even)):
                children_even[position_odd[k]] = loss_even[k]
                children_odd[position_even[k]] = loss_odd[k]
        # for i in range(len(children)):
            # mutation.append(list(reversed(children[i])))
        # print(mutation)
        return children
if __name__ == '__main__':
    '''
    input = [
    [10, 20, 23, 4],
    [15, 13, 6, 25],
    [ 2, 22, 35, 34],
    [12, 3, 14, 17]
    ]
    '''
    input =[
    [0.43045255, 0.78681387, 0.07514408, 0.72583933, 0.52916145, 0.87483212, 0.34701621],
    [0.68704291, 0.45392742, 0.46862110, 0.67669006, 0.23817468, 0.87520581, 0.67311418],
    [0.38505150, 0.05974168, 0.11388629, 0.28978058, 0.66089373, 0.92592403, 0.70718757],
    [0.24975701, 0.16937649, 0.42003672, 0.88231235, 0.74635725, 0.59854858, 0.88631100],
    [0.64895582, 0.58909596, 0.99772334, 0.85522575, 0.33916707, 0.72873479, 0.26826203],
    [0.47939038, 0.88484586, 0.05122520, 0.83527995, 0.37219939, 0.20375257, 0.50482283],
    [0.58926554, 0.45176739, 0.25217475, 0.83548120, 0.41687026, 0.00293049, 0.23939052]
    ]

    ga = GA(input)
    parent = ga.gene_algorithma()
