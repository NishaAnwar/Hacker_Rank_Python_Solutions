if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average=0
    for item in student_marks:
        if query_name==item:
            marks_list=student_marks[item]
            for i in range(len(marks_list)):
                average+=marks_list[i]
            average=average/len(marks_list)
            
    print(f"{average:.2f}")
    
                
            
                
        
