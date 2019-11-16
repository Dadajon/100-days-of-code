def cat_and_mouse(cat_x, cat_y, mouse_z):
    distanceA = abs(cat_x - mouse_z)
    distanceB = abs(cat_y - mouse_z)
    if distanceA > distanceB:
        return 'Cat B'
    elif distanceA == distanceB:
        return 'Mouse C'
    else:
        return 'Cat A'


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])

        result = cat_and_mouse(x, y, z)
        print(result + '\n')