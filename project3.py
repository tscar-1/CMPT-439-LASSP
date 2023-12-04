import numpy as np
import math

def gaussSeidel(augMtx, delta, flag):
    n = len(augMtx) # gets row size of augmented matrix
    prevSoln = np.zeros(n) # initialization of starting approximation vector (set to [0, 0, 0] by default)
    currSoln = np.zeros(n) # initialization of solution vector
    
    # loop runs until specified stopping criteria is reached
    while True:
        mae = 0 # initialization of the mean absolute error
        rmse = 0 # initialization of the root mean square error
        
        # loop through the coefficients in each equation
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += augMtx[i][j] * currSoln[j] # use the values from the current solution to compute the sum
            currSoln[i] = (augMtx[i][n] - sum) / augMtx[i][i] # computes the new approximation
        
        # computes errors based on current and previous approximations
        for i in range(n):
            mae += abs(currSoln[i] - prevSoln[i])
            rmse += (currSoln[i] - prevSoln[i]) ** 2
        
        if flag == 1: # approximate mean absolute error
            if mae / n < delta:
                return currSoln
        elif flag == 2: # approximate root mean square error
            if np.sqrt(rmse / n) < delta:
                return currSoln
        elif flag == 3: # true mean absolute error
            if mae < delta:
                return currSoln
        elif flag == 4: # true root mean square error
            if np.sqrt(rmse) < delta:
                return currSoln
        
        # copies the current solution to the previous solution for the next iteration
        prevSoln = np.copy(currSoln)

def jacobi(augMtx, delta, flag):
    n = len(augMtx) # gets row size of augmented matrix
    prevSoln = [0] * n # initialization of starting approximation vector (set to [0, 0, 0] by default)
    currSoln = [0] * n # initialization of solution vector
    
    # loop runs until specified stopping criteria is reached
    while True:
        mae = 0 # initialization of the mean absolute error
        rmse = 0 # initialization of the root mean square error
        
        # loop through the coefficients in each equation
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += augMtx[i][j] * prevSoln[j] # use the values from the previous solution to compute the sum
            currSoln[i] = (augMtx[i][n] - sum) / augMtx[i][i] # computes the new approximation
        
        # computes errors based on current and previous approximations
        for i in range(n):
            mae += abs(currSoln[i] - prevSoln[i])
            rmse += math.pow(currSoln[i] - prevSoln[i], 2)
        
        if flag == 1: # approximate mean absolute error
            if mae / n < delta:
                return currSoln
        elif flag == 2: # approximate root mean square error
            if math.sqrt(rmse / n) < delta:
                return currSoln
        elif flag == 3: # true mean absolute error
            if mae < delta:
                return currSoln
        elif flag == 4: # true root mean square error
            if math.sqrt(rmse) < delta:
                return currSoln
        
        # copies the current solution to the previous solution for the next iteration
        prevSoln = currSoln.copy()
  
if __name__ == '__main__':
  main()
