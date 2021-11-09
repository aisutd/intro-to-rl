import argparse
import sys
import numpy as np
from random import randrange

import gym
from gym import wrappers, logger

env = gym.make("CartPole-v0")

#   code to create videos of the episodes
outdir = "./recordings"
env = wrappers.Monitor(env, directory=outdir, force=True, uid="", write_upon_reset=False)

def run_episode():
    total_reward = 0
    observation = env.reset()
    while True:
        #   randomly chooses 0 or 1
        #   0 move the cart left, 1 moves the cart right
        action = randrange(2)
        
        #   this collects all the information given in each step of the environment
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

    #   track the current max reward
    max_reward = max(max_reward, total_reward)

#   the reward has a statistically very very very high chance to never reach 200 as it randomly moves the cart around
print(max_reward)

env.close()