import numpy as np
import gymnasium as gym
import random
import matplotlib.pyplot as plt

def train_taxi_agent(total_episodes):
    #Membuat environment Taxi-v4
    env = gym.make("Taxi-v4")
    
    #Inisialisasi Q-Table dengan nol
    state_size = env.observation_space.n
    action_size = env.action_space.n
    q_table = np.zeros((state_size, action_size))
    
    #Hyperparameters
    learning_rate = 0.8
    #Alpha
    discount_rate = 0.95         
    #Gamma
    epsilon = 1.0                
    #Exploration rate awal
    max_epsilon = 1.0            
    #Batas atas eksplorasi
    min_epsilon = 0.01           
    #Batas bawah eksplorasi
    decay_rate = 0.005           
    #Tingkat penurunan eksplorasi (Epsilon decay)
    
    #Variabel untuk menyimpan hasil
    rewards_all_episodes = []
    avg_rewards_per_100 = []
    
    #Looping Training
    for episode in range(total_episodes):
        #Reset environment di awal episode
        state_info = env.reset()
        state = state_info[0] if isinstance(state_info, tuple) else state_info # Kompatibilitas versi Gym
        
        done = False
        rewards_current_episode = 0
        
        while not done:
            #Eksplorasi vs Eksploitasi
            exploration_rate_threshold = random.uniform(0, 1)
            if exploration_rate_threshold > epsilon:
                #Eksploitasi: Pilih aksi dengan nilai Q terbesar
                action = np.argmax(q_table[state, :])
            else:
                #Eksplorasi: Pilih aksi acak
                action = env.action_space.sample()
                
            #Lakukan aksi
            step_result = env.step(action)
            #Menyesuaikan dengan versi Gym terbaru
            if len(step_result) == 5:
                new_state, reward, done, truncated, info = step_result
                done = done or truncated
            else:
                new_state, reward, done, info = step_result
                
            #Update Q-Table menggunakan Persamaan Bellman
            q_table[state, action] = q_table[state, action] * (1 - learning_rate) + \
                learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))
            
            #Pindah ke state baru
            state = new_state
            rewards_current_episode += reward
            
        #Update nilai Epsilon (mengurangi eksplorasi seiring waktu)
        epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)
        rewards_all_episodes.append(rewards_current_episode)
        
        #Menghitung rata-rata reward setiap 100 episode
        if (episode + 1) % 100 == 0:
            avg_reward = np.mean(rewards_all_episodes[-100:])
            avg_rewards_per_100.append(avg_reward)
            
    env.close()
    return avg_rewards_per_100
    
#Evaluasi dan perbandingan
print("Mulai proses training untuk 1000, 2000, dan 5000 episode...\n")

#Menjalankan training untuk masing-masing target episode
avg_rewards_1000 = train_taxi_agent(1000)
avg_rewards_2000 = train_taxi_agent(2000)
avg_rewards_5000 = train_taxi_agent(5000)

print("Training selesai! Membuat visualisasi grafik...")

#Visualisasi hasil perbandingan
plt.figure(figsize=(12, 6))

'''
Plotting grafik rata-rata reward
plt.plot(range(100, 1001, 100), avg_rewards_1000, label='1000 Episodes', marker='o')
plt.plot(range(100, 2001, 100), avg_rewards_2000, label='2000 Episodes', marker='s')
plt.plot(range(100, 5001, 100), avg_rewards_5000, label='5000 Episodes', marker='^')

Kustomisasi Grafik
plt.title('Perbandingan Rata-rata Reward per 100 Episode (Taxi-v4)')
plt.xlabel('Jumlah Episode')
plt.ylabel('Rata-rata Reward')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
'''

"Tugas soal no 5"
# Plotting data rata-rata reward per 100 episode untuk masing-masing variasi
plt.plot(range(100, 1001, 100), avg_rewards_1000, label='1000 Episodes', marker='o', linewidth=2)
plt.plot(range(100, 2001, 100), avg_rewards_2000, label='2000 Episodes', marker='s', linewidth=2)
plt.plot(range(100, 5001, 100), avg_rewards_5000, label='5000 Episodes', marker='^', linewidth=2)

# Menambahkan elemen dekoratif akademik pada grafik
plt.title('Analisis Perbandingan Performa Agen Q-Learning pada Taxi-v4', fontsize=14, fontweight='bold')
plt.xlabel('Jumlah Episode', fontsize=12)
plt.ylabel('Rata-rata Reward (Per 100 Episode)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=11)

#Menampilkan grafik
plt.tight_layout()
plt.show()