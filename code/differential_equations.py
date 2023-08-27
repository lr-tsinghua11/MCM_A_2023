import numpy as np
from scipy.integrate import solve_ivp
from datas import matrix_coefficient, genes, rs, sa
# Set the number of populations and some arguments
num_population = 1
lambda_ = 2
# Precipitation data ready
precipitation = np.load("precipitation.npy").reshape(-1)
precipitation = precipitation / precipitation.max() / 2
# Competitive factor and Reproduction capacity data ready
alpha = matrix_coefficient[:num_population, :num_population] / 1.5
rs = [i / 10 for i in rs]
sa = [i / 10 for i in sa]
for x in range(21):
    # Drought frequency (no-drought, once every two years, once every three 
    # years) and severity (precipitation ratio 0.80-1.00)
    eta = 0.8 + 0.01 * x
    # Year i drought
    precipitation[360 * (i - 1):360 *i] = precipitation[360 *
    (i - 1):360 * i] * eta
    # Organic matter accumulation in each year
    f = [1]
    def differential_equations(t, ecosystem):
        # Details of the Interaction Model, including a differential equation 
        #for water content and several differential equations for plants
        total_diff = np.zeros(num_population + 1)
        def h(C, i):
            # Map plant environmental capacity and water content
            return 2 * sa[i] * C - (C ** 2)
        def p(t):
            # Continuous precipitation profile
            t_int = int(t)
            return (precipitation[t_int + 1] - precipitation[t_int])
            * (t - t_int) + precipitation[t_int]
        # number of generation
        n = int(t // 360)
        # Details of (num_population + 1) differential equations 
        total_diff[0] = (p(t) - 0.1) * f[-1] - \
            sum([sa[i] * ecosystem[i + 1] for i in range(num_population)])
        for i in range(num_population):
            total_competition = 0
            for j in range(num_population):
                total_competition += alpha[j][i] * \
                    ecosystem[j + 1] * ecosystem[i + 1]
            total_diff[i + 1] = rs[i] * ecosystem[i + 1] * \
                (1 - ecosystem[i + 1] / genes[i][n] /
                 h(ecosystem[0], i)) - total_competition
        return total_diff
    # Set the initial conditions and time range
    # Simulate population changes during the fisrt years
    y0 = [0.2] + [0.2 / num_population] * num_population
    t_span = [0, 360]
    # Solve the system of differential equations
    sol = solve_ivp(differential_equations, t_span, y0)
    for i in range(4):
        # Simulate population changes during the 2-5 years
        # Water content and Biomass are the same as last year
        y0 = [sol.y[0][-1]]
        for j in range(num_population):
            y0.append(sol.y[j + 1][-1])
        # Calculate the soil fertility factor by remaining
        total_m = sum([sol.y[i + 1][-1] for i in range(num_population)])
        f.append((total_m * lambda_ + f[-1]))
        # Solution for a new year
        t_span = [360 * (i + 1), 360 * (i + 2)]
        sol = solve_ivp(differential_equations, t_span, y0)
    print(f[-1], end=',')
