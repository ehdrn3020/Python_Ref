# The combination of 3*3 magic square is up to eight.
# 마방진 규칙
# The center is a fixed value of 5
# The corners are even
# The numbers attached to 5 are odd
def formingMagicSquare(s):
    pos=[
        [[4,3,8],[9,5,1],[2,7,6]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[8,1,6],[3,5,7],[4,9,2]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[2,7,6],[9,5,1],[4,3,8]],
        [[6,1,8],[7,5,3],[2,9,4]]
    ]

    difflist=[]
    for x in pos:
        diff=0
        for i in range(3):
            for j in range(3):
                diff=diff+abs(s[i][j]-x[i][j])
        difflist.append(diff)

    return min(difflist)