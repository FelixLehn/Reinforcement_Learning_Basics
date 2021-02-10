import gym
from gym import error, spaces, utils
from gym.utils import seeding
from random import randint

# https://github.com/openai/gym/blob/master/docs/creating-environments.md
# Custom Gmy env https://bit.ly/2Uii1vq https://bit.ly/2UnVrBy
# 1D Example https://bit.ly/2L8Pe9G

class EdlEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    env = [-100, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0]  # 12 Elements 0=Bomb, 8=Gold
    pos = randint(0, 11)

    def __init__(self):
        print("EdlEnv initialized.")
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Discrete(12)

    def step(self, action):  # 0 for left and 1 for right for Discrete(2)
        if action == 0:
            action = -1
        self.pos += action

        if self.pos > 11:  # wallbang left
            self.pos = 11
        if self.pos < 0:  # wallbang left
            self.pos = 0

        env_obs = None
        myreward = self.env[self.pos]
        episode_over: bool = True if abs(self.env[self.pos]) == 100 else False
        my_info = None
        return env_obs, myreward, episode_over, my_info

    def reset(self):
        self.env = [-100, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0]
        self.pos = randint(0, 11)

    def render(self, mode='human', close=False):
        print("pos->", self.pos, ";", "env=", self.env)  # TODO Use Curses to display the position



