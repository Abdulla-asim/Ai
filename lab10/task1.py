import numpy as np

def forward_algorithm(observations, states, start_prob, trans_prob, emit_prob):
    num_obs = len(observations)
    num_states = len(states)

    # Initialize the forward probability matrix
    fwd = np.zeros((num_states, num_obs))

    # Initialize base case (t=0)
    for s in range(num_states):
        fwd[s, 0] = start_prob[s] * emit_prob[s, observations[0]]

    # Recursion for t > 0
    for t in range(1, num_obs):
        for s in range(num_states):
            fwd[s, t] = sum(fwd[s_prev, t - 1] * trans_prob[s_prev, s] for s_prev in range(num_states)) * emit_prob[s, observations[t]]

    return fwd

def stationary_distribution(states, trans_prob, emit_prob, max_iter=1000, tol=1e-6):
    num_states = len(states)

    # Use a uniform initial probability distribution
    start_prob = np.ones(num_states) / num_states

    # Simulate a long observation sequence with a single dummy observation
    dummy_observation = [0]
    fwd = forward_algorithm(dummy_observation, states, start_prob, trans_prob, emit_prob)

    # Iterate to find stationary distribution
    for _ in range(max_iter):
        next_prob = np.dot(start_prob, trans_prob)
        if np.linalg.norm(next_prob - start_prob) < tol:
            break
        start_prob = next_prob

    return start_prob

# Define states and observations
states = ["Rainy", "Sunny", "Cloudy", "Snowy"]
observations = ["Walk", "Shop", "Clean"]

# Map observations to indices
obs_map = {"Walk": 0, "Shop": 1, "Clean": 2}

# Observation sequence (Walk, Shop, Clean, Walk, Clean)
obs_seq = [obs_map[obs] for obs in ["Walk", "Shop", "Clean", "Walk", "Clean"]]

# Transition probabilities
trans_prob = np.array([
    [0.5, 0.2, 0.2, 0.1],
    [0.1, 0.6, 0.2, 0.1],
    [0.3, 0.3, 0.3, 0.1],
    [0.3, 0.1, 0.1, 0.5]
])

# Emission probabilities
emit_prob = np.array([
    [0.1, 0.4, 0.5],
    [0.6, 0.3, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.1, 0.7]
])

# Initial probabilities
start_prob = np.array([0.2, 0.4, 0.3, 0.1])

# Calculate and display stationary distribution using forward algorithm
stationary_fwd = stationary_distribution(states, trans_prob, emit_prob)
print("\nStationary Distribution (Forward Algorithm Approximation):")
for state, prob in zip(states, stationary_fwd):
    print(f"{state}: {prob:.4f}")
