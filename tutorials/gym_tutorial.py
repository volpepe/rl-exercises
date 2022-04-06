import gym

if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    # env = gym.make('Breakout-v0')
    env.reset()
    for i_episode in range(20):
        observation = env.reset()
        for t in range(1000):
            env.render()    # Render the frame
            # Step is the most important function in Gym.
            # It receives in input the action to be taken and returns
            # a quadruple (observation, reward, done, info)
            action = env.action_space.sample() # Sample a random action
            observation, reward, done, info = env.step(action) # Execute it, get reward
            if (done):
                print(f"Episode finished after {t+1} time steps")
                break
    env.close()

# Every environment has an action_space and an observation_space
# In this case, the action space is Discrete(2) and the observation space is Box(4,)
# The Discrete space allows for a fixed range of non-negative numbers (either 0 or 1)
# The Box space is an n-dimensional box, so valid observations in this case will be an array of 4 numbers
# More information about what the observations represent can be found in the documentation