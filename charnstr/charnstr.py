# https://stackoverflow.com/a/7086420/9475509
def analyze(string):
  # https://stackoverflow.com/a/71250746/9475509
  """
  Analyze unique characters from a string
  
  :param str string: The string to be analyzed
  :return: Information of unique characters and count of each
  :rtype: dict
  """
  
  # https://stackoverflow.com/a/1007499/9475509
  str2 = string.replace(" ", "_")
  
  # https://stackoverflow.com/a/13902829/9475509
  unique = ''.join(set(str2))
  
  # https://stackoverflow.com/a/15046263/9475509
  sotd = ''.join(sorted(unique))
  
  # https://stackoverflow.com/a/1712236/9475509
  N = len(sotd)
  
  # https://stackoverflow.com/a/5205580/9475509
  keys = [' '] * N
  vals = [0] * N
  
  # https://stackoverflow.com/a/61932501/9475509
  for i in range(N):
    # https://stackoverflow.com/a/8848336/9475509
    keys[i] = sotd[i]
    
    # https://stackoverflow.com/a/1155647/9475509  
    count = str2.count(keys[i])
    
    # https://stackoverflow.com/a/63195804/9475509
    vals[i] += count
  
  # https://stackoverflow.com/a/209854/9475509
  result = dict(zip(keys, vals))
  
  return result