from matplotlib import pyplot as plt
import numpy as np
no_of_students=[22,34,54,34,22]
lang_known=['c','c++','java','python','php']
plt.bar(lang_known,no_of_students)
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
#customize the minor grid
plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')
plt.show
