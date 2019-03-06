import numpy as np
import time
import copy

p = [10 , 10 , 13 , 4 , 9 , 4 , 8 , 15 , 7 , 1 , 9 , 3 , 15 , 9 , 11 , 6 , 5 , 14 , 18 , 3 ]
d = [50 , 38 , 49 , 12 , 20 , 105 , 73 , 45 , 6 , 64 , 15 , 6 , 92 , 43 , 78 , 21 , 15 , 50 , 150 , 99 ]
w = [10 , 5 , 1 , 5 , 10 , 1 , 5 , 10 , 5 , 1 , 5 , 10 , 10 , 5 , 1 , 10 , 5 , 5 , 1 , 5 ]


job_num = 20
population_size = 30
crossover_rate = 0.8
iteration_time = 1000

answer = 999999999999

for i in range(population_size):
	random_gene = list(np.random.permutation(job_num))
	population_list.append(random_gene)


for j in range(iteration_time):
	test_ans = 999999999999

	parent_list = copy.deepcopy(population_list)
	child_list = copy.deepcopy(population_list)
	S = list(np.random.permutation(population_size)

	for k in range(int(population_size/2)):
		crossover_probability = np.random.rand()
		if crossover_rate >= crossover_probability:
			parent_1 = population_list[S[2*k]][:] #can i use copy?
			parent_2 = population_list[S[2*k +1]][:]
			child_1  = ["na" for i in range(job_num)]
			child_2  = ["na" for i in range(job_num)]#create the child with value

