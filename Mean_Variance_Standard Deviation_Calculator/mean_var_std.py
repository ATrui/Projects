import numpy as np

def calculate(list):
  if len(list) > 9 or len(list) < 9:
    raise ValueError("List must contain nine numbers.")

  list1 = list[0:3]
  list2 = list[3:6]
  list3 = list[6:9]

  a = np.array([list1, list2, list3])

  mean1 = np.mean(a, axis=0).tolist()
  mean2 = np.mean(a, axis=1).tolist()
  mean_all = np.mean(a)

  var1 = np.var(a, axis=0).tolist()
  var2 = np.var(a, axis=1).tolist()
  var_all = np.var(a)

  std1 = np.std(a, axis=0).tolist()
  std2 = np.std(a, axis=1).tolist()
  std_all = np.std(a)

  max1 = np.max(a, axis=0).tolist()
  max2 = np.max(a, axis=1).tolist()
  max_all = np.max(a)

  min1 = np.min(a, axis=0).tolist()
  min2 = np.min(a, axis=1).tolist()
  min_all= np.min(a)

  sum1 = np.sum(a, axis=0).tolist()
  sum2 = np.sum(a, axis=1).tolist()
  sum_all = np.sum(a)

  calculations = {}
  calculations["mean"] = [mean1, mean2, mean_all]
  calculations["variance"] = [var1, var2, var_all]
  calculations["standard deviation"] = [std1, std2, std_all]
  calculations["max"] = [max1, max2, max_all]
  calculations["min"] = [min1, min2, min_all]
  calculations["sum"] = [sum1, sum2, sum_all]


  return calculations