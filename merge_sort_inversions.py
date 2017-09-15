# Merge sort works by subdividing the the list into two sub-lists,
# sorting them using Merge sort and then merging them back up.
# As the recursive call is made to subdivide each list into a sublist,
# they will eventually reach the size of 1, which is technically a sorted list.
"""
Input Format
The first line contains an integer,d, denoting the number of datasets.
The 2d subsequent lines describe each respective dataset over two lines:
The first line contains an integer, n , denoting the number of elements in the dataset.
The second line contains n space-separated integers describing the respective values of the array.

Output Format
For each of the  datasets, print the number of inversions that must be swapped to sort the dataset on a new line.
"""

# TODO: Implement merge sort
# Count # of iterations
# Run over different instances
import requests
import time

response = requests.get(
    'https://hr-testcases-us-east-1.s3.amazonaws.com/25392/input11.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1505524820&Signature=6Wrsl1d7CBE9dZB%2F1kan%2BHUarEY%3D&response-content-type=text%2Fplain')

new_response = response.text.split('\n')
n = new_response[0]
siz_arr = new_response[1::2]
arr = new_response[2::2]


def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print f.__name__, 'took', end - start, 'time'
        return result
    return f_timer


class MergeSort():

    def __init__(self, array):
        self.swaps = long(0)
        self.array = array
        self.mergeSort(self.array)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                self.swaps += (len(left) - i)
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    def mergeSort(self, L):
        if len(L) < 2:
            return L[:]
        else:
            middle = int(len(L) / 2)
            left = self.mergeSort(L[:middle])
            right = self.mergeSort(L[middle:])
            return self.merge(left, right)


# Return number of swaps
@timefunc
def countInversions(arr):
    # Complete this function
    merge_sort = MergeSort(arr)
    return merge_sort.swaps


if __name__ == "__main__":
    t = int(n)
    for a0 in xrange(t):
        n = int(siz_arr[t - 1])
        single_arr = map(int, arr[t - 1].split())
        result = countInversions(single_arr)
        print result
