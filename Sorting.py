def SelectionSort(arr,n): #selects minimum from the array ,T.C=O(n^2)

    for i in range(n):
        mini=i              #mini for comparison
        
        for j in range(i+1,n):      
            if arr[mini]>arr[j]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i] #swap
    
    return arr

def BubbleSort(arr,n): # pushes the max to end by adjacent swapping ,worst /avg case T.C=O(n^2),else T.C=O(n)

    for i in range(n-1,1,-1): # from n-1 to 0 
        swap=0
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=1
        if swap==0:
            break
    return arr

def InsertionSort(arr,n): #places value in its correct position # worst /avg case T.C=O(n^2),else T.C=O(n) 
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr

def Merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while(left<=mid) and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]

def mSort(arr,low,high):
    if low>=high:
        return 
    mid=(low+high)//2

    mSort(arr,low,mid)
    mSort(arr,mid+1,high)
    
    Merge(arr,low,mid,high)


arr=[10,2,20,10,1,2,4,99,1]
n=len(arr)-1
low=0
high=n
mSort(arr,low,high)
print(arr)            
