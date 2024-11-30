'''
Name:Anannya Abhi
Date:30/11/24
Python program to that accepts 3 sides for a triangle and checks if it is right-angled or not
'''
#indentation( is important
def right_triangle_or_not(values):
    '''
    function to check right angle triangle
    :param values: list containing sides of a triangle
    :return:Nil
    '''
    hyp=values[2]
    base=values[1]
    altitude=values[0]
    if hyp**2==base**2+altitude**2:
        print("The triangle is right angled triangle")
    else:
        print("The triangle is not a right angled triangle")
values=[]
for i in range(0,3):
    side=float(input("Enter the length of side:"))
    values.append(side)
values.sort()
right_triangle_or_not(values)


