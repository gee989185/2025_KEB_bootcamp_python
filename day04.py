# # closure
# def out_func(nout):               #
#     def inner_func():             #
#         return nout * nout        #
#     return inner_func             #
#
#
# x = out_func(9)
# print(type(x))
# print(x)
# print(x())

#inner function
def out_func(nout):                 #2
    def inner_func(nin):            #4
        return nin * nin            #5
    return inner_func(nout)         #3

print(out_func(5))                  #1