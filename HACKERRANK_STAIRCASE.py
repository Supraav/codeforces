#HACKERRANK STAIRCASE


# Staircase detail
# This is a staircase of size :4

#    #
#   ##
#  ###
# ####

###################################################

# Sample Input

# 6 
# Sample Output

#      #
#     ##
#    ###
#   ####
#  #####
# ######


n= int(input('enter number'))

for i in range(0,n+1):
    for spaces in range(n-i):
        print(' ',end='')
    for hash in range(i):
        print('#',end='')

    print()