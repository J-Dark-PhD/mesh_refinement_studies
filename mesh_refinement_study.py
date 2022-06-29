from fenics import *
from parametric_values import max_size_range, component_to_test
from temp_3D_slicer import slicer
from solve_navier_stokes import navier_stokes_sim
from solve_h_transport import h_transport_sim_FESTIM

mesh_study = "../data/meshes/mesh_study/"
mesh_folder = "../data/meshes/mesh_study/mesh_files/"
temperature_field_3D = "../data/Results_3D/T.xdmf"

if __name__ == "__main__":
    n = 0
    for size in max_size_range:
        n += 1
        factor = component_to_test + "_max_size"
        print(
            "Running case: {}_{:.1e}, iteration {} of {}".format(
                factor, size, n, len(max_size_range)
            )
        )

        # define mesh to use
        domains_file = mesh_folder + "mesh_domains_{}_{:.1e}.xdmf".format(factor, size)
        boundaries_file = mesh_folder + "mesh_boundaries_{}_{:.1e}.xdmf".format(
            factor, size
        )

        # temperature field slicer
        print("... \nProducing temperature field \n...")
        T_sl = slicer(
            temperature_field_3D=temperature_field_3D,
            mesh_domains_filename=domains_file,
            mesh_boundaries_filename=boundaries_file,
            case="{}_{:.1e}".format(factor, size),
            exports=True,
        )

        # navier stokes sim
        print("... \nProducing velocity field \n...")
        u_full = navier_stokes_sim(
            mesh_domains_filename=domains_file,
            mesh_boundaries_filename=boundaries_file,
            temperature_field=T_sl,
            case="{}_{:.1e}".format(factor, size),
            exports=True,
        )

        # h transport simulation
        print("... \nRunning FESTIM simulation \n...")

        # TODO fix this so accepts the field functions rather than
        #  the file locations

        h_transport_sim_FESTIM(
            mesh_domains_filename=domains_file,
            mesh_boundaries_filename=boundaries_file,
            temperature_field=mesh_study
            + "T_files/T_{}_{:.1e}.xdmf".format(factor, size),
            velocity_field=u_full,
            case="{}_{:.1e}".format(factor, size),
        )
