'''
Source code from https://github.com/qqiang00/Reinforce/blob/master/reinforce/gridworld.py
'''

states = [i for i in range(16)]
values = [0 for _ in range(16)]
actions = ['n','e','s','w']
ds_actions = {'n':-4,'e':1,'s':4,'w':-1} #因为方格世界中上面的数比下面小4故向上走状态就得减去4 同理知e,s,w
gamma = 1.00


def nextState(s, a):
    next_state = s
    if (s%4 == 0 and a ==  'w') or (s <4 and a == 'n') or \
        (s+1 % 4 == 0 and a == 'e') or (s > 11 and a == 's'):
        pass
    else:   
        next_state = s + ds_actions[a] #ds_actions得到该动作的所对应的数值
    return next_state


def reward(s):            #某一状态的及时奖励
    return 0 if s in [0, 15] else -1


def isTerminateState(s):  #是否为终止状态
    return s in [0, 15]


def getSuccessors(s):   #得到后继状态
    successors = []
    if isTerminateState(s):
        return successors
    else:
        for a in actions:
            next_state = nextState(s,a)
            successors.append(next_state)
    return successors


def updatValue(s):   #根据后继状态 更新某一状态价值 
    successors = getSuccessors(s)
    newValue = 0
    instantReward = reward(s)
    for successor in successors:
        newValue += 1/4*(instantReward + gamma * values[successor])
    return newValue


def performOneIteration():   #进行一次迭代
    newValues = [0 for _ in range(16)]
    for s in states:
        newValues[s] = updatValue(s)
    global values
    values = newValues
    printValue(values)


def printValue(v):     #输出状态价值
    for i in range(16):
        print("{0:>6.2f}".format(v[i]), end= ' ')
        if (i + 1)% 4 == 0:
            print("")
    print()


def main():    #主函数
    max_iterate_times = 150
    cur_iterate_times = 0
    while cur_iterate_times < max_iterate_times:
        print("Iterate No.{}".format(cur_iterate_times))
        performOneIteration()
        cur_iterate_times += 1
    #printValue(values)


if __name__ == "__main__":
    main()