import prompt, predicate
from random import random as gen_preference
from listlib import rank,print_histogram
import random


def hire_exceed(alist,float):
    for i in range(0,len(alist)):
        if alist[i] > float:
            return alist[i]
    else:
        return alist[-1] 

def do_one_experiment(total,preint):
    goodness = random.sample(range(1000), 100) 
    maxgoodpreint = max(goodness[0:preint+1])
    hired = hire_exceed(goodness[preint:],maxgoodpreint)
    return rank(hired,goodness)

def do_many_experiments(total,preint,exp):
    hist=[0]*(total+1)
    trials=0
    while True:           
        if trials == exp:
            break 
        trials +=1
        x=do_one_experiment(total,preint)
        hist[x] += 1          
    return hist

def good_percent(histogram,p):
    sum = 0
    total = 0
    for i in range(len(histogram)):
        if p(i):
            sum += histogram[i]
        total += histogram[i]
    return sum/total


total = prompt.for_int('Enter number of candidates in interview(>= 10)',default=100,is_legal=(lambda x : x >= 10))
preint = prompt.for_int('Enter number of candidates to pre-interview(>=1, <100)',default=20,is_legal=(lambda x: x>=1 and x<100))
experiments = prompt.for_int('Enter number of experiments to simulate',default=1000)
bins = do_many_experiments(total,preint,experiments)
print('Histogram for one set of experiments')
print_histogram('Rank  Hire%',bins)
lamb = prompt.for_string('Enter lambda to define good',default = 'lambda x : x <= 3')
goodperc = good_percent(bins,eval(lamb))
print('goodness for above histogram =','{:.1%}'.format(goodperc))
print('Results for many experiments, one set for each different pre-interview number')
print('PreI  good%')
for i in range(1,100):
    exper = do_many_experiments(total,i,experiments)
    goodpercent = good_percent(exper,eval(lamb))
    print(i,'[','{:.1%}'.format(goodpercent),']|','*'*int(goodpercent*100))
     
