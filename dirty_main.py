import datetime
import matplotlib.pyplot as plt
import numpy as np

from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    print(datetime.datetime.now())
    calculate_salary()
    get_employees()

    t = np.linspace(0, 2 * np.pi, 100)
    plt.figure(figsize=(4, 4))
    plt.plot(np.cos(t), np.sin(t))
    plt.show()
