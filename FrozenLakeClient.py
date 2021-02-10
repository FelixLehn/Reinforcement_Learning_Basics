import gym
from random import randint
env = gym.make("FrozenLake-v0")
observation = env.reset() 
# env.action_space => Discrete(4) => 0=left, 1=down, 2=right, 3=up
# env.observation_space => Discrete(16) => numbered 4x4 box

pathlist = []
for _ in range(100): # 100 genügend Suchsteps
  env.render() # Zeige das Environment und meine Position an
  # Hier macht evtl. ein time.sleep(0.5) Sinn, um die Steps zu sehen
  # action = env.action_space.sample() # type(action) => <class 'int'>
  action = randint(1,2) # Wir fahren hier mal die runter/rechts Strategie
  pathlist.append(action) # Aktion merken
  observation, reward, done, info = env.step(action) 
  # observation = 0-15 pos, reward = 0.0 or 1.0, done = true / false, info=prob=0.333
  print("Observation=", observation, "Reward=", reward, "Done=", done)
  if reward > 0.0:
    print("GEWINNPFAD: ", pathlist, ", LEN = " , len(pathlist))
    break;

  if done:
    print("TERMINIERT!")
    break

env.render()
observation = env.reset() # shut down
env.close()