# https://github.com/TehMillhouse/PyMarkovChain
# pip install PyMarkovChain
from pymarkovchain import MarkovChain

mc = MarkovChain("./am_m")
f = open('cap_short.txt','r')
mc.generateDatabase(f.read())
for x in range(0,20):
    str=mc.generateString()
    if(len(str))>10:
        print(str)
