import matplotlib.pyplot as plt
import numpy as np

lipb_size = 2.39e-03
structure_size = 1.28e-03
baffle_plate_size = 8.34e-04
tungsten_size = 6.08e-04
bz_pipe_1_1_size = 5.47e-04
bz_pipe_1_2_size = 5.47e-04
bz_pipe_1_3_size = 5.47e-04
bz_pipe_2_1_size = 5.47e-04
bz_pipe_2_2_size = 5.47e-04
bz_pipe_2_3_size = 5.47e-04
bz_pipe_2_4_size = 5.47e-04
bz_pipe_3_1_size = 5.47e-04
bz_pipe_3_2_size = 5.47e-04
bz_pipe_3_3_size = 5.47e-04
bz_pipe_3_4_size = 5.47e-04

alt_list = np.linspace(1, 2, num=4)

lipb_range = lipb_size * alt_list
structure_range = structure_size * alt_list
baffle_range = baffle_plate_size * alt_list
tungsten_range = tungsten_size * alt_list
pipes_range = bz_pipe_1_1_size * alt_list

component_to_test = "everything_optimised"

inventory_lipb = []
inventory_structure = []
inventory_baffle = []
inventory_tungsten = []
inventory_pipes = []
max_sizes = []
mesh_sizes = []
sim_times = []

factor = component_to_test + "_max_size"
max_size_range = alt_list

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

reference_value_lipb = inventory_lipb[-1]
reference_value_structure = inventory_structure[-1]
reference_value_baffle = inventory_baffle[-1]
reference_value_tungsten = inventory_tungsten[-1]
reference_value_pipes = inventory_pipes[-1]

# ##### Plotting ##### #

# plt.rc("text", usetex=True)
# plt.rc("font", family="serif", size=12)

plt.figure()
plt.plot(lipb_range, inventory_lipb, marker="x", color="black")
plt.hlines(
    reference_value_lipb * 1.001,
    lipb_range[0],
    lipb_range[-1],
    linestyles="dashed",
    color="grey",
    label="0.1%",
)
plt.hlines(
    reference_value_lipb * 0.999,
    lipb_range[0],
    lipb_range[-1],
    linestyles="dashed",
    color="grey",
)
plt.hlines(
    reference_value_lipb * 1.005,
    lipb_range[0],
    lipb_range[-1],
    linestyles="dashed",
    color="red",
    label="0.5%",
)
plt.hlines(
    reference_value_lipb * 0.995,
    lipb_range[0],
    lipb_range[-1],
    linestyles="dashed",
    color="red",
)
# plt.scatter(max_sizes[8], inventory_lipb[8], s=150, facecolors="none", edgecolors="red")
# plt.scatter(
#     max_sizes[18], inventory_lipb[18], s=150, facecolors="none", edgecolors="grey"
# )
ax = plt.gca()
ax.invert_xaxis()
# ax.set_xscale("log")
ax.set_xlabel("Maximum cell size (m)")
ax.set_xlim(lipb_range[0], lipb_range[-1])
plt.legend()
plt.ylabel("Inventory (H m$^{-3}$)")
plt.title("Lipb")


plt.figure()
plt.plot(structure_range, inventory_structure, marker="x", color="black")
plt.hlines(
    reference_value_structure * 1.001,
    structure_range[0],
    structure_range[-1],
    linestyles="dashed",
    color="grey",
    label="0.1%",
)
plt.hlines(
    reference_value_structure * 0.999,
    structure_range[0],
    structure_range[-1],
    linestyles="dashed",
    color="grey",
)
plt.hlines(
    reference_value_structure * 1.005,
    structure_range[0],
    structure_range[-1],
    linestyles="dashed",
    color="red",
    label="0.5%",
)
plt.hlines(
    reference_value_structure * 0.995,
    structure_range[0],
    structure_range[-1],
    linestyles="dashed",
    color="red",
)
# plt.scatter(
#     max_sizes[13], inventory_structure[13], s=150, facecolors="none", edgecolors="red"
# )
# plt.scatter(
#     max_sizes[22], inventory_structure[22], s=150, facecolors="none", edgecolors="grey"
# )
ax = plt.gca()
ax.invert_xaxis()
# ax.set_xscale("log")
ax.set_xlabel("Maximum cell size (m)")
ax.set_xlim(structure_range[0], structure_range[-1])
plt.legend()
plt.ylabel("Inventory (H m$^{-3}$)")
plt.title("Structure")


