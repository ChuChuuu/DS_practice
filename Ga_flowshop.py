import numpy as np
import time
import copy

p = [10 , 10 , 13 , 4 , 9 , 4 , 8 , 15 , 7 , 1 , 9 , 3 , 15 , 9 , 11 , 6 , 5 , 14 , 18 , 3 ]
d = [50 , 38 , 49 , 12 , 20 , 105 , 73 , 45 , 6 , 64 , 15 , 6 , 92 , 43 , 78 , 21 , 15 , 50 , 150 , 99 ]
w = [10 , 5 , 1 , 5 , 10 , 1 , 5 , 10 , 5 , 1 , 5 , 10 , 10 , 5 , 1 , 10 , 5 , 5 , 1 , 5 ]


job_num = 20
population_size = 30
crossover_rate = 0.8
iteration_time = 2000
mutation_rate = 0.1
mutation_select_rate = 0.5
mutation_num = round(job_num*mutation_select_rate)

answer = 999999999999
population_list =[]

start_time = time.time()

for i in range(population_size):
	random_gene = list(np.random.permutation(job_num))
	population_list.append(random_gene)


for j in range(iteration_time):
	test_ans = 999999999999

	parent_list = copy.deepcopy(population_list)
	child_list = copy.deepcopy(population_list)
	S = list(np.random.permutation(population_size))

	for k in range(int(population_size/2)):
		crossover_probability = np.random.rand()
		if crossover_rate >= crossover_probability:
			parent_1 = population_list[S[2*k]][:] #can i use copy?
			parent_2 = population_list[S[2*k +1]][:]
			child_1  = ["na" for i in range(job_num)]
			child_2  = ["na" for i in range(job_num)]#create the child with value
			fix_num = round(job_num/2) #to decide how many job need to be fixed
			gene_fix_position = list(np.random.choice(job_num,fix_num,replace = False))

			for fix in range(fix_num):
				child_1[gene_fix_position[fix]] = parent_2[gene_fix_position[fix]]
				child_2[gene_fix_position[fix]] = parent_1[gene_fix_position[fix]]

			change_1 = [parent_1[i] for i in range(job_num) if parent_1[i] not in child_1]
			change_2 = [parent_2[i] for i in range(job_num) if parent_2[i] not in child_2] # to figure out which job need to change

			for i in range(job_num - fix_num):
				child_1[child_1.index("na")] = change_1[i]
				child_2[child_2.index("na")] = change_2[i]

			child_list[S[2*k]] = child_1[:]
			child_list[S[2*k +1]] = child_2[:]

	for k in range(len(child_list)):# can i use population_size?
		mutation_probability = np.random.rand()
		if mutation_rate >= mutation_probability:
			mutation_change_position = list(np.random.choice(job_num,mutation_num,replace=False))
			change_temp = child_list[k][mutation_change_position[0]]
			for i in range(mutation_num-1):
				child_list[k][mutation_change_position[i]] = child_list[k][mutation_change_position[i+1]]

			child_list[k][mutation_change_position[mutation_num-1]] = change_temp

#calculate fitness value
	all_chromosome = copy.deepcopy(parent_list) + copy.deepcopy(child_list)
	
	chromosome_fitness,chromosome_fit = [],[] #why???
	total_fitness=0
	for i in range(population_size*2):
		process_time = 0
		delay = 0
		for j in range(job_num):
			process_time = process_time + p[all_chromosome[i][j]]
			delay = delay + w[all_chromosome[i][j]]*max(process_time-d[all_chromosome[i][j]],0)
		chromosome_fitness.append(1/delay)
		chromosome_fit.append(delay)
		total_fitness = total_fitness + chromosome_fitness[i]

#selection
	Pk,Qk = [],[]
	for i in range(population_size*2):
		Pk.append(chromosome_fitness[i]/total_fitness)
	for i in range(population_size*2):#i think there are another writing style
		cumulative = 0
		for j in range(i+1):
			cumulative = cumulative + Pk[j]
		Qk.append(cumulative)

	selection_random = [np.random.rand() for i in range(population_size)]

	for i in range(population_size):
		if selection_random[i] < Qk[0]:
			population_list[i] = copy.deepcopy(all_chromosome[0])
		else:
			for j in range(population_size*2 -1):
				if selection_random[i] > Qk[j] and selection_random[i] <= Qk[i+1]:
					population_list[i] = copy.deepcopy(all_chromosome[i+1])
					break
#comparison
	for i in range(population_size*2):
		if chromosome_fit[i] < test_ans:
			test_ans = chromosome_fit[i]
			sequence_now = copy.deepcopy(all_chromosome[i])
	if test_ans <= answer:#why here is <=?
		answer = test_ans
		sequence_best = copy.deepcopy(sequence_now)

	job_sequence_ptime = 0
	delay_num = 0
	for i in range(job_num):
		job_sequence_ptime = job_sequence_ptime + p[sequence_best[i]]
		if job_sequence_ptime > d[sequence_best[i]]:
			delay_num = delay_num+1

print("optimal sequence ", sequence_best)
print("optimal value :{}".format(answer))
print("aberage delay : {}".format(answer / job_num))
print("number of delay: {}".format(delay_num))
print("run time : {}".format(time.time()-start_time))
