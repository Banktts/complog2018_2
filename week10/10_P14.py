def tiling(x,c):
  if x==1 : return 1
  else:
    if c[-1]=="G":
      return tiling(x-1,c+"R")+tiling(x-1,c+"B")
    else:
      return tiling(x-1,c+"R")+tiling(x-1,c+"B")+tiling(x-1,c+"G")
N= int(input())
print(tiling(N,"G")+tiling(N,"R")+tiling(N,"B"))
