from qpd_logic.qiskit_logic import play_game


def run(job):
    """Function converts string values to floats and submits to circuit logic"""
    # print(job)
    # print(type(job))
    gamma = float(job["gamma"])
    theta = float(job["theta"])
    phi = float(job["phi"])
    # qpu = job["qpu"]
    qpu = ""  # placeholder for later; supposed to be used as flag

    result = play_game(gamma, theta, phi, qpu)
    return result
