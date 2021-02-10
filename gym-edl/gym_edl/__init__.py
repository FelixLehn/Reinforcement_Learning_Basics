from gym.envs.registration import register

register(
	id='edl-v0',  # pass this to gym.make('gym_edl:edl-v0')
	entry_point='gym_edl.envs:EdlEnv',
)
