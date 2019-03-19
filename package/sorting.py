def bubble_sort( items ):
    '''Return array of items, sorted in ascending order'''
    for i, num in enumerate(items):     #enumerate items list to create a tmp variable called num with each iteration
        try:                            #try block for if there is nothing wrong with the index bounds
            if items[i+1] < num:        #if the second item in the list is smaller than the current item
                items[i] = items[i+1]   #swap the items (num acts as temp variable)
                items[i+1] = num        #still swapping
                bubble_sort(items)      #recursively sort the items
        except IndexError:              #catches the exception for when the list index is out of bounds
            pass                        #do nothing
    return items                        #return the sorted list of items

def merge( half1, half2 ):
        '''Return a sorted array by comparing 2 lists with each other'''
        out = []                                          #create a holder array
        while len( half1 ) > 0 and len( half2 ) > 0:      #compare the values at he beginning of the 2 lists
            if half1[0] < half2[0]:                       #if the one in half1 is smaller, it gets added to the final list first and removed from half 1
                out.append(half1[0])
                half1.pop(0)
            else:                                         #if the one in half2 is smaller, it gets added to the final list first and removed from half2
                out.append(half2[0])
                half2.pop(0)

        if len(half1) == 0:                               #if half1 is empty, add the rest of half 2 to the final list
            out = out + half2
        if len(half2) == 0:                               #if half2 is empty, add the rest of half1 to the final list
            out = out + half1

        return out

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    len_items = len(items)          #get the length of the list once so we don't have to do it again

    if len_items == 1:              #if the list has only one item, return the list as is since its already sorted
        return items

    mid = int(len_items / 2)        # find the half-way mark of the list and floor the value using in to get rid of the decimals

    half1 = merge_sort(items[:mid]) #slice the first half of the list into half1 using the midpoint as the termination index
    half2 = merge_sort(items[mid:]) #slice the second half of the list into half2 using the midpoint as the initial index

    return merge(half1, half2)            # sort the 2 halfs and merge them


def quick_sort(items, index = -1):
    '''Return array of items, sorted in ascending order'''
    len_items = len( items )                         #get the length of the list once

    if len_items <= 1:                                  #check if the list is smaller than 1
        return items                                    #return the list as is

    pivot = items[index]                                #initialise the pivot item at the last index
    small = []                                          #initialise an empty small list
    big = []                                            #initialise an empty big list
    duplicate = []                                      #initialise a duplicates list
    for i in items:                                     #cycle through the items lists
        if i < pivot:                                   #if the the current item is less than the pivot
            small.append(i)                             #add the item to small
        elif i > pivot:                                 #if the item is greater than the pivot,
            big.append(i)                               #add it to the big list
        elif i == pivot:                                #if the item is equal to the pivot
            duplicate.append(i)                         #add it to the duplicate list

    small = quick_sort(small)                           #sort the small list
    big = quick_sort(big)                               #sort the big list

    return small + duplicate + big                      #return the output in order: small, duplicate then big
