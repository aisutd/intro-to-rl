import argparse
import sys
import numpy as np

import gym
from gym import wrappers, logger

env = gym.make("CartPole-v0")

#   code to create videos of the episodes
outdir = "./recordings"
env = wrappers.Monitor(env, directory=outdir, force=True, uid="", write_upon_reset=False)

def run_episode(params):
    total_reward = 0
    observation = env.reset()
    while True:
        #   apply policy to the observation and return an action
        #   the @ symbol denotes matrix multiplication
        if param @ observation < 0:
            action = 0
        else:
            action = 1
        
        #   this collects all the information given in each step of the environment
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
    #   generate a random policy
    param = np.random.rand(4)
    total_reward = run_episode(param)
    
    #   track the current max reward
    max_reward = max(max_reward, total_reward)

    #   if the max reward is 200 (the highest it can be) the policy is the best policy
    if max_reward >= 200:
        print("Best Policy: ", param)
    
env.close()