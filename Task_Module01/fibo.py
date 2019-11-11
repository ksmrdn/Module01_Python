# def fibo(param):
#     fi = 0
#     bo = 1
#     result = [fi,bo]
#     for num in range(0, param-1):
#         fibo = fi + bo
#         fi = bo
#         bo = fibo
#         result.append(fibo)
#     print(result)
#     print(fibo)
#     # result.append(fibo0)
#     # print(result)
# fibo(8)

# def fibo1(urutan):
#     if urutan < 2:
#         return urutan
#     else:
#         return(urutan-1)+fibo(urutan-2)
# print(fibo1(0))

class Fibo:
    def fibo1(self, urutan):
        if urutan < 2:
            return urutan
        else:
            return self.fibo1(urutan-1)+ self.fibo1(urutan-2)

Fibo = Fibo()
print(Fibo.fibo1(1))
print(Fibo.fibo1(4))
