n = int(input())
D = {'global':{'parent': None, 'vars':[]}}
def create(namespace,parent):
  k = 'vars'
  D[parent][k].append(namespace)
  D[namespace] = {'parent': parent, 'vars':[]}
def add(namespace,var):
  k = 'vars'
  D[namespace][k].append(var)
def get(namespace,var):
  k1 = 'vars'
  k2 = 'parent'
  if var in D[namespace][k1]:
    print(namespace)
  elif namespace != "global":
    return get(D[namespace][k2],var)
  else:
    print("None")
for i in range(n):
  s0, s1, s2 = str(input()).split()
  if s0 == "create":
    create(s1,s2)
  elif s0 == "add":
    add(s1,s2)
  else:
    get(s1,s2)