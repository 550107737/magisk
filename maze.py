import re
import copy


# 0墙，1路，2不可进入点，3可以走通的路，4原来为点阵的点,5pillar,6死路,7最佳路线
class MazeError(Exception):
    pass


class Point(object):
    def __init__(self, x, y, previous):
        self.x = x
        self.y = y
        self.previous = previous


class Maze(object):
    def __init__(self, filename):
        # sys.setrecursionlimit(10000000)
        self.__filename = filename
        self.__mazeCode = readfile(filename)

    def analyse(self):
        get_road_matrix(self.__mazeCode)
        # for i in roadMatrix:
        #     print(*i)
        analyse_roadmatrix()

    def display(self):
        finalStr = ""
        header = "\documentclass[10pt]{article}\n\
\\usepackage{tikz}\n\
\\usetikzlibrary{shapes.misc}\n\
\\usepackage[margin=0cm]{geometry}\n\
\\pagestyle{empty}\n\
\\tikzstyle{every node}=[cross out, draw, red]\n\
\n\
\\begin{document}\n\
\n\
\\vspace*{\\fill}\n\
\\begin{center}\n\
\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n\
% Walls\n"
        ender = "\\end{tikzpicture}\n\
\\end{center}\n\
\\vspace*{\\fill}\n\
\n\
\\end{document}\n"
        finalStr += header
        finalStr += draw_wall()
        finalStr += "% Pillars\n"
        finalStr += draw_pillars()
        finalStr += "% Inner points in accessible cul-de-sacs\n"
        finalStr += draw_cul_de_sacs()
        finalStr += "% Entry-exit paths without intersections\n"
        finalStr += draw_path()
        finalStr += ender
        # print(finalStr)
        f = open(re.sub("txt$", "tex", self.__filename), 'w')
        f.write(finalStr)
        f.close()


gates = []


def draw_path():
    str1 = ""
    for i in range(1, len(roadMatrix), 2):
        line = roadMatrix[i][0::2]
        for m in re.finditer(r"(7)(\1){0,}", "".join(str(n) for n in line)):
            length = m.end() - m.start() - 1
            str1 += "    \\draw[dashed, yellow] (" + str((m.start() * 2 - 1) / 2) + "," + str(i / 2) + ") -- (" + str(
                (m.start() * 2 + length * 2 + 1) / 2) + "," + str(i / 2) + ");\n"
    for j in range(1, len(roadMatrix[0]), 2):
        line = [x[j] for x in roadMatrix[::2]]
        for m in re.finditer(r"(7)(\1){0,}", "".join(str(n) for n in line)):
            length = m.end() - m.start() - 1
            str1 += "    \\draw[dashed, yellow] (" + str(j / 2) + "," + str((m.start() * 2 - 1) / 2) + ") -- (" + str(
                j / 2) + "," + str((m.start() * 2 + length * 2 + 1) / 2) + ");\n"
    # for i in range(1, len(roadMatrix), 2):
    #     for j in range(0, len(roadMatrix[0]), 2):
    #         if roadMatrix[i][j] == 7:
    #             str1 += "\t\\draw[dashed, yellow] (" + str((j - 1) / 2) + "," + str(i / 2) + ") -- (" + str(
    #                 (j + 1) / 2) + "," + str(i / 2) + ");\n"
    # for i in range(0, len(roadMatrix), 2):
    #     for j in range(1, len(roadMatrix[0]), 2):
    #         if roadMatrix[i][j] == 7:
    #             str1 += "\t\\draw[dashed, yellow] (" + str(j / 2) + "," + str((i - 1) / 2) + ") -- (" + str(
    #                 j / 2) + "," + str((i + 1) / 2) + ");\n"
    return str1


def draw_cul_de_sacs():
    str1 = ""
    for i in range(1, len(roadMatrix), 2):
        for j in range(1, len(roadMatrix[0]), 2):
            if roadMatrix[i][j] == 6:
                str1 += "    \\node at (" + str(j / 2) + "," + str(i / 2) + ") {};\n"
    return str1


