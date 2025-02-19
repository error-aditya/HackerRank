class print_function:
    def print_in_string(self):
        n = int(input())
        for i in range(0,n):
                    print(str(i+1),end='')
        
p_string = print_function()
p_string.print_in_string()