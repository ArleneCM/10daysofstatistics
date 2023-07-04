def interQuartile(values, freqs):
    arr = []
    for value, freq in zip(values, freqs):
        arr += [value] * freq
    arr.sort() 
    q1=median(arr[: len(arr)//2]) 
    q2=median(arr)     
    q3=median(arr[len(arr)//2 *-1:]) 
    result=q3-q1
    print(f'{result:.1f}')
