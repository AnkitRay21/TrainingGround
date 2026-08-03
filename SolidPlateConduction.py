import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------
# Plate properties
# ----------------------------------------------------
Lx = 0.2          # Plate width (m)
Ly = 0.1          # Plate height (m)

Nx = 51           # Grid points in x
Ny = 31           # Grid points in y

dx = Lx/(Nx-1)
dy = Ly/(Ny-1)

k = 20.0          # Thermal conductivity (W/m-K)
h = 25.0          # Convective coefficient (W/m2-K)
T_inf = 25.0      # Ambient temperature (°C)

# Initial temperature guess
T = np.ones((Ny, Nx))*100.0

# Convergence parameters
tolerance = 1e-6
max_iter = 20000

# Biot numbers
Bi_x = h*dx/k
Bi_y = h*dy/k

# ----------------------------------------------------
# Gauss-Seidel Iteration
# ----------------------------------------------------
for iteration in range(max_iter):

    T_old = T.copy()

    # Interior nodes
    for j in range(1, Ny-1):
        for i in range(1, Nx-1):

            T[j,i] = (
                (T[j,i+1] + T[j,i-1])*dy**2 +
                (T[j+1,i] + T[j-1,i])*dx**2
            )/(2*(dx**2 + dy**2))

    # -----------------------------------------
    # Left insulated boundary
    # dT/dx = 0
    # -----------------------------------------
    T[:,0] = T[:,1]

    # Right insulated boundary
    T[:,-1] = T[:,-2]

    # -----------------------------------------
    # Bottom convection
    #
    # -k dT/dy = h(T-Tinf)
    # -----------------------------------------
    for i in range(1, Nx-1):
        T[0,i] = (T[1,i] + Bi_y*T_inf)/(1 + Bi_y)

    # -----------------------------------------
    # Top convection
    # -----------------------------------------
    for i in range(1, Nx-1):
        T[-1,i] = (T[-2,i] + Bi_y*T_inf)/(1 + Bi_y)

    # Corners
    T[0,0]     = (T[0,1] + T[1,0]) / 2
    T[0,-1]    = (T[0,-2] + T[1,-1]) / 2
    T[-1,0]    = (T[-1,1] + T[-2,0]) / 2
    T[-1,-1]   = (T[-1,-2] + T[-2,-1]) / 2

    error = np.max(np.abs(T-T_old))

    if error < tolerance:
        print(f'Converged after {iteration} iterations')
        break

# ----------------------------------------------------
# Plot temperature contour
# ----------------------------------------------------
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(8,4))

cp = plt.contourf(X, Y, T, 30, cmap='jet')
plt.colorbar(cp, label='Temperature (°C)')
plt.contour(X, Y, T, colors='k', linewidths=0.4)

plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Steady-State Temperature Distribution')
plt.tight_layout()
plt.show()