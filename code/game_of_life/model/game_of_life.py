class GameOfLife(object):
    @staticmethod
    def string_validation(field):
        for field_line in field:
            if len(field[0]) != len(field_line):
                msg = "invalid string entered"
                raise ValueError(msg)

    @staticmethod
    def calc_field_boundaries(current_field):
        field_boundaries = {}
        height_field = len(current_field)
        width_field = len(current_field[0])
        field_boundaries["height_field"] = height_field
        field_boundaries["width_field"] = width_field
        return field_boundaries

    @staticmethod
    def create_empty_field(field_boundaries):
        empty_field = [[0 for i in range(field_boundaries["width_field"])]
                       for j in range(field_boundaries["height_field"])]
        return empty_field

    def counting_neighbors(self, current_field, y, x):
        count = 0
        step = self.calc_border_of_neighbors(current_field, y, x)
        for i in range(y - step["step_back_y"], y + step["step_forward_y"] + 1):
            for j in range(x - step["step_back_x"], x + step["step_forward_x"] + 1):
                if current_field[i][j]:
                    count += 1
        if current_field[y][x] == 1:
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

    def step_calculation(self, current_field, field_boundaries):
        next_field = self.create_empty_field(field_boundaries)
        for i in range(field_boundaries["height_field"]):
            for j in range(field_boundaries["width_field"]):
                current_neighbors = self.counting_neighbors(current_field, i, j)
                if current_field[i][j] == 1:
                    if current_neighbors == 2 or current_neighbors == 3:
                        next_field[i][j] = 1
                    else:
                        next_field[i][j] = 0
                elif current_field[i][j] == 0:
                    if current_neighbors == 3:
                        next_field[i][j] = 1
        return next_field

    def start(self, field):
        self.string_validation(field)
        field_boundaries = self.calc_field_boundaries(field)
        next_field = self.step_calculation(field, field_boundaries)
        return next_field
