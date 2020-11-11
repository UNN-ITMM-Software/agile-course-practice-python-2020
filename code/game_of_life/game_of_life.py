class GameOfLife(object):
    def add(self, string):
        if string == "":
            return 0
        parser = GameOfLifeParser()
        field = parser.parse(string)
        height_field = len(field)
        width_field = len(field[0])
        for i in range(height_field):
            for j in range(width_field):
                current_neighbors = self.counting_neighbors(field, i, j)
                if field[i][j]:
                    if current_neighbors == 2 or current_neighbors == 3:
                        field[i][j] = 1
                    else:
                        field[i][j] = 0
                else:
                    if current_neighbors == 3:
                        field[i][j] = 1
        return self.convert_to_string(field)

    def counting_neighbors(self, current_field, y, x):
        count = 0
        step_back_y = 1
        step_back_x = 1
        step_forward_y = 1
        step_forward_x = 1
        height_field = len(current_field)
        width_field = len(current_field[0])
        if y == 0:
            step_back_y = 0
        if x == 0:
            step_back_x = 0
        if y == height_field - 1:
            step_forward_y = 0
        if x == width_field - 1:
            step_forward_x = 0
        for i in range(y - step_back_y, y + step_forward_y + 1):
            for j in range(x - step_back_x, x + step_forward_x + 1):
                if current_field[i][j]:
                    count += 1
        if current_field[y][x]:
            count -= 1
        return count

    def convert_to_string(self, current_field):
        height_field = len(current_field)
        width_field = len(current_field[0])
        string = ""
        for i in range(height_field):
            for j in range(width_field):
                if current_field[i][j]:
                    string += "*"
                else:
                    string += "."
            if i != height_field - 1:
                string += "\n"
        return string


class GameOfLifeParser(object):
    def parse(self, string):
        field_lines = string.split()
        height_field = len(field_lines)
        width_field = len(field_lines[0])
        next_field = [[0 for i in range(width_field)] for j in range(height_field)]
        for i in range(height_field):
            for j in range(width_field):
                if field_lines[i][j] == '.':
                    next_field[i][j] = 0
                else:
                    next_field[i][j] = 1
        return next_field
