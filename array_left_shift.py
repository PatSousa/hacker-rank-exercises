'''
left rotation operation on array of size n. 
Given array of n integers and number d, perform d left rotations on the array.
Print the updated array as a single line of space separated integers
Input: -First line is two space separated integers denoting n and d. 
       -Second line contains array
Constraints: 
1<=n<=10^5
1<=d<=n
1<=ai<=10^6
'''

#TODO: write tests
class ValidationError(ValueError):
    pass


class LeftShifter():

    def __init__(self, *args, **kwargs):
        self.input_array = input_array
        self.n = n 
        self.d = d
        self.verify_inputs()

    def left_shifter(self):
        to_shift = self.input_array[0:self.d]
        to_keep = self.input_array[d:self.n+1]
        final = to_keep + to_shift
        return final

    def verify_inputs(self):
        if any((not isinstance(x, int)) for x in self.input_array + [n] + [d]):
            raise ValidationError
        if 1 >= self.d >= self.n >= 10**5:
            raise ValidationError
        elif len(input_array) >= 10**6:
            raise ValidationError
        else:
            pass

if __name__ == "__main__":
    shifter = LeftShifter(n, d, input_array)
    shifter.verify_inputs()
    shifter.left_shifter()
