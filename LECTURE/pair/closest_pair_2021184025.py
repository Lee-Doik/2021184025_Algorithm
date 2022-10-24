from math import *
class City:
  def __init__(self, name, x, y, index=0):
    self.name = name
    self.x, self.y = x, y
    self.index = index
  def __repr__(self):
    return f'{self.name}({self.index}:{self.x:3d},{self.y:3d})'

cities = [
  City("Twain", 1220, 488, 42),
  City("Allow", 1192, 401, 43),
  City("Kiosk", 1131, 611, 44),
  City("Wheat", 1044, 133, 45),
  City("Birch", 1240, 519, 46),
  City("Flail", 1415, 72, 47),
  City("Thong", 190, 385, 48),
  City("Bongo", 528, 455, 49),
  City("Quilt", 800, 365, 50),
  City("Satyr", 1315, 172, 51),
  City("Alibi", 133, 245, 52),
  City("Auger", 442, 866, 53),
  City("Event", 218, 174, 54),
  City("Scowl", 206, 61, 55),
  City("Shelf", 928, 242, 56),
  City("Melon", 527, 416, 57),
  City("Scrap", 471, 625, 58),
  City("Drupe", 880, 13, 59),
  City("Nadir", 1163, 145, 60),
  City("Kudos", 1426, 806, 61),
  City("Pushy", 14, 429, 62),
]

def distance(c1, c2):
  return sqrt((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2)

def closest_of_three(array, start, end): #end_Inclusive
  # size = end - start + 1
  # if size != 3:
  #   print(f"Hey this array size is not three : it's {size}")
  #   exit(0)

  d1 = distance(array[start], array[start + 1])
  d2 = distance(array[start], array[start + 2])
  d3 = distance(array[start + 1], array[start + 2])
  min_distance = min(d1, d2, d3)

  if min_distance == d1:
    return start, start + 1, d1
  if min_distance == d2:
    return start, start + 2, d2
  if min_distance == d3:
    return start + 1, start + 2, d3

def closest_pair(array, start, end): # end_Inclusive
  size = end - start + 1
  if size <= 1:
    print(f"BUG : it's {size}")
    exit(0)
  if size == 2:
    return start, end, distance(array[start], array[end])
  if size == 3:
    return closest_of_three(array, start, end)

  last_left = (start + end) // 2

  ls, le, ld = closest_pair(array, start, last_left)  # left group
  rs, re, rd = closest_pair(array, last_left + 1, end)  # right group

  s, e, d = (ls, le, ld) if ld <= rd else (rs, re, rd)  # ld rd compair

  x1 = array[last_left].x - d
  x2 = array[last_left].x + d

  # strip = [c for c in cities \
  #          if c.x >= x1 and c.x <= x2 and \
  #          c.index >= start and c.index <= end]
  #
  # strip.sort(key=lambda c:c.y)  # sorted by y

  i1 = min(c.index for c in cities if c.x >= x1 and c.index >= start)
  i2 = max(c.index for c in cities if c.x <= x2 and c.index <= end)
  # strip = sorted(cities[i1:i2+1], key=lambda c:c.y)
  strip = [c for c in cities_y if i1 <= c.index and c.index <= i2]

  n_strip = len(strip)
  for i1 in range(n_strip):
    c1 = strip[i1]
    for i2 in range(i1 + 1, n_strip):
      c2 = strip[i2]
      dy = c2.y - c1.y  # 항상 c2의 y좌표가 큼 (정렬됨)
      if dy > d:
        break
      dd = sqrt((c1.x - c2.x) ** 2 + dy ** 2)
      if d > dd:
        s, e, d = c1.index, c2.index, dd

  return s, e, d

n_cities = len(cities)
print(cities)
cities.sort(key = lambda c : c.x)  # x좌표 로 정렬
for i in range(n_cities):
  cities[i]. index = i
cities_y = sorted(cities, key=lambda c:c.y)
# closest_of_three(cities, 0, len(cities) - 1)
s, e, d = closest_pair(cities, 0, len(cities) - 1)
print(f'{cities[s]} ~ {cities[e]} : {d:.1f}')