def gaussSeidel(augMtx, delta, flag):
  n = len(augMtx)
  prevSoln = [0] * n
  currSoln = [0] * n

  while True:
    mae = 0
    rmse = 0
    
    for i in range(n):
    sum = 0
    for j in range(n):
      if i != j:
        sum += augMtx[i][j] * currSoln[j]
    currSoln[i] = (augMtx[i][n] - sum / augMtx[i][i]

    for i in range(n):
      mae += abs(currSoln[i] - prevSoln[i])
      rmse += math.pow(currSoln[i] - prevSoln[i], 2)

    if flag == 1:
      pass
    elif flag == 2:
      pass
    elif flag == 3:
      pass

    if mae < delta or rmse < delta:
      break

  return currSoln

def jacobi():
  
  
if __name__ == '__main__':
  main()
