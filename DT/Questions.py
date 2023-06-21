class Question :
    Children = []
    Data = "NoQuestion"
    Attribute = None
    Entropy = 1 
    GiniIndex = 1
    def __init__(self):
        pass

class Child:
    def __init__(self):
        self.Answer = -1
        self.Instances = []
        self.Question = None
        self.Is_Visited = False
        self.Height = -1

class pclass (Question):
    Data = "pclass"
    def split(instances):
        child1 = Child()
        child2 = Child()
        child3 = Child()

        for instance in instances:
            if(instance[0] == 1):
                child1.Instances.append(instance)
            elif(instance[0] == 2):
                child2.Instances.append(instance)
            else:
                child3.Instances.append(instance)
        pclass.Children = [child1 , child2 , child3]

class sex (Question):
    Data = "sex"
    def split(instances):
        child1 = Child()
        child2 = Child()
        for instance in instances:
            if(instance[2] == "female"):
                child1.Instances.append(instance)
            else:
                child2.Instances.append(instance)
        sex.Children = [child1 , child2]
                
class age (Question):
    Data = "age"
    def split(instances):
        child0 = Child()
        child1 = Child()
        child2 = Child()
        child3 = Child()
        child4 = Child()
        child5 = Child()
        for instance in instances:
            try:
                i_age = int(instance[3])
            except ValueError :
                continue
            finally:
                if i_age >= 80:
                    child5.Instances.append(instance)
                elif 65 <= i_age < 80:
                    child4.Instances.append(instance)
                elif 50 <= i_age < 65:
                    child3.Instances.append(instance)
                elif 35 <= i_age < 50:
                    child2.Instances.append(instance)
                elif 10 <= i_age < 35:
                    child1.Instances.append(instance)
                else:
                    child0.Instances.append(instance)
                age.Children = [child0 , child1 , child2 , child3 , child4 , child5]


class cabin (Question):
    Data = "cabin"
    def split(instances):
        child0 = Child()
        child1 = Child()
        child2 = Child()
        child3 = Child()
        child4 = Child()
        child5 = Child()
        for instance in instances:
            try :
                c = instance[-3][0]
            except :
                continue
            if( c == "A"):
                child0.Instances.append(instance)
            if(c == "B"):
                child1.Instances.append(instance)
            elif( c == "C"):
                child2.Instances.append(instance)
            elif(c == "D"):
                child3.Instances.append(instance)
            elif(c == "E"):
                child4.Instances.append(instance)
            elif(c == "F"):
                child5.Instances.append(instance)
            else :
                continue
            cabin.Children = [child0 , child1 , child2 
            , child3 , child4 , child5] 


class est():
    Data = "WaitEstimate?"
    def split(instances):
        child0 = Child()
        child1 = Child()
        child2=  Child()
        child3=  Child()
        for instance in instances:
            if instance[-2] == "0-10":
                child0.Instances.append(instance)
            elif instance[-2] == "10-30" :
                child1.Instances.append(instance)
            elif instance[-2] == "30-60":
                child2.Instances.append(instance)
            else:
                child3.Instances.append(instance)
            
        est.Children = [child0 , child1 , child2 , child3 ]
    

class Rain():
    Data = "raining?"
    def split(instances):
        child0 = Child()
        child1 = Child()
        for instance in instances:
            if(instance[6]== "Yes"):
                child0.Instances.append(instance)
            else:
                child1.Instances.append(instance)
        Rain.Children = [child0 , child1 ]


class Pat():
    Data = "Patron?"
    def split(instances):
        child0 = Child()
        child1 = Child()
        child2=  Child()
        for instance in instances:
            if(instance[4]== "Some"):
                child0.Instances.append(instance)
            elif instance[4] == "Full":
                child1.Instances.append(instance)
            else:
                child2.Instances.append(instance)
            
        Pat.Children = [child0 , child1 , child2 ]

class alt():
    Data = "alternate?"
    def split(instances):
        child0 = Child()
        child1 = Child()
        for instance in instances:
            if(instance[0]== "Yes"):
                child0.Instances.append(instance)
            else:
                child1.Instances.append(instance)
            
        alt.Children = [child0 , child1 ]

class Bar():
    Data = "Bar?"
    def split(instances):
        child0 = Child()
        child1 = Child()
        for instance in instances:
            if(instance[1]== "Yes"):
                child0.Instances.append(instance)
            else:
                child1.Instances.append(instance)
            
        Bar.Children = [child0 , child1 ]

class Fri():
    Data = "Friday?"
    def split(instances):
        child0 = Child()
        child1 = Child()
        for instance in instances:
            if(instance[2]== "Yes"):
                child0.Instances.append(instance)
            else:
                child1.Instances.append(instance)
            
        Fri.Children = [child0 , child1 ]

class Hungry():
    Data = "Hungry?"
    def split(instances):
        child0 = Child()
        child1 = Child()
        child2=  Child()
        for instance in instances:
            if(instance[3]== "Some"):
                child0.Instances.append(instance)
            elif instance[3] == "Full":
                child1.Instances.append(instance)
            else:
                child2.Instances.append(instance)
            
        Hungry.Children = [child0 , child1 , child2 ]