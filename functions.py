#from IPython.utils.text import num_ini_spaces
class functions:
  def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        functions.mergeSort(left)
        functions.mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if int(left[i] )<= int(right[j]):
              # The value from the left half has been used
              myList[k] = int(left[i])
              # Move the iterator forward
              i += 1
            else:
                myList[k] = int(right[j])
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
    return myList
  
  def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if (float(lys[mid]) == val):
          index = mid
        else:
            if val<float(lys[mid]):
                last = mid -1
            else:
                first = mid +1
    return index

  def searchAdd(target, lista):
    resp=[]
    ListaOr = functions.mergeSort(lista)
    numList2 = ListaOr[:]
    for i in range(0, len(ListaOr)):
      targetTemp = (float(target) - float(ListaOr[i]))
      piv = functions.BinarySearch(numList2,float (targetTemp))
      suma=(float(numList2[piv])+ float(ListaOr[i]))
      if (piv != -1) and ( float(ListaOr[i]) != float(numList2[piv]))  and suma==float(target): 
        resp.append([int(numList2[piv]),int(ListaOr[i])])
        numList2[i] = 0.5
    return resp

  def readList(fileName):
    file = open(fileName, mode="r").read()
    space=file.index(' ')
    subStr = file[:space]
    return subStr.split(',')

  def readTarget(fileName):
    file = open(fileName, mode="r").read()
    space = file.index(' ')
    subStr = file[space:]
    return subStr

  def twoCompare(numList1,target):
    res = [] 
    i=0
    #numList1.remove('')
    numList2 = numList1 [:] #copy of array
    for left in range(0, len(numList1)): #run array numList1 from left to right
      right = len(numList2)-1
      while left<right:  #run the numList2 array from right to left without jumping to the counter
        sum=(int(numList1[left])+int(numList2[right]))
        if sum == int(target):
          res.append([int(numList1[left]),int(numList2[right])])# save the pair of numbers
        right -=1 #decrease the right counter
        i+=1
      left += 1 #increment the left counter
    return (res,i) 

  def Compare(numList1,target,result):
    if len(numList1) > 0:
      primero = int(numList1[0])
      for left in range(1,len(numList1)):
       # print(i)
        sum=(primero + int(numList1[left]))
        if sum == int(target):
            result.append([primero,int(numList1[left])])
            numList1.pop(left)
            numList1.pop(0)
            functions.Compare(numList1,target,result)
            break
        elif left == (len(numList1)-1):
            numList1.pop(0)
            functions.Compare(numList1, target,result)
            break
        left += 1
    else:
      return(result)
    return(result)

  def count_elapsed_time(f):    
    def wrapper():
        # Start counting.
        start_time = time()
        # Take the original function's return value.
        ret = f()
        # Calculate the elapsed time.
        elapsed_time = time() - start_time
        print("Elapsed time: %0.10f seconds." % elapsed_time)
        return ret
    return wrapper

  

   
