class Translator(object):
    @staticmethod
    def num_to_string(num):
        if num == 0:
            return "zero"

        simple_nums_to_str = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen"
        }
        if num in simple_nums_to_str:
            return simple_nums_to_str[num]

        second_placed_nums_to_str = {
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety",
        }

        dig_places = list(map(int, list(str(num))))

        result_str = ""
        for place, dig in enumerate(reversed(dig_places)):
            if place == 0:
                if dig == 0:
                    continue
                result_str += simple_nums_to_str[dig]
            elif place == 1:
                if result_str == "":
                    result_str = second_placed_nums_to_str[dig]
                else:
                    result_str = second_placed_nums_to_str[dig] + "-" + result_str

        return result_str
