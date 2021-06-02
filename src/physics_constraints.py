
def calculate_physics_constraints(rocket, *args, **kwargs):
    ## 
    rocket.add_constraint("min_impulse", [1,2])

    ##
    rocket.add_constraint("mass_lims", [1,2])
    
    ##
    rocket.add_constraint("wind_lims", [1,2])

    return (rocket)
