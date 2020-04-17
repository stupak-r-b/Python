# ex. => 4.2.1
import numpy as np
print(np.array([int(i[0]) for i in [str(float(i) + 0.5).split(".") for i in input().split(" ")]]))




# ex. => 4.2.2
import numpy as np
x, y = [int(i) for i in input().split(" ")]
print(sum([np.array([int(j)*i for j in input().split(" ")]) for i in range(1, x+1)]))