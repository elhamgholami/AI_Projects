import math
import pandas 
from Questions import *

#-------------------------------------------------------------------------------------
#Constructing tree
def Calc_entropy(child , question):
    question.split(child.Instances)
    esum = 0 
    for ch in question.Children :

        negatives = len(list(filter(lambda x : x[-1] == 0, ch.Instances)))
        size = len(ch.Instances)

        if(size == 0 ):
            continue

        if( negatives == 0 ):
            ch.Answer == 1
            continue

        elif( negatives == size ):
            ch.Answer == 0
            continue

        esum += (size/len(child.Instances)) * (negatives / size) * math.log(size / negatives , 6)

    question.Entropy = esum
    
def min_entropy(child , Questions):
    min_e = 1
    q = None
    for question in Questions:
        Calc_entropy(child , question)
        if (question.Entropy < min_e):
            min_e = question.Entropy
            q = question
    return q

def Calc_gini(child , question):
    question.split(child.Instances)
    gsum = 0
    for ch in question.Children:
        negatives = len(list(filter(lambda x : x[-1] == 0, child.Instances)))
        size = len(ch.Instances)

        if(size == 0 ):
            continue

        if( negatives == 0 ):
            ch.Answer = 1
            continue

        elif( negatives == size ):
            ch.Answer = 0
            continue

        gsum += (size/len(child.Instances)) * (negatives / size) * (1 - negatives / size)
    
    question.GiniIndex = gsum

def min_gini(instances , Questions):
    min_g = 1
    q = None 
    for question in Questions:
        Calc_gini(instances , question)
        if question.GiniIndex < min_g :
            q = question
    return q 

def Set_Answer(question):
    for child in question.Children :
        negatives = len(list(filter(lambda x : x[-1] == 0, child.Instances)))

        if(negatives > len(child.Instances)- negatives):
            child.Answer = 0
        else :
            child.Answer = 1


def decision_tree(child , Questions , parent_question , compare_base , height =-1): 
    if (parent_question != titanic_root ) :
        # if len(instances[1]) == 0 :
        #     return 

        #set answer for each child
        if len(Questions) == 0 or height+1 >= 4:
            Set_Answer(parent_question)


    if compare_base == "Entropy":
        question = min_entropy(child , Questions)
    else :
        question = min_gini(child , Questions)

    if question == None :
        return

    child.Question = question 
    child.Height = height +1
    parent_question.Attribute = question
    # question.Parent = parent_question
    for ch in question.Children :
        if ch.Answer == -1 and len(ch.Instances) != 0 :
            decision_tree(ch , [x for x in Questions if x != question] , question , compare_base , ch.Height)
    return question

#BFS 
def bfs(question):
    ch = queue.pop(0)
    #When bfs isn't started

    if ch == "\n":
        print(ch)
        #when we reach to leaf
        if queue[0] != "\n":
            bfs(queue[0])
        return 
    print(f"{ch.Data} |" , end=' ')
    for child in question.Children :
        if child.Is_Visited == False and child.Answer ==-1 and len(child.Instances)!=0:
            child.Is_Visited == True
            queue.append(child.Question)
    queue.append("\n")
    if len(queue) == 0:
        return

    bfs(queue[0])

#-------------------------------------------------------------------------------------
#Test
def Test(test , node):
    children = node.Children 
    node.split(test)
    result = -1
    #If there is no data for a question , set the answer as 0
    Is_Nan = True
    for i in range(len(node.Children)):
        if len(node.Children[i].Instances) == 0 :
            Is_Nan = False
            break
    if(Is_Nan):
        return 0

    for i in range(len(node.Children)):
        if len(node.Children[i].Instances) != 0 :
            if children[i].Answer != -1 :
                result = children[i].Answer
                node.Children = children
                return result
            else:
                node.Children = children
                return Test(node.Children[i].Instances, children[i].Question)

#-------------------------------------------------------------------------------------
#FunctionCall

#titanic
titanic_data = pandas.read_csv('path to titanic file')

# Questions = [pclass , sex , age , sibsp , parch , cabin , embarked]
Questions = [pclass , sex , age , cabin ]
titanic_root = Question()
d = Child()
d.Instances = titanic_data.values[1:1100].tolist()
decision_tree(d , Questions , titanic_root , "Entropy")

queue = [titanic_root.Attribute]
bfs(queue[0])
# informationGain(titanic_root.Attribute)
sum = 0
for i in range(1100 , 1309):
    if(titanic_data.values[i][-1] == Test([titanic_data.values[i]], titanic_root.Attribute)):
        sum += 1
print("\nTitanic Tree accuracy:" , sum/2)

#restaurant
res_data = pandas.read_csv('path to restaurant file')
resqs = [alt , Bar , Fri , Hungry , Pat , Rain , est]
res_root = Question()
r = Child()
r.Instances = res_data.values[1:7].tolist()

decision_tree(r, resqs, res_root, "Entropy")

queue = [res_root.Attribute]
bfs(queue[0])
for i in range(8,14):
    if(titanic_data.values[i][-1] == Test([titanic_data.values[i]], titanic_root.Attribute)):
        sum += 1
print("\nRestaurant Tree accuracy:" , sum/2)