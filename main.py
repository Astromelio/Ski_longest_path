
with open('map.txt', 'r') as f:
    l = [[int(num) for num in line.split(' ')] for line in f]

dimensiones = l[0]
matrix = l[1:]
MAX = 1500
counter = 0
global value
value = MAX + 1


class Ski_route_optimizer:
    def __init__(self):
        self.path_list = []
        self.dict_path_length = {}
        self.dict_values = {}
        self.dict_val = {}
        self.list_min = 0

    def solve(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dp(y, x, post=False, final_point=False):
            self.dict_val[(y, x)] = {}

            # if counter!=0:
            newY_final = y
            newX_final = x
            if post == True:
                min_value_list = []
            if y < 0 or y >= n or x < 0 or x >= m:
                return 0

            currVal = matrix[y][x]
            res = 0
            list_min = None
            for d in moves:
                dy, dx = d
                newY, newX = y + dy, x + dx
                if (newY >= 0 and newY < n and newX >= 0 and newX < m and matrix[newY][newX] < currVal):
                    if (post == False and final_point == False):
                        res = max(res, dp(newY, newX))

                    if post == True:
                        res_real = dp(newY, newX, post=True)[0]
                        if res_real > res:
                            x_temp = x
                            y_temp = y
                            value = matrix[newY][newX]
                            list_min = (value)

                        res = max(res, res_real)

                    if final_point == True:
                        points = dp(newY, newX, post=True, final_point=True)
                        res = max(res, points[0])
                        route = []
                        route.append(matrix[newY][newX])
            if list_min is not None:
                self.path_list.append(list_min)
            if (post == False and final_point == False):
                return (res + 1)
            elif (post == True):
                # self.dict_val[(y,x)]=(newX_final,newY_final)
                # if res==0:
                #     newY_final = newY
                #     newX_final = newX
                #     value = matrix[newY][newX]
                #     cont = 1
                #     self.path_list2.append(value)
                return (res + 1, newX_final, newY_final, self.path_list)

            # elif (final_point == True):
            #     return (res + 1, newX_final, newY_final, route)

        def max_points_calculator():
            same_length = []
            result = 0
            cambio_total = 0
            for i in range(n):
                for j in range(m):
                    if result < dp(i, j):
                        i_inicial = i
                        j_inicial = j
                        same_length = []
                    elif result == dp(i, j):
                        same_length.append([i, j])

                    result = max(result, dp(i, j))
            same_length.append([i_inicial, j_inicial])
            print(same_length)
            # print(matrix[i_inicial][j_inicial])
            return result, i_inicial, j_inicial, same_length

        # def remove_duplicate:

        def steep_comparing():
            initial_points = max_points_calculator()[3]
            height_losses = []
            final = []
            orders = []
            for i in initial_points:
                result = MAX + 1
                point_x = i[1]
                point_y = i[0]
                # if dp(point_y, point_x, post=True)[3].exists and result < dp(point_y, point_x, post=True)[3]:
                #     finalpoint = dp(point_y, point_x, post=True)
                finalpoint = dp(point_y, point_x, post=True)
                order = set(sorted(finalpoint[3]))
                print(finalpoint)
                initial_height = matrix[point_y][point_x]
                order=sorted(list(order))
                order.append(initial_height)
                order.reverse()
                height_loss = initial_height - min(order)
                height_losses.append(height_loss)
                orders.append(order)
                final.append(finalpoint)
                self.path_list = []

            max_value = max(height_losses)
            max_index = height_losses.index(max_value)
            initial = initial_points[max_index]
            route = orders[max_index]
            total_length = finalpoint[0]
            print(height_losses)

            return (initial, max_value ,route,total_length)

        maximo = steep_comparing()
        return (maximo)


ob = Ski_route_optimizer()

print(ob.solve(matrix))

# def find_track_characteristics:
# def get_length_initial_coordinates:
