import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self,**test):
        self.contents=[]
        for color,number in test.items():
            for i in range(number):
                self.contents.append(str(color))
    
    # returns value of content
    def get_contents(self):
        return self.contents
    
    def draw(self,n):
      if n>len(self.contents):
        return self.contents
           
      self.sample = [] # Creating List
    
      for i in range(n):
        singleDraw=random.choice(self.contents) # From random module
        self.sample.append(singleDraw)
        index=self.contents.index(singleDraw)
        self.contents.pop(index) # Removing the drawn sample
    
      return self.sample



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
        
    probabilityCounter=0  # Variable to calculate positive occurances
    
    for experiment in range(num_experiments):
        
        hats=copy.deepcopy(hat)
        sampleList=hats.draw(num_balls_drawn)
        
        sampleDict = {color: sampleList.count(color) for color in set(sampleList)}
        
        match = True
        
        for color,value in expected_balls.items():
            if (color in sampleDict) and (expected_balls[color]<=sampleDict[color]):
                continue
            else:
                match=False
                
        if match:
            probabilityCounter+=1  
    
    
    return probabilityCounter/num_experiments 
    # Calculating probability
