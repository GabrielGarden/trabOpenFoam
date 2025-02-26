import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('OpenFOAMdata/cylinderOpenFOAM/U_0_22_newtonianNoTurb.csv')
data2 = pd.read_csv('OpenFOAMdata/cylinderTurb/U_10_12_newtonianTurb.csv')
data3 = pd.read_csv('OpenFOAMdata/nonNewtOpenFOAM/U_0_02_nonNewtonian.csv')
data4 = pd.read_csv('OpenFOAMdata/nonNewtTurb/U_0_385_nonNewtonianTurb.csv')


# ySimulation = np.linspace(-0.5, 0.5, len(data3['U_2']))


# def analytic(y, newt=None):
#
#     R = 0.5
#     if newt == 1:
#         # hagen-poiseuille flow
#         L = 1
#         # res1 = (6/L**2)*y*(L-y)
#         dp = 0.32
#         mu = 0.01
#         newtonian = dp/(4*mu*L) * (R**2 - y**2)
#         return newtonian
#     elif newt == 0:
#         n = 0.5
#         dpNon = 0.07905
#         k = 0.008838835
#         nonNewtonian = n/(n+1) * (dpNon/(2*k))**(1/n) * (R**((n+1)/n) - y**((n+1)/n))
#         return nonNewtonian
#     else:
#         # hagen-poiseuille flow
#         L = 1
#         res1 = (6 / L ** 2) * y * (L - y)
#         dp = 0.32
#         mu = 0.01
#         newtonian = dp / (4 * mu * L) * (R ** 2 - y ** 2)
#         return newtonian
#
#
# yAnalytic = np.linspace(-0., 0.5, 1001)
# vxAnalytic = analytic(yAnalytic)


# plt.plot(ySimulation, data1["U:2"].to_numpy(), label='Newtonian Laminar')
# plt.plot(ySimulation, data2["U:2"].to_numpy(), label='Newtonian Turbulent')
# plt.plot(ySimulation, data3["U_2"].to_numpy(), label='nonNewtonian Laminar')
# plt.plot(ySimulation, data4["U_2"].to_numpy(), label='nonNewtonian Turbulent')

# plt.plot(yAnalytic, analytic(yAnalytic,1), 'k-.', label='Newtonian Analytic')
# plt.plot(yAnalytic, analytic(yAnalytic, 0), 'k--', label='nonNewtonian Analytic')


def analytic(param='Newtonian'):
    rNewtonianLaminar = np.linspace(data1['Points_1'].min(), data1['Points_1'].max(), 200)
    rNonNewtonianLaminar = np.linspace(data3['Points_1'].min(), data3['Points_1'].max(), 200)
    if param == 'Newtonian':
        dp = 0.015519
        nu = 2.2e-03
        R = 0.5
        res = (1 / (4 * nu)) * dp * (R ** 2 - rNewtonianLaminar ** 2)
        return res, rNewtonianLaminar
    elif param == 'NonNewtonian':
        dp = 0.0001282
        R = 0.5
        k = 1.07e-04
        n = 0.6976
        res = (n / (n + 1)) * ((dp / (2 * k)) ** (1 / n)) * (R ** ((n + 1) / n)) * (
                    1 - (np.abs(rNonNewtonianLaminar) / R) ** ((n + 1) / n))
        return res, rNonNewtonianLaminar


UzNewtonian, rNewtoninan = analytic('Newtonian')
UzNonNewtonian, rNonNewtonian = analytic('NonNewtonian')

plt.figure()
plt.plot(data1["U_2"], data1['Points_1'], 'b.', label='Newtonian Laminar')
# plt.plot(data3["U_2"], data3['Points_1'], 'r.', label='NonNewtonian Laminar')
plt.plot(data2["U_2"], data2['Points_1'], 'r.', label='Newtonian Turbulent')
plt.plot(UzNewtonian, rNewtoninan, 'k-', label='Newtonian Analytic')
# plt.plot(UzNonNewtonian, rNonNewtonian, 'k-', label='NonNewtonian Analytic')
plt.grid(True)
plt.legend()
# plt.xlim(-0, 0.5)
# plt.ylim(0)
plt.ylabel('U [m/s]')
plt.xlabel('r [m]')
# plt.title('Velocity profile for non Newtonian flow')
# plt.title('Velocity profile for Newtonian flow')
plt.tight_layout()
plt.savefig('newtonianVelocityProfile.pdf', dpi=300)

plt.figure()
plt.plot(data3["U_2"], data3['Points_1'], 'b.', label='NonNewtonian Laminar')
# plt.plot(data2["U_2"], data2['Points_1'], 'b.', label='Newtonian Turbulent')
plt.plot(data4["U_2"], data4['Points_1'], 'r.', label='NonNewtonian Turbulent')
plt.plot(UzNonNewtonian, rNonNewtonian, 'k-', label='NonNewtonian Analytic')
plt.grid(True)
plt.legend()
# plt.xlim(-0, 0.5)
# plt.ylim(0)
plt.ylabel('U [m/s]')
plt.xlabel('r [m]')
# plt.title('Velocity profile for non Newtonian flow')
# plt.title('Velocity profile for Newtonian flow')
plt.tight_layout()
plt.savefig('nonNewtonianVelocityProfile.pdf', dpi=300)

plt.show()
