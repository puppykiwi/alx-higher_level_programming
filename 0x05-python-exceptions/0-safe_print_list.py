def safe_print_list(my_list=[], x=0):
    try:
        [print(x,end=('')) for  x in my_list]
        print('\n')
    except:
        print("The program ran into a fatal crash")

safe_print_list(my_list=[1,2,3,4],x=2)