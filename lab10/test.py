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

def backward_algorithm(observations, states, trans_prob, emit_prob):
    num_obs = len(observations)
    num_states = len(states)

    # Initialize the backward probability matrix
    bwd = np.zeros((num_states, num_obs))

    # Base case (t=T-1)
    bwd[:, -1] = 1

    # Recursion for t < T-1
    for t in range(num_obs - 2, -1, -1):
        for s in range(num_states):
            bwd[s, t] = sum(trans_prob[s, s_next] * emit_prob[s_next, observations[t + 1]] * bwd[s_next, t + 1] for s_next in range(num_states))

    return bwd

def stationary_distribution(trans_prob):
    # Calculate stationary distribution
    eigvals, eigvecs = np.linalg.eig(trans_prob.T)
    stationary = eigvecs[:, np.isclose(eigvals, 1)]  # Eigenvector corresponding to eigenvalue 1
    stationary = stationary[:, 0].real  # Take the real part of the eigenvector
    stationary /= stationary.sum()  # Normalize to sum to 1
    return stationary

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

# Run forward and backward algorithms
fwd_probs = forward_algorithm(obs_seq, states, start_prob, trans_prob, emit_prob)
bwd_probs = backward_algorithm(obs_seq, states, trans_prob, emit_prob)

# Normalize probabilities for inference
posterior_probs = (fwd_probs * bwd_probs) / np.sum(fwd_probs * bwd_probs, axis=0)

# Display results
print("Forward Probabilities:")
print(fwd_probs)
print("\nBackward Probabilities:")
print(bwd_probs)
print("\nPosterior Probabilities:")
print(posterior_probs)

# Infer most likely weather condition at each time step
most_likely_states = [states[np.argmax(posterior_probs[:, t])] for t in range(len(obs_seq))]
print("\nMost likely states:", most_likely_states)

# Calculate and display stationary distribution
stationary = stationary_distribution(trans_prob)
print("\nStationary Distribution:")
for state, prob in zip(states, stationary):
    print(f"{state}: {prob:.4f}")
