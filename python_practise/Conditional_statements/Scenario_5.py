# 5. Smart Traffic Light
# You’ve been hired to simulate a smart traffic light system.
# Each light (Red, Yellow, Green) stays on for a different number of seconds. The system repeats this cycle 3 times.
#
# Task:
#
# Simulate the light system using a loop:
#
# Red: 30 seconds
#
# Yellow: 5 seconds
#
# Green: 25 seconds
#
# Print which light is on and for how long — for 3 full cycles.
#
# This one’s about loops, sequences, and control.


def simulate_traffic_light():
    traffic_light = [("Red", 30), ("Yellow", 5), ("Green", 25)]

    for i in range(1, 4):
        print(f"Starting cycle {i}")
        for light, duration in traffic_light:
            print(f"{light} was on for {duration} seconds.")


# Call the function
simulate_traffic_light()
