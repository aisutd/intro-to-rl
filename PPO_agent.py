import argparse
import sys
import numpy as np

import gym
from gym import wrappers, logger

env = gym.make("CartPole-v0")

outdir = "./recordings"
env = wrappers.Monitor(env, directory=outdir, force=True, uid="", write_upon_reset=False)

def run_episode(params):
    total_reward = 0
    observation = env.reset()
    while True:
        if param @ observation < 0:
            action = 0
        else:
            action = 1
        
        observation, reward, done, info = env.step(action)
        total_reward += reward
        env.render()
        if done:
            break

    return total_reward

episode_count = 126
reward = 0
done = False
max_reward = 0

for i in range(episode_count):
    param = np.random.rand(4)
    total_reward = run_episode(param)

    max_reward = max(max_reward, total_reward)

    if max_reward >= 200:
        print("Best Policy: ", param)
    
env.close()