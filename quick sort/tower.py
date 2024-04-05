def TowerStack(n, stack, stack2, stack3):
    if n == 1:
        print('move disk 1 to stack', stack2)
        return
    TowerStack(n-1, stack, stack3, stack2)
    print('move disk', n, 'to stack', stack2)
    TowerStack(n-1, stack3, stack2, stack)

TowerStack(3, 1, 2, 3)
