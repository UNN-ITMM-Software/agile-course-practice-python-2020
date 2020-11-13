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

        result_str = ""
        dig_place_groups = []
        while num:
            dig_place_groups.append(num % 100)
            num //= 100
            dig_place_groups.append(num % 10)
            num //= 10

        group_pred = {
            0: "",
            1: " hundred ",
            2: " thousand ",
            4: " million ",
            6: " billion ",
            8: " trillion ",
            10: " quadrillion ",
            12: " quintillion ",
            14: " sextillion ",
            16: " septillion "
        }

        for group, gnum in enumerate(dig_place_groups):
            if gnum == 0:
                continue
            if group % 2 == 0:
                if gnum in simple_nums_to_str:
                    result_str = simple_nums_to_str[gnum] + group_pred[group] + result_str
                else:
                    result_str = second_placed_nums_to_str[gnum // 10]\
                                 + ("-" + simple_nums_to_str[gnum % 10] if gnum % 10 != 0 else "")\
                                 + group_pred[group] + result_str
            else:
                result_str = simple_nums_to_str[gnum] + group_pred[1] + result_str

        return result_str.rstrip()
