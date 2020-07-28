m='Меня видно везде'

def a():
    ma='меня видно в b() и в a()'

    def b():
        print(m)
        print(ma)
        mb='Меня видно в c() и в b() но не видно в а'

        def c():
            print(m)
            print(ma)
            print(mb)
            mc='Меня видно только в с'

        # print(mc)
        c()
    b()
a()
