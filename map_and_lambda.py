class map_lambda:
    def ml(self):
        n = int(input())
        list1 = list(map(int,input().split()))
        print(sum(list1) * sum(list1))
        
fibo = map_lambda()
fibo.ml()