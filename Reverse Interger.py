class Solution(object):
    def reverse(self, x):
        sign =1
        if x <0:
            sign=-1
        str_x = str(abs(x))
        str_x_reversed = "".join(reversed(str_x))
        num_x_reversed = int(str_x_reversed)
        if num_x_reversed > 2147483647:
            return 0
        return num_x_reversed * sign
