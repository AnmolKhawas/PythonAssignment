#try:
#    print('raise exception')
#    raise IndexError
#except IndexError:
#    print('caught exception')

#try:
#    a=10
#    b=20
#    print(a+c)
#    lst=[10,12,34,45]
#    print(lst[5])
#except NameError:
#    print('Name error')
#except IndexError:
#    print('Index error')
#except (NameError,IndexError):
#    print('Multi')
#else:
#    print('No error')
#finally:
#    print('Must call')

#food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
#fifth = []

#for x in food:
#    try:
#        fifth.append(x[4])
#    except:
#        print('Got exception')
   
#print(fifth)


blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]

total_likes = 0

for post in blog_posts:
          total_likes = total_likes + post['Likes']
        
print(total_likes)


#Add exception handling to the get_value() function so that it, if an IndexError exeception occurs because the specified index does not exist, the function returns the keyword None. Do not handle any other types of exceptions.
def get_value(data_list, index):
    return data_list[index]

# Sample list data
my_list = ['a', 'b', 'c']



#Calculate the log base ten of each value in xvals and store the result in a list called solution. Use exception handling to skip any calculations that produce math domain errors.
xvals = (0.8, -0.1, 0.9, -0.1, 0.1, 0.30000000000000004, -0.1, 0.5, 1.0, -0.1, 0.9, 0.9, 0.1, 1.0, 0.2, 0.2, 0.1, 0.9, 0.0, 1.0)
solution = []