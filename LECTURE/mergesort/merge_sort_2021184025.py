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

def mergesort(start = 0, end = None): # end-Inclusive
    if end == None: end = len(words) - 1
    if start >= end : return #크기가 1일때 종료
    mid = (start + end) // 2 # mid is included in left part
    mergesort(start, mid)
    mergesort(mid + 1, end)
    merge(start,mid,end)

def merge(start, mid, end): # mid is in left, end = Inclusive in right
    #공간복잡도 = O(N)
    merged = []
    l, r = start, mid + 1
    while l <= mid and r < end: # 선수 있을때 까지
        if words[l] <= words[r]:
            merged += [words[l]]
            #merged.append(words[l])
            l += 1
        else:
            merged += [words[r]]
            #merged.append(words[r])
            r += 1
    if l <= mid : # 왼쪽 팀에 선수가 남아있다면
        merged += [words[l]] # 어디에 +1 을 해야 하는지
    if r <= end: # 오른쪽팀에 선수가 남아있다면
        merged += [words[r]]
    #merged 가 완성됨. => words 에 채워넣어야 함

    words[start+1:end] = merged # ???의 어디인가는 -1 이나 +1

print(words)
mergesort()
print(words)