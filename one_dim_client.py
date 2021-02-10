import gym

env = gym.make('gym_edl:edl-v0')
print("action_space =", env.action_space, " |  observation_space =", env.observation_space)
env.render()
for i in range(10):
	action = env.action_space.sample()
	print("step = ", i, "    action =", action)
	observation, reward, done, info = env.step(action)
	print("Observation =", observation, "| Reward =", reward, "| Done =", done, " | Info =", info)
	if reward == 100:
		print("Found the beer! :-)")
		break
	if reward == -100:
		print("Fell into the hole :-)")
		break
	env.render()
