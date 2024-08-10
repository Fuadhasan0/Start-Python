num = input("Enter numbers separated with comma(..,..,..,)\n~ ")
num = list(map(int,num.split(',')))
"""
   * user_input.split(','):

   1. This part takes the string user_input (which is the input provided by the user) and splits it into a list of substrings based on the comma , as a delimiter.
      ~ Example: If the user inputs "9,8,7,3,10", split(',') will break it into a list like ['9', '8', '7', '3', '10'].
      
   * map(int, ...):

   1. The map() function applies the int function to each element in the list created by split().
      This converts each string in the list into an integer.
       ~ Example: The list ['9', '8', '7', '3', '10'] is converted by map(int, ...) to [9, 8, 7, 3, 10], where each element is now an integer.
       
    * list(...):

    1. The map function returns a map object, which is an iterator. To turn this into a regular list, the list(...) function is used.
       ~ Example: list(map(int, ['9', '8', '7', '3', '10'])) will ultimately give [9, 8, 7, 3, 10].
"""
       

max_n = num[0]

for n in num:
       if n > max_n:
              max_n = n
       
print("Max number is", max_n)       