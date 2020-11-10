class GameOfLife(object):
    def add(self, string):
        if string == "":
            return 0
        parser = GameOfLifeParser()
        field = parser.parse(string)
        height_field = len(field)
        width_field = len(field[0])
        for i in range(width_field):
            for j in range(height_field):
                field[i][j] = 0
        print(field)
        return field


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
