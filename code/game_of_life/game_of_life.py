class GameOfLife(object):
    def start(self, string_field):
        if string_field == "":
            return ""
        parser = GameOfLifeParser()
        field = parser.parse(string_field)
        field_boundaries = self.calc_field_boundaries(field)
        next_field = self.step_calculation(field, field_boundaries)
        res_string = self.convert_to_string(next_field)
        return res_string

    def calc_field_boundaries(self, current_field):
        field_boundaries = {}
        height_field = len(current_field)
        width_field = len(current_field[0])
        field_boundaries["height_field"] = height_field
        field_boundaries["width_field"] = width_field
        return field_boundaries

    def create_empty_field(self, field_boundaries):
        next_field = [[0 for i in range(field_boundaries["width_field"])]
                      for j in range(field_boundaries["height_field"])]
        return next_field

    def step_calculation(self, current_field, field_boundaries):
        next_field = self.create_empty_field(field_boundaries)
        for i in range(field_boundaries["height_field"]):
            for j in range(field_boundaries["width_field"]):
                current_neighbors = self.counting_neighbors(current_field, i, j)
                if current_field[i][j]:
                    if current_neighbors == 2 or current_neighbors == 3:
                        next_field[i][j] = 1
                    else:
                        next_field[i][j] = 0
                else:
                    if current_neighbors == 3:
                        next_field[i][j] = 1
        return next_field

    def counting_neighbors(self, current_field, y, x):
        count = 0
        step = self.calc_border_of_neighbors(current_field, y, x)
        for i in range(y - step["step_back_y"], y + step["step_forward_y"] + 1):
            for j in range(x - step["step_back_x"], x + step["step_forward_x"] + 1):
                if current_field[i][j]:
                    count += 1
        if current_field[y][x]:
            count -= 1
        return count

    def calc_border_of_neighbors(self, current_field, y, x):
        step = {}
        step_back_y = 1
        step_back_x = 1
        step_forward_y = 1
        step_forward_x = 1
        field_boundaries = self.calc_field_boundaries(current_field)
        if y == 0:
            step_back_y = 0
        if x == 0:
            step_back_x = 0
        if y == field_boundaries["height_field"] - 1:
            step_forward_y = 0
        if x == field_boundaries["width_field"] - 1:
            step_forward_x = 0
        step["step_back_y"] = step_back_y
        step["step_back_x"] = step_back_x
        step["step_forward_y"] = step_forward_y
        step["step_forward_x"] = step_forward_x
        return step

    def convert_to_string(self, current_field):
        field_boundaries = self.calc_field_boundaries(current_field)
        string = ""
        for i in range(field_boundaries["height_field"]):
            for j in range(field_boundaries["width_field"]):
                if current_field[i][j]:
                    string += "*"
                else:
                    string += "."
            if i != field_boundaries["height_field"] - 1:
                string += "\n"
        return string


class GameOfLifeParser(object):
    def parse(self, string):
        field_lines = string.split()
        field_boundaries = self.calc_filed_boundaries(field_lines)
        next_field = self.create_empty_field(field_boundaries)
        for i in range(field_boundaries["height_field"]):
            for j in range(field_boundaries["width_field"]):
                if field_lines[i][j] == '.':
                    next_field[i][j] = 0
                elif field_lines[i][j] == '*':
                    next_field[i][j] = 1
                else:
                        msg = "invalid character entered" + ', ' + field_lines[i][j]
                        raise ValueError(msg)
        return next_field

    def string_validation(self, field_lines):
        for field_line in field_lines:
            if len(field_lines[0]) != len(field_line):
                msg = "invalid string entered"
                raise ValueError(msg)

    def calc_filed_boundaries(self, field_lines):
        field_boundaries = {}
        height_field = len(field_lines)
        width_field = len(field_lines[0])
        field_boundaries["height_field"] = height_field
        field_boundaries["width_field"] = width_field
        return field_boundaries

    def create_empty_field(self, field_boundaries):
        next_field = [[0 for i in range(field_boundaries["width_field"])]
                      for j in range(field_boundaries["height_field"])]
        return next_field
