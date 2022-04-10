from qpd_logic.qiskit_logic import play_game


def run(job):
    # print(job)
    # print(type(job))
    gamma = float(job["gamma"])
    theta = float(job["theta"])
    phi = float(job["phi"])

    result = play_game(gamma, theta, phi)
    return result
