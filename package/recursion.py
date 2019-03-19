def sum_array( array ):
    '''Return sum of all items in array'''
    if len(array) == 0: #should there be nothing left in the array, return 0
        return 0
    else:  # return the sum of the first element and the sum of the rest of the array
        return array.pop() + sum( array )

def fibonacci( n ):
    '''Return the nth term in fibonacci sequence'''
    if ( n == 1 ) or ( n == 0 ):
        #should n be 1 or 0, no computation should take place
        #we already know the output 0 = 0 ; and 0+1  = 1
        return n
    else:  #return the previous term + the term before it
        return fibonacci( n - 1 ) + fibonacci( n - 2 )

def factorial( n ):
    '''Return n!'''
    if ( n == 1 ) or( n == 0 ): # should n be 1, then use no processing power since 0! and 1! = 1 and
        return 1
    else:
        return n * factorial( n - 1 )

def reverse( word ):
    '''Return word in reverse'''
    if len( word ) == 0: # should the length of the word be 0, return an empty string
        return ''
    else: # add to the returned string, the last letter of the string and the reverse of the reverse
          #of the string excluding the first letter
        return word[-1] + reverse( word[:-1] )
