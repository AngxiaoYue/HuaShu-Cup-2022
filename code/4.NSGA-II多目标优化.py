from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_problem
from pymoo.core.problem import ElementwiseProblem
from pymoo.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
import time


class MyProblem(ElementwiseProblem):
    def __init__(self):
        super().__init__(n_var=2,   # 变量数
                         n_obj=2,   # 目标数
                         n_constr=6,    # 约束数
                         xl=np.array([20, 800]),     # 变量下界
                         xu=np.array([100, 2000]),   # 变量上界
                         )

    def _evaluate(self, x, out, *args, **kwargs):
        # 定义目标函数
        f1 = (-0.412 * x[0] - 0.014 * x[1] + 55.815)   # x1放在x的第0列，x2放在x的第一列
        f2 = -1 * (-0.538 * x[0] - 0.017 * x[1] + 85.852)
        # 定义约束条件
        g1 = -0.8601 + 0.0542 * x[0] + 0.0018 * x[1] - 3
        g2 = -1 * (-0.8601 + 0.0542 * x[0] + 0.0018 * x[1])
        g3 = -91.4094 + 0.0688 * x[0] + 0.0027 * x[1] + 85
        g4 = 91.4094 - 0.0688 * x[0] - 0.0027 * x[1] - 100
        g5 = 90.3490 + 0.0841 * x[0] + 0.0030 * x[1] - 100
        g6 = -1 * (90.3490 + 0.0841 * x[0] + 0.0030 * x[1])
        # todo
        out["F"] = np.column_stack([f1, f2])
        out["G"] = np.column_stack([g1, g2, g3, g4, g5, g6])

problem = MyProblem()

# 定义遗传算法
algorithm = NSGA2(pop_size=40, n_offsprings=10, elimate_duplicates=False)

res = minimize(problem, algorithm, ('n_gen', 300), verbose=False)

print(res.F)
plt.scatter(res.F[:, 0], res.F[:, 1], marker="o", s=10)
plt.grid(True)
plt.show()

X = res.X
F = res.F
print(X)
xl, xu = problem.bounds()
plt.figure(figsize=(7, 5))
plt.scatter(X[:, 0], X[:, 1], s=30, facecolors='none', edgecolors='r')
plt.xlim(xl[0], xu[0])
plt.ylim(xl[1], xu[1])
plt.title("Design Space")
plt.show()

approx_ideal = F.min(axis=0)
approx_nadir = F.max(axis=0)

nF = (F - approx_ideal) / (approx_nadir - approx_ideal)

fl = nF.min(axis=0)
fu = nF.max(axis=0)

weights = np.array([0.5, 0.5])

from pymoo.decomposition.asf import ASF
decomp = ASF()

i = decomp.do(nF, 1/weights).argmin()

print("Best regarding ASF: Point \ni = %s\nF = %s" % (i, F[i]))
print("Best regarding ASF: Point \ni = %s\nX = %s" % (i, X[i]))

plt.figure(figsize=(7, 5))
for i in range(len(F)):
    F[i][1] = -1 * F[i][1]
plt.scatter(F[:, 0], F[:, 1], s=30, facecolors='none', edgecolors='blue')
plt.scatter(F[i, 0], F[i, 1], marker="x", color="red", s=200)
plt.title("Objective Space")
plt.xlabel(r"Filtration resistance")
plt.ylabel(r"Filtration efficiency")
plt.show()