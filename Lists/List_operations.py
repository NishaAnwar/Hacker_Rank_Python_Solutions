if __name__ == '__main__':
    N = int(input())
    lst=[]
    command_list=[]
    for i in range(N):
        commands=input()
        command_list.append(commands)
    for item in command_list:
        if 'insert' in item:
            _,i,e=item.split()
            lst.insert(int(i),int(e)) 
        elif 'print' in item:
            print(lst)
        elif 'remove' in item:
            _,e=item.split()
            lst.remove(int(e)) 
        elif 'append' in item:
            _,e=item.split()
            lst.append(int(e))
        elif 'sort' in item:
            lst.sort()
        elif 'pop' in item:
            lst.pop()
        else:
            lst.reverse()
            
           
        
        
        
        
        