plt.figure()
plt.plot(baffle_range, inventory_baffle, marker="x", color="black")
plt.hlines(
    reference_value_baffle * 1.001,
    baffle_range[0],
    baffle_range[-1],
    linestyles="dashed",
    color="grey",
    label="0.1%",
)
plt.hlines(
    reference_value_baffle * 0.999,
    baffle_range[0],
    baffle_range[-1],
    linestyles="dashed",
    color="grey",
)
plt.hlines(
    reference_value_baffle * 1.005,
    baffle_range[0],
    baffle_range[-1],
    linestyles="dashed",
    color="red",
    label="0.5%",
)
plt.hlines(
    reference_value_baffle * 0.995,
    baffle_range[0],
    baffle_range[-1],
    linestyles="dashed",
    color="red",
)
# plt.scatter(
#     max_sizes[17], inventory_baffle[17], s=150, facecolors="none", edgecolors="red"
# )
# plt.scatter(
#     max_sizes[20], inventory_baffle[20], s=150, facecolors="none", edgecolors="grey"
# )
ax = plt.gca()
ax.invert_xaxis()
# ax.set_xscale("log")
ax.set_xlabel("Maximum cell size (m)")
ax.set_xlim(baffle_range[0], baffle_range[-1])
plt.legend()
plt.ylabel("Inventory (H m$^{-3}$)")
plt.title("Baffle plate")


plt.figure()
plt.plot(tungsten_range, inventory_tungsten, marker="x", color="black")
plt.hlines(
    reference_value_tungsten * 1.001,
    tungsten_range[0],
    tungsten_range[-1],
    linestyles="dashed",
    color="grey",
    label="0.1%",
)
plt.hlines(
    reference_value_tungsten * 0.999,
    tungsten_range[0],
    tungsten_range[-1],
    linestyles="dashed",
    color="grey",
)
plt.hlines(
    reference_value_tungsten * 1.005,
    tungsten_range[0],
    tungsten_range[-1],
    linestyles="dashed",
    color="red",
    label="0.5%",
)
plt.hlines(
    reference_value_tungsten * 0.995,
    tungsten_range[0],
    tungsten_range[-1],
    linestyles="dashed",
    color="red",
)
# plt.scatter(
#     max_sizes[20], inventory_tungsten[20], s=150, facecolors="none", edgecolors="red"
# )
# plt.scatter(
#     max_sizes[25], inventory_tungsten[25], s=150, facecolors="none", edgecolors="grey"
# )
ax = plt.gca()
ax.invert_xaxis()
# ax.set_xscale("log")
ax.set_xlabel("Maximum cell size (m)")
ax.set_xlim(tungsten_range[0], tungsten_range[-1])
plt.legend()
plt.ylabel("Inventory (H m$^{-3}$)")
plt.title("First wall")


plt.figure()
plt.plot(pipes_range, inventory_pipes, marker="x", color="black")
plt.hlines(
    reference_value_pipes * 1.001,
    pipes_range[0],
    pipes_range[-1],
    linestyles="dashed",
    color="grey",
    label="0.1%",
)
plt.hlines(
    reference_value_pipes * 0.999,
    pipes_range[0],
    pipes_range[-1],
    linestyles="dashed",
    color="grey",
)
plt.hlines(
    reference_value_pipes * 1.005,
    pipes_range[0],
    pipes_range[-1],
    linestyles="dashed",
    color="red",
    label="0.5%",
)
plt.hlines(
    reference_value_pipes * 0.995,
    pipes_range[0],
    pipes_range[-1],
    linestyles="dashed",
    color="red",
)
# plt.scatter(
#     max_sizes[21], inventory_pipes[21], s=150, facecolors="none", edgecolors="red"
# )
# plt.scatter(
#     max_sizes[22], inventory_pipes[22], s=150, facecolors="none", edgecolors="grey"
# )
ax = plt.gca()
ax.invert_xaxis()
# ax.set_xscale("log")
ax.set_xlabel("Maximum cell size (m)")
ax.set_xlim(pipes_range[0], pipes_range[-1])
plt.legend()
plt.ylabel("Inventory (H m$^{-3}$)")
plt.title("BZ Pipes")


plt.show()
