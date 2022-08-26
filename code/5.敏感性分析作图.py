import matplotlib.pyplot as plt
import numpy as np


robutness = [0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.02, 1.03, 1.04, 1.05]
a_1_1_4 = [2.6394, 2.6612, 2.6829, 2.7045, 2.7262, 2.7479, 2.7696, 2.7913, 2.8129, 2.8346, 2.8563]
a_1_1_2 = [1.9697, 1.9805, 1.9913, 2.0022, 2.0130, 2.0239, 2.0347, 2.0455, 2.0564, 2.0672, 2.0781]
b_1_1_4 = [28.3544, 28.2514, 28.1484, 28.0454, 27.9424, 27.8394, 27.7365, 27.6335, 27.5305, 27.4275, 27.3245]
b_1_1_2 = [33.5860, 33.5101, 33.4343, 33.3584, 33.2826, 33.2067, 33.1308, 33.0550, 32.9791, 32.9033, 32.8274]

h = np.arange(0,11)


fig, axs = plt.subplots(2, 2)
axs[0,0].set_ylim([0,4])
axs[0,0].plot(h, robutness, label = r"$x_1$",color='tab:pink',marker='D', markersize=4)
axs[0,0].plot(h, a_1_1_2, label = r"$y_1$",color='cornflowerblue',marker='^', markersize=4)
axs[0,0].set_xlabel(r'fluctuate the coefficient of $x_1$')
axs[0,0].set_title(r"(a).$x_1$ = 20, $x_2$ = 1000, $y_1$", fontsize=10)

axs[0,1].set_ylim([0,4])
axs[0,1].plot(h, robutness, label = "Fluctuation factor",color='tab:pink',marker='D', markersize=4)
axs[0,1].plot(h, a_1_1_4, label = "Dependent variable",color='cornflowerblue',marker='^', markersize=4)
axs[0,1].set_xlabel(r'fluctuate the coefficient of $x_1$')
axs[0,1].set_title(r"(b).$x_1$ = 40, $x_2$ = 800, $y_1$", fontsize=10)

axs[1,0].set_ylim([0,35])
axs[1,0].plot(h, robutness, label = "",color='tab:pink',marker='D', markersize=4)
axs[1,0].plot(h, b_1_1_2, label = "",color='cornflowerblue',marker='^', markersize=4)
axs[1,0].set_xlabel(r'fluctuate the coefficient of $y_1$')
axs[1,0].set_title(r"(c).$x_1$ = 20, $x_2$ = 1000, $w_1$", fontsize=10)

axs[1,1].set_ylim([0,35])
axs[1,1].plot(h, robutness, label = "",color='tab:pink',marker='D', markersize=4)
axs[1,1].plot(h, b_1_1_4, label = "",color='cornflowerblue',marker='^', markersize=4)
axs[1,1].set_xlabel(r'fluctuate the coefficient of $y_1$')
axs[1,1].set_title(r"(d).$x_1$ = 40, $x_2$ = 800, $w_1$", fontsize=10)

axs[0,1].legend(loc='upper left', bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)  ##设置ax4中legend的位置，将其放在图外
fig.tight_layout()
plt.show()