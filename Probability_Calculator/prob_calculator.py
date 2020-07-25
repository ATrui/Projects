import random
import copy

class Hat():
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for x in range(value):
        self.contents.append(key)

  def draw(self, balls):
    if balls > len(self.contents):
      return self.contents
    else:
      drawn = []
      contents = self.contents
      while len(drawn) < balls:
        d = random.choice(contents)
        contents.remove(d)
        drawn.append(d)
      return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0 

  for experiment in range(num_experiments):

    exp_hat = copy.deepcopy(hat)

    exp_draw = exp_hat.draw(num_balls_drawn) 

    good = 0   

    for colour in expected_balls.keys():

      if exp_draw.count(colour)>= expected_balls[colour]:
        good +=1 
   
    if good == len(expected_balls):
      m+=1

  return m/num_experiments