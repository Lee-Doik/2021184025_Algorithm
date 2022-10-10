from random import randint
words = [
  'jingo', 'lf', 'log', 'non', 'lj', 'goo', 'hmg', 'joe', 'knell', 'minim',
  '2021184025', '이도익',
  'ion', 'in', 'gen', 'mono', 'feign', 'look', 'hinge', 'moonie', 'nil', 'ginkgo',
  'kilo', 'fief', 'ikon', 'moon', 'long', 'hf', 'lifeline', 'lingo', 'mink', 'nigh',
  'k', 'killing', 'hoi', 'mongol', 'nikkei', 'ime', 'hoof', 'me', 'floe', 'omen',
  'jiff', 'mike', 'foe', 'ingoing', 'leg', 'kiln', 'fin', 'noel', 'niff', 'minion',
  'gnome', 'ill', 'ogle', 'info', 'igloo', 'fife', 'milk', 'loo', 'en', 'high',
  'f', 'kook', 'miff', 'hele', 'hmi', 'longing', 'kink', 'n', 'fee', 'mm',
  'hole', 'hellene', 'mien', 'moo', 'homing', 'jiggle', 'inkling', 'll', 'off', 'goof',
  'lifelike', 'feline', 'lie', 'jingle', 'eel', 'filo', 'nook', 'eeg', 'gillie', 'leonine',
  'ko', 'elk', 'honk', 'lien', 'mme', 'feeling', 'kneel', 'fleming', 'em', 'glee',
  'mil', 'homo', 'offing', 'engine', 'limekiln', 'film', 'giggle', 'folio', 'ming', 'men',
]

def insertionsort(start, end): # end = Inclusive
  for i in range(start, + 1, end + 1):
    v = array[i] # i 위치의 v 값이 주인공
    j = i -1 # v와 비교를 시작할 위치
    while start <= j and array[j] > v:
      array[j + 1] = array[j] # 오른쪽으로 밀어준다
      j -= 1
    array[j + 1] = v #주인공을 도착할 위치에 넣는다.

def quickSort(start, end): # end = Inclusive
  if start >= end: return
  if end < start + 5: #size of this array <= 10
    insertionsort(start, end)
    return
  pi = partition(start, end - 1)
  quickSort(start, pi - 1)
  quickSort(pi + 1, end)

def partition(start, end): #end = Inclusive

  ri = randint(start, end)
  array[start], array[ri] = array[ri], array[start]
  pv = array[start]

  p, q = start, end + 1

  while True:
    #find p
    while True:
      p += 1
      if q < p: break
      if p > end or array[p] > pv: break
    #found p

    #find q
    while True:
      q -= 1
      if q < p: break
      if q < start or array[q] <= pv : break
    #found q

    if p >= q: break # 더이상 바꿀 요소가 없다.

    #swap @p and @q
    array[p], array[q] = array[q], array[p]

  #swap @start and @q
  if start != q:
    array[start], array[q] = array[q], array[start]

  return q

array = words
quickSort(0, len(array))
print(array)
