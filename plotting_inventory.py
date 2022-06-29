import matplotlib.pyplot as plt
import numpy as np
from parametric_values import max_size_range, component_to_test

component_to_test = "lipb"

inventories = []
max_sizes = []
mesh_sizes = []
sim_times = []

factor = component_to_test + "_max_size"

for size in max_size_range:
    max_sizes.append(size)
    data_folder = "../data/meshes/mesh_study/Results/{}_{:.1e}/".format(factor, size)
    data = np.genfromtxt(
        data_folder + "derived_quantities.csv", delimiter=",", names=True
    )
    data_sim = np.genfromtxt(data_folder + "sim_data.csv", delimiter=",", names=True)

    if "lipb" in component_to_test:
        inventory = data["Total_solute_volume_6"]
    elif "structure" in component_to_test:
        inventory = data["Total_retention_volume_7"]
    elif "baffle" in component_to_test:
        inventory = data["Total_retention_volume_8"]
    elif "tungsten" in component_to_test:
        inventory = data["Total_retention_volume_9"]
    elif "pipes" in component_to_test:
        inventory = sum(
            data["Total_retention_volume_{}".format(i)] for i in range(10, 21)
        )

    mesh_sizes.append(data_sim["cells"])
    sim_times.append(data_sim["sim_time"])
    inventories.append(inventory)

inventories = np.array(inventories)
max_cell_sizes = np.array(max_sizes)
mesh_sizes = np.array(mesh_sizes)
sim_times = np.array(sim_times)
# y = np.abs(np.diff(inventories) / np.diff(mesh_sizes))
# standard_value = inventories.min()
standard_value = inventories[-1]

# ##### Plotting ##### #

# plt.rc("text", usetex=True)
# plt.rc("font", family="serif", size=12)

plt.figure()
plt.plot(max_sizes, inventories, marker="x")
plt.hlines(
    standard_value * 1.005,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="grey",
)
plt.ylim(4.390e21, 4.430e21)
plt.vlines(1.4e-3, 0, 3e22)
ax = plt.gca()
ax.invert_xaxis()
ax.set_xscale("log")
ax.set_xlabel("Maximum cell size (m)")
ax.set_xlim(max_sizes[0] * 0.9, max_sizes[-1] * 1.1)
plt.ylabel("Inventory (H m$^{-3}$)")
# plt.xlabel("Mesh size (cells)")
# plt.xlim(mesh_sizes[0] * 0.9, mesh_sizes[-1] * 1.1)

# plt.figure()
# plt.plot(mesh_sizes[:-1], y * sim_times[:-1])
# plt.yscale("log")
# plt.xscale("log")
# plt.ylabel("Derivative of Inventory")
# plt.xlabel("Mesh size (cells)")

# plt.rc("text", usetex=True)
# plt.rc("font", family="serif", size=12)

# plt.figure()
# plt.plot(max_sizes, error_values * 100, marker="x")
# plt.ylabel("Error (%)")
# plt.yscale("log")
# ax = plt.gca()
# ax.invert_xaxis()
# ax.set_xscale("log")
# ax.set_xlabel("Maximum cell size (m)")

# plt.figure()
# plt.loglog(mesh_sizes, error_values * 100, marker="x")
# plt.ylabel("Error (%)")
# plt.xlabel("Mesh size (cells)")

plt.show()
