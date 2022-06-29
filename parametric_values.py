import numpy as np

# optimised ref values
ref_lipb = 4.4058e21
ref_structure = 2.0400e20
ref_baffle = 1.0916e18
ref_tungsten = 3.5920e17
ref_pipes = 9.4577e18

max_size_range = []
test_list = []
inital_value = 0.005
max_size_range.append(inital_value)
for i in range(1, 28):
    max_size_range.append(inital_value * 0.9**i)

# for value in max_size_range:
# #     print("{:.2e}".format(value))
# print("{:.2e}".format(max_size_range[22]))

component_to_test = "lipb"

# optimised values 0.5%
optimised_5_value = 5.47e-04
optimised_1_value = 3.59e-04

test_list = []
if component_to_test == "everything":
    # define max range
    inital_value = 0.005
    max_size_range.append(inital_value)
    for i in range(1, 28):
        max_size_range.append(inital_value * 0.9**i)
    for value in max_size_range:
        print("{:.2e}".format(value))
    print("coucou")
    # define cell sizes in each volume 
    for size in max_size_range:
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

if component_to_test == "lipb":
    # define max cell size range 
    no_cases = 10
    max_size_range = []
    for i in range(0, no_cases):
        max_size_range.append(np.round(optimised_1_value * 1.1**i, decimals=6))
    
    print(max_size_range)
    # define sizes in each volume
    for size in max_size_range:
        lipb_size = size
        structure_size = optimised_1_value
        baffle_plate_size = optimised_1_value
        tungsten_size = optimised_1_value
        bz_pipe_1_1_size = optimised_1_value
        bz_pipe_1_2_size = optimised_1_value
        bz_pipe_1_3_size = optimised_1_value
        bz_pipe_2_1_size = optimised_1_value
        bz_pipe_2_2_size = optimised_1_value
        bz_pipe_2_3_size = optimised_1_value
        bz_pipe_2_4_size = optimised_1_value
        bz_pipe_3_1_size = optimised_1_value
        bz_pipe_3_2_size = optimised_1_value
        bz_pipe_3_3_size = optimised_1_value
        bz_pipe_3_4_size = optimised_1_value
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


test_list = np.array(test_list)
max_size_range = np.array(max_size_range)
# print(max_size_range)
# print(test_list[2])
