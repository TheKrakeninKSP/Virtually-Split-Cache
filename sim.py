import random
from matplotlib import pyplot as plt

#aim is to illustrate and simulate the difference in performance between a 
#standard Split L1 cache system and a Virtual Split Cache system
#64 kb is the standard amount of L1 cache allotted per processor core
#32 kb for instructions and 32 kb for data

#for a tighly looped program, the same small set of instructions would be repeated
#that is, amount of data acessed >> amount of instructions acccessed

#we define a instruction-data balance factor to express this:
balance_factor=0.05 #5% of requests are for instructions and remaining for data
balance_factor_list=[]
for i in range(10):
    balance_factor_list.append(random.randint(5,30)/100)
print("List of balance factors for the programs: ",balance_factor_list)

#number of total instructions per program
num_ins=1e10

#assuming CPU speed to be 1Ghz (ie 1 Billion cycles per second)
cpu_speed=10e9

def simulate(miss_penalty, balance_factor_list, num_ins, cpu_speed):
    #Instruction cache is read only and is hence on average, about 10 times faster than Data cache
    ins_clocks=2
    data_clocks=20

    #on a modern cpu, cache hit rate is 95%, so we shall assume that
    hit_rate=0.95
    
    #time taken for a Split L1 cache system
    split_cache_list=[]
    for balance_factor in balance_factor_list:
        inst_cycles = (hit_rate * balance_factor * num_ins * ins_clocks) + ((1-hit_rate) * balance_factor * num_ins * miss_penalty)
        data_cycles = (hit_rate * (1-balance_factor) * num_ins * data_clocks) + ((1-hit_rate) * (1-balance_factor) * num_ins * miss_penalty)
        total_cycles= inst_cycles + data_cycles
        total_time=total_cycles//cpu_speed
        split_cache_list.append(total_time)
    print("Time Required for each program in Split Cache: (in seconds)",split_cache_list)
    
    #-------------------------------------------------------------------------------------------------------------------------------------------
   
    #using a virtual split cache increases hit rate to 99%
    hit_rate=0.99
    
    #but the drawback is that we have to make both Instruction and Data caches read & write capable
    ins_clocks=15
    data_clocks=20
    
    #time taken for a Virtual Split L1 cache system
    virtual_split_cache_list=[]
    for balance_factor in balance_factor_list:
        inst_cycles = (hit_rate * balance_factor * num_ins * ins_clocks) + ((1-hit_rate) * balance_factor * num_ins * miss_penalty)
        data_cycles = (hit_rate * (1-balance_factor) * num_ins * data_clocks) + ((1-hit_rate) * (1-balance_factor) * num_ins * miss_penalty)
        total_cycles= inst_cycles + data_cycles
        total_time=total_cycles//cpu_speed
        virtual_split_cache_list.append(total_time)
    print("Time Required for each program in VSC: (in seconds)",virtual_split_cache_list)
    
    r = [1,2,3,4,5,6,7,8,9,10]
    X_axis = [i-0.2 for i in r]
    X_axis2 = [i+0.2 for i in r]
    plt.bar(X_axis,split_cache_list,0.4,color='orange')
    plt.bar(X_axis2,virtual_split_cache_list,0.4,color='b')
    plt.xticks(X_axis, balance_factor_list)
    plt.xlabel("Balance Factors")
    plt.ylabel("Time Taken (in Seconds)")
    plt.title(f"Miss Penalty {miss_penalty} cycles")
    legd=['Split Cache','VSC']
    plt.legend(legd)
    plt.show()
    return
    
#miss penalty, we assume that 100 clock cycles are lost for a miss and acccess from L2 cache
miss_penalty=500
simulate(miss_penalty, balance_factor_list, num_ins, cpu_speed)

miss_penalty=1000
simulate(miss_penalty, balance_factor_list, num_ins, cpu_speed)

#200 is the most realistic miss penalty
miss_penalty=200
simulate(miss_penalty, balance_factor_list, num_ins, cpu_speed)

miss_penalty=75
simulate(miss_penalty, balance_factor_list, num_ins, cpu_speed)
