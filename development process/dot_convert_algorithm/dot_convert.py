def convert_dot(dot_list):
    l=len(dot_list)
    t_list=[0]*l

    for i in range(l):
        n=i%6
        if n == 0 or n == 5:
            t_list[i]=dot_list[i]
        elif n == 4:
            t_list[i-1]=dot_list[i]
        elif n == 3:
            t_list[i-2]=dot_list[i]
        elif n == 2:
            t_list[i+2]=dot_list[i]
        else:
            t_list[i+1]=dot_list[i]

    return t_list

if '__main__':
    test = [[0,1,0,1,0,1],[1,1,1,0,0,0],[1,0,0,0,0,1,1,1,1,0,0,0]]

    for _ in test:
        print('input : ',_)
        print('ouput : ',convert_dot(_))

    '''
    ----------- result -----------
    input :  [0, 1, 0, 1, 0, 1]
    ouput :  [0, 1, 1, 0, 0, 1]
    input :  [1, 1, 1, 0, 0, 0]
    ouput :  [1, 0, 1, 0, 1, 0]
    input :  [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
    ouput :  [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0]
    -------------------------------
    '''