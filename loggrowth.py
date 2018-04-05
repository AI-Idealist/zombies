# bacterial growth modellingwith boundary
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y, t):
	Ni = y[0]
	f0 = r * Ni * ( 1 - Ni/B) # dit is de afgeleide
	return [f0]

r = 0.5  # groeiratio
B = 1000 # maximale omvang populatie
N0 = 100 # omvang populatie bij start

y0 = [N0]
t  = np.linspace(0, 15., 100) 	
soln = odeint( f, y0, t)
N = soln[:,0]
print(N)
plt.ion()
plt.rcParams['figure.figsize'] = 8, 8
plt.figure()
plt.plot(t, N, label='Bacterieën')
plt.xlabel('tijd (geen eenheid)')
plt.ylabel('populatie')
plt.title('Bacteriegroei met begrenzing')
plt.legend(loc=0)

