import numpy as np
import gymnasium as gym
import random
import matplotlib.pyplot as plt

#membuat Environment
env = gym.make("FrozenLake-v1", is_slippery=False)

print("Jumlah State :", env.observation_space.n)
print("Jumlah Action :", env.action_space.n)


#inisialisasi Q-Table
state_size = env.observation_space.n
action_size = env.action_space.n

q_table = np.zeros((state_size, action_size))

print(q_table)

#parameter Q-Learning
alpha = 0.8       # learning rate
gamma = 0.95      # discount factor
epsilon = 1.0     # exploration rate

epsilon_decay = 0.995
min_epsilon = 0.01

episodes = 2000
max_steps = 100

#Training
rewards = []

for episode in range(episodes):

    state, info = env.reset()
    total_reward = 0

    for step in range(max_steps):

        # Exploration vs Exploitation
        if random.uniform(0,1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])

        next_state, reward, terminated, truncated, info = env.step(action)

        # Update Q-Table
        q_table[state, action] = q_table[state, action] + alpha * (
            reward + gamma * np.max(q_table[next_state]) - q_table[state, action]
        )

        state = next_state
        total_reward += reward

        if terminated or truncated:
            break

    epsilon = max(min_epsilon, epsilon * epsilon_decay)

    rewards.append(total_reward)

print("Training selesai!")

#menampilkan Q-Table
print("Q-Table Hasil Training")
print(q_table)

#visualisasi reward
plt.figure(figsize=(10,5))
plt.plot(rewards)
plt.title("Reward per Episode")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.grid(True)
plt.show()

#testing agent
env = gym.make("FrozenLake-v1", render_mode="ansi", is_slippery=False)

state, info = env.reset()

done = False
total_reward = 0

while not done:

    action = np.argmax(q_table[state])

    state, reward, terminated, truncated, info = env.step(action)

    print(env.render())

    total_reward += reward

    done = terminated or truncated

print("Total Reward:", total_reward)