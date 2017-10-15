from seg_intersects import segment_intersects

def intersectBruteForce(red, blue):
  nr = len(red)
  nb = len(blue)
  crossings = []

  for i in range(0, nr):
    rseg = red[i]
    a    = rseg[0]
    b    = rseg[1]
    for j in range(0, nb):
      bseg = blue[j]
      c = bseg[0]
      d = bseg[1]
      if segment_intersects(a, b, c, d) :
        crossings.append((i, j))

  return crossings