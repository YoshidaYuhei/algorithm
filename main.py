import numpy as np
import time
from bigO_examples import ex2 as ex

if __name__ == '__main__':
    array = np.random.randint(0, 30, 10)

    start = time.time()

    print(ex.foo(array))

    print(time.time() - start)
