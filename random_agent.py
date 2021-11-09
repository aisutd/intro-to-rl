import argparse
import sys
import numpy as np
from random import randrange

import gym
from gym import wrappers, logger

env = gym.make("CartPole-v0")

outdir = "./recordings"
env = wrappers.Monitor(env, directory=outdir, force=True, uid="", write_upon_reset=False)

def run_episode():
    total_reward = 0
    observation = env.reset()
    while True:
        action = randrange(2)
        
        observation, reward, done, info = env.step(action)
        total_reward += reward

        if done:
            break

    return total_reward

episode_count = 126
reward = 0
done = False
max_reward = 0

for i in range(episode_count):
    total_reward = run_episode()

    max_reward = max(max_reward, total_reward)

print(max_reward)

env.close()