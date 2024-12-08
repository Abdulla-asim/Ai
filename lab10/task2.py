import numpy as np

# Define states and observations
states = ["Rainy", "Sunny", "Cloudy", "Snowy"]
observations = ["Walk", "Shop", "Clean"]

# Map observations to indices
observations_dict = {"Walk": 0, "Shop": 1, "Clean": 2}

# Observation sequence (Walk, Shop, Clean, Walk, Clean)
obs_seq = [observations_dict[obs] for obs in ["Walk", "Shop", "Clean", "Walk", "Clean"]]

# Initial probabilities
initial_probs = np.array([0.2, 0.4, 0.3, 0.1])

# Transition probabilities
transition_probs = np.array([ # From x To
    [0.5, 0.2, 0.2, 0.1],   
    [0.1, 0.6, 0.2, 0.1],   
    [0.3, 0.3, 0.3, 0.1],   
    [0.3, 0.1, 0.1, 0.5]    
])

# Emission probabilities
emission_probs = np.array([ # States x Observations
    [0.1, 0.4, 0.5],
    [0.6, 0.3, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.1, 0.7]
])


def forward(observations, states, initial_probs, transition_probs, emission_probs):
    num_observations = len(observations)
    num_states = len(states)

    # Initialize the forward probability matrix
    x = np.zeros((num_states, num_observations))

    # Initialize base case (t=0)
    for s in range(num_states):
        x[s, 0] = initial_probs[s] * emission_probs[s, observations[0]]

    # Recursion for t > 0
    for t in range(1, num_observations):
        for s in range(num_states):
            x[s, t] = sum(x[s_prev, t - 1] * transition_probs[s_prev, s] for s_prev in range(num_states)) * emission_probs[s, observations[t]]

    return x

def backward(observations, states, trans_prob, emit_prob):
    num_observations = len(observations)
    num_states = len(states)

    # Initialize the backward probability matrix
    x = np.zeros((num_states, num_observations))

    # Base case (t=T-1)
    x[:, -1] = 1

    # Recursion for t < T-1
    for t in range(num_observations - 2, -1, -1):
        for s in range(num_states):
            x[s, t] = sum(trans_prob[s, s_next] * emit_prob[s_next, observations[t + 1]] * x[s_next, t + 1] for s_next in range(num_states))

    return x

if __name__ == '__main__':
    # Run forward and backward algorithms
    fwd_probs = forward(obs_seq, states, initial_probs, transition_probs, emission_probs)
    bwd_probs = backward(obs_seq, states, transition_probs, emission_probs)

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



