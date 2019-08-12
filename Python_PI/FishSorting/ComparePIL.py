import sys
import math, operator
from PIL import Image
def compare(file1, file2):
    image1 = Image.open("1.jpg")
    image2 = Image.open("3.jpg")
    h1 = image1.histogram()
    h2 = image2.histogram()
    rms = math.sqrt(reduce(operator.add,
                           map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return rms

if __name__=='__main__':
    file1, file2 = sys.argv[1:]
    print(compare(file1, file2))
