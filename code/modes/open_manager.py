def start(ROUNDS=3):
    from . import mode1, detect_direction, mode2, lidar_manager

    mode1()
    detect_direction()
    mode2()
    for rnd in range(int(ROUNDS * 4 - 1)):
        mode1()
        mode2()

        print(rnd, "round has successfully completed. \U0001F6A9")
    mode1(lidar_manager.START_DISTANCE.value)
