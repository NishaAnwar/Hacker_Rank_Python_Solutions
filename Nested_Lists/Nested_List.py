if __name__ == '__main__':
    nested_arr=[]
    for _ in range(int(input())):
        
        name = input()
        score = float(input())
        nested_arr.append([name,score])
    lowest_scores=[]
        
    for item in nested_arr:
        lowest_scores.append(item[1])
    lowest_scores = sorted(set(lowest_scores)) 
    second_lowest=lowest_scores[1]
    names=[]
    for item in nested_arr:
        if item[1]==second_lowest:
            names.append(item[0])
    names.sort()
    for item in names:
        print(item)
    
            
        
    
