#Building a graphic user interface

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]

]
def show_tree():
    for row in picture:
        for pixel in row:
            if (pixel == 1):
                print('*', end='')
            else:
                print(' ', end='')
        print('')
show_tree()
show_tree()

print("My name is The Dave you know")
print("And you know waht?, we are still learning to be great")

