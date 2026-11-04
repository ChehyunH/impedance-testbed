import mujoco
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the model and make a data object (the sim's state)
model = mujoco.MjModel.from_xml_path("sim/pendulum.xml")
data = mujoco.MjData(model)

# 2. Start position (rad)
data.qpos[0] = 0.5

# 3. Simulate for 3 s, recording time and angle
times = []
angles = []
while data.time < 3:
    data.ctrl[0] = 0           # torque command
    mujoco.mj_step(model, data)     # advance one timestep
    times.append(data.time)
    angles.append(data.qpos[0])

# 4. Plot
plt.plot(times,angles)
plt.xlabel("Time(s)")
plt.ylabel("Angles(rad)")
plt.title("swing")
plt.grid(True)
plt.show()
