import math


class Node:
    def __init__(self, id, x, y):
        self.x = float(x)
        self.y = float(y)
        self.id = int(id)



file_name = "city_coordinate.txt"
dataset = []


with open(file_name, "r") as f:
    for line in f:
        new_line = line.strip()
        new_line = new_line.split(" ")
        id, x, y = new_line[0], new_line[1], new_line[2]
        dataset.append(Node(id=id, x=x, y=y))

N = 20



def create_distance_matrix(node_list):
    matrix = [[0 for _ in range(N)] for _ in range(N)]


    for i in range(0, len(matrix)-1):
        for j in range(0, len(matrix[0])-1):

            matrix[node_list[i].id][node_list[j].id] = math.sqrt(
                pow((node_list[i].x - node_list[j].x), 2) + pow((node_list[i].y - node_list[j].y), 2)
            )
    return matrix


matrix = create_distance_matrix(dataset)



class Chromosome:
    def __init__(self, node_list):
        self.chromosome = node_list

        Chromosome_representation = []
        for i in range(0, len(node_list)):
            Chromosome_representation.append(self.chromosome[i].id)
        self.chr_representation = Chromosome_representation

        distance = 0
        for j in range(1, len(self.chr_representation) - 1):
            distance += matrix[self.chr_representation[j]-1][self.chr_representation[j + 1]-1]
        self.cost = distance

        self.fitness_value = 1 / self.cost






