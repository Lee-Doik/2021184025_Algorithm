import sys

questions = [
  [5, 11, 7, 16, 9, 17, 16, 16, 6, 12],
  [14, 14, 8, 6, 4, 19, 12, 3, 3, 8],
  [16, 18, 8, 3, 7, 11, 11, 4, 12, 4],
  [12, 13, 4, 19, 13, 13, 9, 16, 18, 16],
  [16, 10, 18, 13, 18, 8, 3, 3, 6, 6],
  [11, 17, 13, 16, 7, 12, 12, 11, 14, 12],
]

#  출력은 ((5x11) x (11x7)) x (7x16) 과 같은 형태로 한다.

def cmm(sizes):
  print(f'{sizes=}')
  mc = len(sizes) - 1
  C = questions
  P = [[0 for x in range(mc)] for x in range(mc)]
  for sub in range(2, mc + 1):
    for s in range(1, mc - sub + 1):
      e = s + sub - 1
      P[s][e] = float('inf')
      for k in range(s, e + 1):
        q = P[s][k] + P[k + 1][e] + sizes[s - 1] * sizes[k] * sizes[e]
        if q < P[s][e]:
          P[s][e] = q

  print(C[1][mc], result(sizes, P, 1, mc))

def result(sizes, P, s, e):
  if s == e:  
    return f'({sizes[s - 1]}x{sizes[s]})'
  p = P[s][e - 1]
  if p == 0: return ''

  a = result(sizes, P, s, p)
  b = result(sizes, P, p + 1, e)
  return f'({a} x {b})'

for q in questions:
  cmm(q)    