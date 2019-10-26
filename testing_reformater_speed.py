import timeit
print(timeit.timeit('''
my_triangles = [[3, 5, 6, [255, 0, 0]],
                [13, 8, 2, [255, 255, 0]],
                [2, 2, 2, [255, 0, 255]],
                [6, 5, 5, [0, 0, 0]],
                [7, 6, 5, [255, 255, 255]],
                [3, 6, 5, [0, 0, 255]],
                [3, 4, 7, [255, 0, 0]],
                [8, 1, 8, [0, 255, 255]],
                [2, 51, 0.1, [255, 0, 0]],
                [1, 1, 9, [0, 255, 0]],
                [9, 1, 9, [255, 0, 0]],
                [6, 4, 6, [0, 0, 255],
                [2, 5, 9, [255, 0, 255]],
                [3, 1, 7, [0, 0, 0]],
                [1, 2, 8, [255, 0, 0]],
                [4, 5, 6, [255, 255, 255]],
                [3, 4, 6, [0, 255, 0]],
                [2, 1, 2, [0, 0, 255]],
                [9, 8, 6, [255, 255, 0]],
                [4, 4, 6, [255, 255, 0]],
                [8, 5, 9, [255, 255, 0]],
                [5, 5, 6, [255, 0, 255]]]]

def triangle_list_reformater(list):
    my_triangles_string = str(list)
    translation = my_triangles_string.maketrans({'[':'',']':'',' ':''})
    reformated_comma_trigs_string = my_triangles_string.translate(translation)
    reformated_trigs_string = reformated_comma_trigs_string.split(',')
    reformated_trigs = []
    i = 0
    while i < len(reformated_trigs_string[0::6]):
        a = float(reformated_trigs_string[0::6][i]);
        b = float(reformated_trigs_string[1::6][i]);
        c = float(reformated_trigs_string[2::6][i]);
        red = int(reformated_trigs_string[3::6][i]);
        green = int(reformated_trigs_string[4::6][i]);
        blue = int(reformated_trigs_string[5::6][i]);
        reformated_trigs.append([a, b, c, [red, green, blue]]);
        i += 1;
    return reformated_trigs

triangle_list_reformater(my_triangles)
''' , number=1000))

print(timeit.timeit('''
my_triangles = [[3, 5, 6, [255, 0, 0]],
                [13, 8, 2, [255, 255, 0]],
                [2, 2, 2, [255, 0, 255]],
                [6, 5, 5, [0, 0, 0]],
                [7, 6, 5, [255, 255, 255]],
                [3, 6, 5, [0, 0, 255]],
                [3, 4, 7, [255, 0, 0]],
                [8, 1, 8, [0, 255, 255]],
                [2, 51, 0.1, [255, 0, 0]],
                [1, 1, 9, [0, 255, 0]],
                [9, 1, 9, [255, 0, 0]],
                [6, 4, 6, [0, 0, 255],
                [2, 5, 9, [255, 0, 255]],
                [3, 1, 7, [0, 0, 0]],
                [1, 2, 8, [255, 0, 0]],
                [4, 5, 6, [255, 255, 255]],
                [3, 4, 6, [0, 255, 0]],
                [2, 1, 2, [0, 0, 255]],
                [9, 8, 6, [255, 255, 0]],
                [4, 4, 6, [255, 255, 0]],
                [8, 5, 9, [255, 255, 0]],
                [5, 5, 6, [255, 0, 255]]]]

# Reformating manually (since it's short)
my_reformated_triangles = my_triangles[0:11] + [[my_triangles[11][0],my_triangles[11][1],my_triangles[11][2],my_triangles[11][3]]]+ my_triangles[11][4:]

my_reformated_triangles
''' , number=1000))
