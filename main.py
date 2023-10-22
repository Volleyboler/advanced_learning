import datetime
import matplotlib.pyplot as plt
import numpy as np

import application.salary as sa
import application.db.people as pe


if __name__ == '__main__':
    print(datetime.datetime.now())
    sa.calculate_salary()
    pe.get_employees()

    t = np.linspace(0, 2 * np.pi, 100)
    plt.figure(figsize=(4, 4))
    plt.plot(np.cos(t), np.sin(t))
    plt.show()
