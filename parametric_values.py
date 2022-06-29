import numpy as np

max_size_range = []
inital_value = 0.005
max_size_range.append(inital_value)
for i in range(1, 28):
    max_size_range.append(inital_value * 0.9**i)

# for value in max_size_range:
# #     print("{:.2e}".format(value))
# print("{:.2e}".format(max_size_range[22]))

component_to_test = "everything_optimised_1"

# optimised values 0.5%
lipb_size_5 = 2.39e-03
structure_size_5 = 1.28e-03
baffle_plate_size_5 = 8.34e-04
tungsten_size_5 = 6.08e-04
bz_pipe_1_1_size_5 = 5.47e-04
bz_pipe_1_2_size_5 = 5.47e-04
bz_pipe_1_3_size_5 = 5.47e-04
bz_pipe_2_1_size_5 = 5.47e-04
bz_pipe_2_2_size_5 = 5.47e-04
bz_pipe_2_3_size_5 = 5.47e-04
bz_pipe_2_4_size_5 = 5.47e-04
bz_pipe_3_1_size_5 = 5.47e-04
bz_pipe_3_2_size_5 = 5.47e-04
bz_pipe_3_3_size_5 = 5.47e-04
bz_pipe_3_4_size_5 = 5.47e-04

# optimised values 0.1%
lipb_size_1 = 7.50e-04
structure_size_1 = 4.92e-04
baffle_plate_size_1 = 6.08e-04
tungsten_size_1 = 3.59e-04
bz_pipe_1_1_size_1 = 4.92e-04
bz_pipe_1_2_size_1 = 4.92e-04
bz_pipe_1_3_size_1 = 4.92e-04
bz_pipe_2_1_size_1 = 4.92e-04
bz_pipe_2_2_size_1 = 4.92e-04
bz_pipe_2_3_size_1 = 4.92e-04
bz_pipe_2_4_size_1 = 4.92e-04
bz_pipe_3_1_size_1 = 4.92e-04
bz_pipe_3_2_size_1 = 4.92e-04
bz_pipe_3_3_size_1 = 4.92e-04
bz_pipe_3_4_size_1 = 4.92e-04

# standard testing
lipb_size = 0.01
structure_size = 0.01
baffle_plate_size = 0.01
tungsten_size = 0.01
bz_pipe_1_1_size = 0.01
bz_pipe_1_2_size = 0.01
bz_pipe_1_3_size = 0.01
bz_pipe_2_1_size = 0.01
bz_pipe_2_2_size = 0.01
bz_pipe_2_3_size = 0.01
bz_pipe_2_4_size = 0.01
bz_pipe_3_1_size = 0.01
bz_pipe_3_2_size = 0.01
bz_pipe_3_3_size = 0.01
bz_pipe_3_4_size = 0.01

test_list = []
for size in max_size_range:
    if component_to_test == "lipb":
        lipb_size = size
    elif component_to_test == "structure":
        structure_size = size
    elif component_to_test == "baffle":
        baffle_plate_size = size
    elif component_to_test == "tungsten":
        tungsten_size = size
    elif component_to_test == "pipes":
        bz_pipe_1_1_size = size
        bz_pipe_1_2_size = size
        bz_pipe_1_3_size = size
        bz_pipe_2_1_size = size
        bz_pipe_2_2_size = size
        bz_pipe_2_3_size = size
        bz_pipe_2_4_size = size
        bz_pipe_3_1_size = size
        bz_pipe_3_2_size = size
        bz_pipe_3_3_size = size
        bz_pipe_3_4_size = size
    elif component_to_test == "everything":
        lipb_size = size
        structure_size = size
        baffle_plate_size = size
        tungsten_size = size
        bz_pipe_1_1_size = size
        bz_pipe_1_2_size = size
        bz_pipe_1_3_size = size
        bz_pipe_2_1_size = size
        bz_pipe_2_2_size = size
        bz_pipe_2_3_size = size
        bz_pipe_2_4_size = size
        bz_pipe_3_1_size = size
        bz_pipe_3_2_size = size
        bz_pipe_3_3_size = size
        bz_pipe_3_4_size = size
    else:
        continue

    test_list.append(
        [
            lipb_size,
            structure_size,
            baffle_plate_size,
            tungsten_size,
            bz_pipe_1_1_size,
            bz_pipe_1_2_size,
            bz_pipe_1_3_size,
            bz_pipe_2_1_size,
            bz_pipe_2_2_size,
            bz_pipe_2_3_size,
            bz_pipe_2_4_size,
            bz_pipe_3_1_size,
            bz_pipe_3_2_size,
            bz_pipe_3_3_size,
            bz_pipe_3_4_size,
        ]
    )


if component_to_test == "everything_optimised_5":
    case = 1
    max_size_range = []
    optimised_5 = [
        lipb_size_5,
        structure_size_5,
        baffle_plate_size_5,
        tungsten_size_5,
        bz_pipe_1_1_size_5,
        bz_pipe_1_2_size_5,
        bz_pipe_1_3_size_5,
        bz_pipe_2_1_size_5,
        bz_pipe_2_2_size_5,
        bz_pipe_2_3_size_5,
        bz_pipe_2_4_size_5,
        bz_pipe_3_1_size_5,
        bz_pipe_3_2_size_5,
        bz_pipe_3_3_size_5,
        bz_pipe_3_4_size_5,
        case,
    ]
    optimised_5 = np.array(optimised_5)
    alt_list = np.linspace(1, 2, num=3)
    for factor in alt_list:
        test_list.append(np.round(optimised_5 * factor, decimals=5))
        max_size_range.append(optimised_5[-1] * factor)


if component_to_test == "everything_optimised_1":
    case = 1
    max_size_range = []
    optimised_1 = [
        lipb_size_1,
        structure_size_1,
        baffle_plate_size_1,
        tungsten_size_1,
        bz_pipe_1_1_size_1,
        bz_pipe_1_2_size_1,
        bz_pipe_1_3_size_1,
        bz_pipe_2_1_size_1,
        bz_pipe_2_2_size_1,
        bz_pipe_2_3_size_1,
        bz_pipe_2_4_size_1,
        bz_pipe_3_1_size_1,
        bz_pipe_3_2_size_1,
        bz_pipe_3_3_size_1,
        bz_pipe_3_4_size_1,
        case,
    ]
    optimised_1 = np.array(optimised_1)
    alt_list = np.linspace(1, 2, num=4)
    for factor in alt_list:
        test_list.append(np.round(optimised_1 * factor, decimals=5))
        max_size_range.append(optimised_1[-1] * factor)

test_list = np.array(test_list)
# print(max_size_range)
# print(test_list)
