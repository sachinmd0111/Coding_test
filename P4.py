for i in range(1,6):
    steps=2*i-1;
    iterator=1;
    looper=1;
    while(looper<=steps):
        print(iterator,end=' ')
        if (looper>=i):
            iterator-=1
        else:
            iterator+=1
        looper+=1
    print();