def draw_pillars():
    pillarStr = ""
    for i in range(0, len(roadMatrix), 2):
        for j in range(0, len(roadMatrix[0]), 2):
            if roadMatrix[i][j] == 5:
                pillarStr += "    \\fill[green] (" + str(j // 2) + "," + str(i // 2) + ") circle(0.2);\n"
    return pillarStr


def draw_wall():
    str1 = ""
    for i in range(0, len(roadMatrix), 2):
        line = roadMatrix[i][1::2]
        for m in re.finditer(r"(0)(\1){0,}", "".join(str(n) for n in line)):
            length = m.end() - m.start()
            str1 += "    \\draw (" + str((m.start())) + "," + str(i // 2) + ") -- (" + str(
                (m.start() + length)) + "," + str(i // 2) + ");\n"
    for j in range(0, len(roadMatrix[0]), 2):
        line = [x[j] for x in roadMatrix[1::2]]
        for m in re.finditer(r"(0)(\1){0,}", "".join(str(n) for n in line)):
            length = m.end() - m.start() - 1
            str1 += "    \\draw (" + str(j // 2) + "," + str((m.start())) + ") -- (" + str(j // 2) + "," + str(
                (m.start() + length + 1)) + ");\n"
    # wallStr = ""
    # for i in range(0, len(roadMatrix), 2):
    #     for j in range(1, len(roadMatrix[0]), 2):
    #         if roadMatrix[i][j] == 0:
    #             wallStr += "\t" + "\\draw(" + str((j - 1) // 2) + "," + str(i // 2) + ") -- (" + str(
    #                 (j + 1) // 2) + "," + str(i // 2) + ");\n"
    # for i in range(1, len(roadMatrix), 2):
    #     for j in range(0, len(roadMatrix[0]), 2):
    #         if roadMatrix[i][j] == 0:
    #             wallStr += "\t\\draw(" + str(j // 2) + "," + str((i - 1) // 2) + ") -- (" + str(j // 2) + "," + str(
    #                 (i + 1) // 2) + ");\n"
    return str1


def find_gate_num():
    for i in range(1, len(roadMatrix), 2):
        if roadMatrix[i][0] == 1:
            gates.append((i, 0))
        if roadMatrix[i][-1] == 1:
            gates.append((i, len(roadMatrix[0]) - 1))
    for j in range(1, len(roadMatrix[0]), 2):
        if roadMatrix[0][j] == 1:
            gates.append((0, j))
        if roadMatrix[-1][j] == 1:
            gates.append((len(roadMatrix) - 1, j))
    return len(gates)


roadMatrix = []
dfs_wall_accessible = []
dfs_access_area_accessible = []
dfs_path_accessible = []
dfs_innerpoint_accessible = []


def dfs_find_wall_num(i, j):
    global roadMatrix, dfs_wall_accessible
    if i < 0 or j < 0 or i > len(dfs_wall_accessible) - 1 or j > len(dfs_wall_accessible[0]) - 1:
        return
    if roadMatrix[i][j] != 0 or dfs_wall_accessible[i][j] == 0:
        return
    dfs_wall_accessible[i][j] = 0
    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dfs_find_wall_num(i + x, j + y)


def find_wall_num():
    global dfs_wall_accessible
    wallSetNum = 0
    dfs_wall_accessible = [[1] * len(roadMatrix[0]) for _ in range(len(roadMatrix))]
    for i in range(len(roadMatrix)):
        for j in range(len(roadMatrix[0])):
            if roadMatrix[i][j] == 0 and dfs_wall_accessible[i][j] == 1:
                dfs_find_wall_num(i, j)
                wallSetNum += 1
    return wallSetNum


def find_real_inaccessable_inner_point(inaccessibleInnerPointNum):
    count = 0
    for i in range(len(roadMatrix)):
        for j in range(len(roadMatrix[0])):
            if roadMatrix[i][j] == 2:
                count += 1
    return (count + inaccessibleInnerPointNum) // 2


def dfs_find_access_area_num(i, j):
    global roadMatrix, dfs_access_area_accessible
    if i < 0 or j < 0 or i > len(dfs_access_area_accessible) - 1 or j > len(dfs_access_area_accessible[0]) - 1:
        return
    if roadMatrix[i][j] != 1 or dfs_access_area_accessible[i][j] == 0:
        return
    dfs_access_area_accessible[i][j] = 0
    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dfs_find_access_area_num(i + x, j + y)


paths = []
path = []


def dfs_find_exit_path(i, j, entryTuple):
    global roadMatrix, dfs_path_accessible, path
    if (i, j) != entryTuple and (i, j) in gates:
        paths.append(path[:])
        return
    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        path.append((i + x, j + y))
        if not (i + x < 0 or j + y < 0 or i + x > len(dfs_path_accessible) - 1 or j + y > len(
                dfs_path_accessible[0]) - 1):
            if roadMatrix[i + x][j + y] == 1 and dfs_path_accessible[i + x][j + y] != 0:
                dfs_path_accessible[i + x][j + y] = 0
                dfs_find_exit_path(i + x, j + y, entryTuple)
                dfs_path_accessible[i + x][j + y] = 1
        path.pop()


def find_accessible_area():
    global dfs_access_area_accessible
    dfs_access_area_accessible = [[1] * len(roadMatrix[0]) for _ in range(len(roadMatrix))]
    num = 0
    for i in range(len(roadMatrix)):
        if roadMatrix[i][0] == 1 and dfs_access_area_accessible[i][0] == 1:
            dfs_find_access_area_num(i, 0)
            num += 1
        if roadMatrix[i][-1] == 1 and dfs_access_area_accessible[i][-1] == 1:
            dfs_find_access_area_num(i, len(roadMatrix[0]) - 1)
            num += 1
    for j in range(len(roadMatrix[0])):
        if roadMatrix[0][j] == 1 and dfs_access_area_accessible[0][j] == 1:
            dfs_find_access_area_num(0, j)
            num += 1
        if roadMatrix[-1][j] == 1 and dfs_access_area_accessible[-1][j]:
            dfs_find_access_area_num(len(roadMatrix) - 1, j)
            num += 1
    return num


def bfs_find_all_path(startTuple):
    global paths
    queue = []
    queue.append(Point(startTuple[0], startTuple[1], None))
    while len(queue) != 0:
        current = queue[0]
        queue.pop(0)
        dfs_path_accessible[current.x][current.y] = 0
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nxt = Point(current.x + x, current.y + y, None)
            if nxt.x < 0 or nxt.y < 0 or nxt.x > len(roadMatrix) - 1 or nxt.y > len(roadMatrix[0]) - 1 or \
                    dfs_path_accessible[nxt.x][nxt.y] == 0 or roadMatrix[nxt.x][nxt.y] != 1:
                continue
            tmp = copy.deepcopy(current)
            nxt.previous = tmp
            dfs_path_accessible[nxt.x][nxt.y] = 0
            if (nxt.x, nxt.y) != startTuple and (nxt.x, nxt.y) in gates:
                path = []
                while nxt.previous != None:
                    path.append((nxt.x, nxt.y))
                    nxt = nxt.previous
                path.append(startTuple)
                paths.append(path[:])
            queue.append(nxt)


"""bfs不适用（无法找全所有路径，）比如
12
34
从1开始，下一层23，当2时会把4访问掉，则到3时无法访问4
会导致死路判断错误
"""


def find_path():
    global paths, dfs_path_accessible, path
    dfs_path_accessible = [[1] * len(roadMatrix[0]) for _ in range(len(roadMatrix))]
    for x, y in gates:
        path.append((x, y))
        dfs_find_exit_path(x, y, (x, y))
        path.pop()
    # bfs
    # for x, y in gates:
    #     dfs_path_accessible = [[1] * len(roadMatrix[0]) for _ in range(len(roadMatrix))]
    #     bfs_find_all_path((x, y))
    return paths


def dfs_find_cul_de_sacs_and_inaccessible_point_num(i, j, color):
    global roadMatrix
    if i < 0 or j < 0 or i > len(roadMatrix) - 1 or j > len(roadMatrix[0]) - 1:
        return
    if roadMatrix[i][j] != 1:
        return
    roadMatrix[i][j] = color
    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dfs_find_cul_de_sacs_and_inaccessible_point_num(i + x, j + y, color)


def get_cul_de_sacs_num(num):
    cul_de_sacs_num = 0
    dic = {}
    for k in range(10, 10 + num):
        flag = 1
        for i in range(len(roadMatrix)):
            for j in range(len(roadMatrix[0])):
                if roadMatrix[i][j] == k:
                    if i == 0 or j == 0 or i == len(roadMatrix) - 1 or j == len(roadMatrix[0]) - 1:
                        cul_de_sacs_num += 1
                        flag = 0
                    else:
                        for x, y in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
                            if roadMatrix[i + x][j + y] == 3:
                                cul_de_sacs_num += 1
                                flag = 0
                                break
                    if flag == 0:
                        if k in dic.keys():
                            break
                        else:
                            dic[k] = 6
                            break
    for k in range(10, 10 + num):
        if k not in dic.keys():
            dic[k] = 2
    for i in range(len(roadMatrix)):
        for j in range(len(roadMatrix[0])):
            if roadMatrix[i][j] in dic.keys():
                roadMatrix[i][j] = dic[roadMatrix[i][j]]
    return cul_de_sacs_num


# 剩下的1不是岔路就是不可入侵点
def find_cul_de_sacs_and_inaccessible_point():
    num = 0
    currentColor = 10
    for i in range(len(roadMatrix)):
        for j in range(len(roadMatrix[0])):
            if roadMatrix[i][j] == 1:
                dfs_find_cul_de_sacs_and_inaccessible_point_num(i, j, currentColor)
                num += 1
                currentColor += 1
    cul_de_sacs_num = get_cul_de_sacs_num(num)
    return cul_de_sacs_num, num - cul_de_sacs_num


def removeDuplicatedPath():
    newPath = []
    for i in paths:
        if i not in newPath:
            if i[::-1] not in newPath:
                newPath.append(i)
    return newPath


def resetMatrixPoint():
    for i in range(0, len(roadMatrix), 2):
        for j in range(0, len(roadMatrix[0]), 2):
            roadMatrix[i][j] = 4


def set_pillar():
    for i in range(len(roadMatrix)):
        for j in range(len(roadMatrix[0])):
            if roadMatrix[i][j] != 4:
                continue
            count = 0
            for x, y in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
                if i + x < 0 or j + y < 0 or i + x > len(roadMatrix) - 1 or j + y > len(roadMatrix[0]) - 1:
                    count += 1
                    continue
                if roadMatrix[i + x][j + y] == 1:
                    count += 1
                else:
                    break
            if count == 8:
                roadMatrix[i][j] = 5


def find_straight_away_path(newPaths):
    dic = {}
    path = []
    for i in newPaths:
        for j in i:
            if j in dic.keys():
                dic[j] += 1
            else:
                dic[j] = 1
    for k, v in dic.items():
        if v == 2:
            path.append(k)
    if not path:
        return False
    finalpath = []
    for i in newPaths:
        if set(i).issubset(set(path)):
            finalpath.append(i)
    return finalpath


def final_print(gateNum, wallSetNum, inaccessibleInnerPointNum, accessibleAreaNum, cul_de_sacs_num, singlePath):
    if gateNum == 0:
        print("The maze has no gate.")
    elif gateNum == 1:
        print("The maze has a single gate.")
    else:
        print("The maze has", gateNum, "gates.")
    if wallSetNum == 0:
        print("The maze has no wall.")
    elif wallSetNum == 1:
        print("The maze has walls that are all connected.")
    else:
        print("The maze has", wallSetNum, "sets of walls that are all connected.")
    if inaccessibleInnerPointNum == 0:
        print("The maze has no inaccessible inner point.")
    elif inaccessibleInnerPointNum == 1:
        print("The maze has a unique inaccessible inner point.")
    else:
        print("The maze has", inaccessibleInnerPointNum, "inaccessible inner points.")
    if accessibleAreaNum == 0:
        print("The maze has no accessible area.")
    elif accessibleAreaNum == 1:
        print("The maze has a unique accessible area.")
    else:
        print("The maze has", accessibleAreaNum, "accessible areas.")
    if cul_de_sacs_num == 0:
        print("The maze has no accessible cul-de-sac.")
    elif cul_de_sacs_num == 1:
        print("The maze has accessible cul-de-sacs that are all connected.")
    else:
        print("The maze has", cul_de_sacs_num, "sets of accessible cul-de-sacs that are all connected.")
    if not singlePath:
        print("The maze has no entry-exit path with no intersection not to cul-de-sacs.")
    elif len(singlePath) // 2 == 1:
        print("The maze has a unique entry-exit path with no intersection not to cul-de-sacs.")
    else:
        print("The maze has", len(singlePath) // 2, "entry-exit paths with no intersections not to cul-de-sacs.")


def analyse_roadmatrix():
    gateNum = find_gate_num()
    wallSetNum = find_wall_num()
    resetMatrixPoint()  # 把原来为点阵的点重新设为点4

    set_pillar()
    accessibleAreaNum = find_accessible_area()
    find_path()  # 寻找所有可行路径
    newPaths = paths  # 路径去重(超时严重，比dfs时间还长，最后直接除2，放弃去重)
    # 把通路设置为3
    for i in newPaths:
        for x, y in i:
            roadMatrix[x][y] = 3
    cul_de_sacs_num, inaccessibleInnerPointFakeNum = find_cul_de_sacs_and_inaccessible_point()
    inaccessibleInnerPointRealNum = find_real_inaccessable_inner_point(inaccessibleInnerPointFakeNum)
    singlePath = find_straight_away_path(newPaths)
    if not type(singlePath) == bool:
        for i in singlePath:
            for x, y in i:
                roadMatrix[x][y] = 7
    final_print(gateNum, wallSetNum, inaccessibleInnerPointRealNum, accessibleAreaNum, cul_de_sacs_num, singlePath)


# 转换为带点和路的矩阵
def get_road_matrix(mazeCode):
    global roadMatrix
    height = len(mazeCode) * 2 - 1  # y轴
    width = len(mazeCode[0]) * 2 - 1  # x轴
    roadMatrix = [[1] * width for _ in range(height)]
    for i in range(len(mazeCode)):
        for j in range(len(mazeCode[0])):
            a = i * 2
            b = j * 2
            if mazeCode[i][j] == '0':
                continue
            elif mazeCode[i][j] == '1':
                roadMatrix[a][b] = 0  # 一横干掉3个点
                roadMatrix[a][b + 1] = 0
                roadMatrix[a][b + 2] = 0
            elif mazeCode[i][j] == '2':
                roadMatrix[a][b] = 0
                roadMatrix[a + 1][b] = 0
                roadMatrix[a + 2][b] = 0
            elif mazeCode[i][j] == '3':
                roadMatrix[a][b] = 0
                roadMatrix[a + 1][b] = 0
                roadMatrix[a + 2][b] = 0
                roadMatrix[a][b + 1] = 0
                roadMatrix[a][b + 2] = 0
    return roadMatrix


def readfile(filename):
    f = open(filename)
    result = []
    for line in f.readlines():  # 依次读取每行
        line = line.strip()  # 去掉每行头尾空白
        if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
            continue  # 是的话，跳过不处理
        if not re.match(r"^[0-3 ]+$", line):
            raise MazeError("Incorrect input.")
        result.append(re.sub(r" +", "", line))
    f.close()
    processInput(result)
    return result


def processInput(inputMatrix):
    height = len(inputMatrix)  # y轴
    width = len(inputMatrix[0])  # x轴
    if not 2 <= width <= 31 or not 2 <= height <= 41:
        raise MazeError("Incorrect input.")
    for i in range(len(inputMatrix)):
        if len(inputMatrix[i]) != width:
            raise MazeError("Incorrect input.")
    for i in range(len(inputMatrix)):
        if not re.match(r"[0-3]+[02]$", inputMatrix[i]):
            raise MazeError("Input does not represent a maze.")
        if i == len(inputMatrix) - 1:
            if not re.match(r"^[01]+[0]$", inputMatrix[i]):
                raise MazeError("Input does not represent a maze.")


def start():
    maze = Maze("maze_11.txt")
    maze.analyse()
    maze.display()


if __name__ == "__main__":
    start()
