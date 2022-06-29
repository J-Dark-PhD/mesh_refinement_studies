import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append("../")
from parametric_values import max_size_range


component_to_test = "lipb_2.2e-3_everything_else"

max_size_range = []
inital_value = 2.2e-3
max_size_range.append(inital_value)
for i in range(1, 15):
    max_size_range.append(inital_value * 0.9**i)

# for value in max_size_range:
#     print("{:.1e}".format(value))

inventory_lipb = []
inventory_structure = []
inventory_baffle = []
inventory_tungsten = []
inventory_pipes = []
max_sizes = []
mesh_sizes = []
sim_times = []

factor = component_to_test + "_max_size"

for size in max_size_range:
    max_sizes.append(size)
    data_folder = "../../data/meshes/mesh_study/Results/{}_{:.1e}/".format(factor, size)
    data = np.genfromtxt(
        data_folder + "derived_quantities.csv", delimiter=",", names=True
    )
    data_sim = np.genfromtxt(data_folder + "sim_data.csv", delimiter=",", names=True)

    inventory_lipb.append(data["Total_solute_volume_6"])
    inventory_structure.append(data["Total_retention_volume_7"])
    inventory_baffle.append(data["Total_retention_volume_8"])
    inventory_tungsten.append(data["Total_retention_volume_9"])
    inventory_pipes.append(
        sum(data["Total_retention_volume_{}".format(i)] for i in range(10, 21))
    )

    mesh_sizes.append(data_sim["cells"])
    sim_times.append(data_sim["sim_time"])

inventory_lipb = np.array(inventory_lipb)
inventory_structure = np.array(inventory_structure)
inventory_baffle = np.array(inventory_baffle)
inventory_tungsten = np.array(inventory_tungsten)
inventory_pipes = np.array(inventory_pipes)
max_cell_sizes = np.array(max_sizes)
mesh_sizes = np.array(mesh_sizes)
sim_times = np.array(sim_times)
# y = np.abs(np.diff(inventories) / np.diff(mesh_sizes))
# standard_value = inventories.min()
reference_value_lipb = inventory_lipb[-1]
reference_value_structure = inventory_structure[-1]
reference_value_baffle = inventory_baffle[-1]
reference_value_tungsten = inventory_tungsten[-1]
reference_value_pipes = inventory_pipes[-1]

# ##### Plotting ##### #

# plt.rc("text", usetex=True)
# plt.rc("font", family="serif", size=12)

plt.figure()
plt.plot(max_sizes, inventory_lipb, marker="x", color="black")
plt.hlines(
    reference_value_lipb * 1.001,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="grey",
    label="0.1%",
)
plt.hlines(
    reference_value_lipb * 0.999,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="grey",
)
plt.hlines(
    reference_value_lipb * 1.005,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="red",
    label="0.5%",
)
plt.hlines(
    reference_value_lipb * 0.995,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="red",
)
# plt.vlines(1.9e-03, reference_value_lipb * 0.995, reference_value_lipb * 1.005)
ax = plt.gca()
ax.invert_xaxis()
ax.set_xscale("log")
ax.set_xlabel("Maximum cell size (m)")
ax.set_xlim(max_sizes[0], max_sizes[-1])
plt.legend()
plt.ylabel("Inventory (H m$^{-3}$)")
plt.title("Lipb")


plt.figure()
plt.plot(max_sizes, inventory_structure, marker="x", color="black")
plt.hlines(
    reference_value_structure * 1.001,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="grey",
    label="0.1%",
)
plt.hlines(
    reference_value_structure * 0.999,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="grey",
)
plt.hlines(
    reference_value_structure * 1.005,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="red",
    label="0.5%",
)
plt.hlines(
    reference_value_structure * 0.995,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="red",
)

ax = plt.gca()
ax.invert_xaxis()
ax.set_xscale("log")
ax.set_xlabel("Maximum cell size (m)")
ax.set_xlim(max_sizes[0], max_sizes[-1])
plt.legend()
plt.ylabel("Inventory (H m$^{-3}$)")
plt.title("Structure")


plt.figure()
plt.plot(max_sizes, inventory_baffle, marker="x", color="black")
plt.hlines(
    reference_value_baffle * 1.001,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="grey",
    label="0.1%",
)
plt.hlines(
    reference_value_baffle * 0.999,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="grey",
)
plt.hlines(
    reference_value_baffle * 1.005,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="red",
    label="0.5%",
)
plt.hlines(
    reference_value_baffle * 0.995,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="red",
)

ax = plt.gca()
ax.invert_xaxis()
ax.set_xscale("log")
ax.set_xlabel("Maximum cell size (m)")
ax.set_xlim(max_sizes[0], max_sizes[-1])
plt.legend()
plt.ylabel("Inventory (H m$^{-3}$)")
plt.title("Baffle plate")


plt.figure()
plt.plot(max_sizes, inventory_tungsten, marker="x", color="black")
plt.hlines(
    reference_value_tungsten * 1.001,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="grey",
    label="0.1%",
)
plt.hlines(
    reference_value_tungsten * 0.999,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="grey",
)
plt.hlines(
    reference_value_tungsten * 1.005,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="red",
    label="0.5%",
)
plt.hlines(
    reference_value_tungsten * 0.995,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="red",
)

ax = plt.gca()
ax.invert_xaxis()
ax.set_xscale("log")
ax.set_xlabel("Maximum cell size (m)")
ax.set_xlim(max_sizes[0], max_sizes[-1])
plt.legend()
plt.ylabel("Inventory (H m$^{-3}$)")
plt.title("First wall")


plt.figure()
plt.plot(max_sizes, inventory_pipes, marker="x", color="black")
plt.hlines(
    reference_value_pipes * 1.001,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="grey",
    label="0.1%",
)
plt.hlines(
    reference_value_pipes * 0.999,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="grey",
)
plt.hlines(
    reference_value_pipes * 1.005,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="red",
    label="0.5%",
)
plt.hlines(
    reference_value_pipes * 0.995,
    max_sizes[0] * 1.1,
    max_sizes[-1] * 0.9,
    linestyles="dashed",
    color="red",
)

ax = plt.gca()
ax.invert_xaxis()
ax.set_xscale("log")
ax.set_xlabel("Maximum cell size (m)")
ax.set_xlim(max_sizes[0], max_sizes[-1])
plt.legend()
plt.ylabel("Inventory (H m$^{-3}$)")
plt.title("BZ Pipes")


plt.show()
