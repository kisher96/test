def print_sep(sep, sep_len):
    print(sep *sep_len)
    return sep*sep_len

# меняем знак разделителя
print_sep('*', 100)
print_sep("0-", 100)

print_sep('-', 50)

sep=print_sep('-', 50)
text='Hello {} Func {}'.format(sep,sep)

print(text)

# result=print_sep('-',50)
# print(result)