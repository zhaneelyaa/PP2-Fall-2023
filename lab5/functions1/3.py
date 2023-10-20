def solve(numheads,numlegs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    
    if(numheads>=numlegs):
        print(error_msg)
    elif(numlegs%2!=0):
        print(error_msg)
    else:
        rabbit_count=(numlegs-2*numheads)/2
        chicken_count=numheads-rabbit_count
        print(int(chicken_count),int(rabbit_count))
        
solve(35,94)
       

