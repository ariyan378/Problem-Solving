def runner_up(arr_student):
    arr_student = list(arr_student)
    arr_student.sort(reverse=True)
    for i in range(len(arr_student)):
        if arr_student[i]!= arr_student[i+1]:
            runner_up = arr_student[i+1]
            break
        else:
            continue
    print(runner_up)            
        
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up(arr)