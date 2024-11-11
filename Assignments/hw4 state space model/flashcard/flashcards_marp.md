<!-- Slide 1: Front -->
# Q: What is a State-Space Model (SSM) used for in time series forecasting?  

---

<!-- Slide 1: Back -->
# A: SSMs model time series data by capturing both the system's dynamics and observation uncertainty, using hidden latent states that evolve recursively over time.

---

<!-- Slide 2: Front -->
# Q: What are the two main components of a State-Space Model?  

---

<!-- Slide 2: Back -->
# A: The state equation (process model) and the observation equation (measurement model).

---

<!-- Slide 3: Front -->
# Q: Define the state equation in a State-Space Model.  

---

<!-- Slide 3: Back -->
# A: The state equation describes how the hidden state vector \(X_k\) evolves based on the previous state, inputs, and a noise term, formalized as \( X_{k+1} = f_{	heta_x}(X_k, u_k, \eta_k) \).

---

<!-- Slide 4: Front -->
# Q: What role does the observation equation play in a State-Space Model?  

---

<!-- Slide 4: Back -->
# A: It maps the hidden state vector to the observable data \(Y_k\), modeling how latent dynamics are reflected in measurements, formulated as \( Y_k = g_{	heta_y}(X_k, u_k, \epsilon_k) \).

---

<!-- Slide 5: Front -->
# Q: How do Hidden Markov Models (HMMs) relate to State-Space Models?  

---

<!-- Slide 5: Back -->
# A: HMMs are a specialized type of SSM where hidden states follow a Markov process with discrete possible states, often used for systems with distinct regimes.

---

<!-- Slide 6: Front -->
# Q: What is the state transition matrix \(P\) in an HMM?  

---

<!-- Slide 6: Back -->
# A: \(P\) is a matrix where each element \(p_{ij}\) represents the probability of transitioning from one state to another, maintaining a row-stochastic property.

---

<!-- Slide 7: Front -->
# Q: Describe the role of emission probabilities in an HMM.  

---

<!-- Slide 7: Back -->
# A: Emission probabilities define the likelihood of observing a specific output given a hidden state, organized into an emission matrix.

---

<!-- Slide 8: Front -->
# Q: What is a Linear State-Space Model (LSSM)?  

---

<!-- Slide 8: Back -->
# A: An LSSM uses linear transformations to model time-series data, balancing complexity and tractability, with continuous hidden states linked to outputs through matrix operations.

---

<!-- Slide 9: Front -->
# Q: How is the state equation structured in an LSSM?  

---

<!-- Slide 9: Back -->
# A: It is expressed as \( X_{k+1} = A_k X_k + B_k u_k + \eta_k \), where \( A_k \) and \( B_k \) represent the system dynamics and input effects, respectively.

---

<!-- Slide 10: Front -->
# Q: What is the measurement equation in an LSSM?  

---

<!-- Slide 10: Back -->
# A: The measurement equation relates the state vector to observed data through \( Y_k = C_k X_k + D_k u_k + \epsilon_k \), where \(C_k\) maps latent states to observations.

---

<!-- Slide 11: Front -->
# Q: What is the Markov property in State-Space Models?  

---

<!-- Slide 11: Back -->
# A: The Markov property implies that the system’s future evolution depends solely on the current hidden state, not on the full history of past states.

---

<!-- Slide 12: Front -->
# Q: How is an AR(p) model represented as a Linear State-Space Model (LSSM)?  

---

<!-- Slide 12: Back -->
# A: An AR(p) model can be represented as an LSSM by defining a state vector with lagged values and using a state transition matrix to evolve the state vector over time.

---

<!-- Slide 13: Front -->
# Q: What is the purpose of similarity transformations in LSSMs?  

---

<!-- Slide 13: Back -->
# A: Similarity transformations allow different internal state representations that yield the same input-output behavior, showing that the observable dynamics are invariant under these transformations.

---

<!-- Slide 14: Front -->
# Q: Explain the concept of controllable and observable canonical forms in LSSMs.  

---

<!-- Slide 14: Back -->
# A: Controllable and observable canonical forms are specific configurations of system matrices that simplify analysis, with controllable form focused on input control and observable form on reconstructing states from outputs.

---

<!-- Slide 15: Front -->
# Q: What is the primary goal in parameter identification for LSSMs?  

---

<!-- Slide 15: Back -->
# A: The goal is to estimate system matrices (A, B, C, D) and initial state \(x_0\) to best fit observed input-output data, often using gradient descent.

---

<!-- Slide 16: Front -->
# Q: How does Backpropagation Through Time (BPTT) assist in training LSSMs?  

---

<!-- Slide 16: Back -->
# A: BPTT calculates gradients over sequential data by unrolling dependencies, enabling the optimization of parameters in LSSMs.

---

<!-- Slide 17: Front -->
# Q: What is the primary challenge when using gradient-based methods on LSSMs or RNNs?  

---

<!-- Slide 17: Back -->
# A: The vanishing and exploding gradient problem, often linked to the eigenvalues of the state matrix, which affects stability during training.

---

<!-- Slide 18: Front -->
# Q: Describe the forward pass in the BPTT algorithm for LSSMs.  

---

<!-- Slide 18: Back -->
# A: In the forward pass, the model propagates input through the state-space equations to generate predictions at each time step.

---

<!-- Slide 19: Front -->
# Q: What is a Jacobian tensor in the context of BPTT for LSSMs?  

---

<!-- Slide 19: Back -->
# A: It represents the gradient of state variables with respect to parameters, essential for calculating parameter updates during backpropagation.

---

<!-- Slide 20: Front -->
# Q: How is the total loss function defined in LSSMs during training?  

---

<!-- Slide 20: Back -->
# A: The total loss is the average squared error across time steps, measuring the alignment between predicted and observed outputs over a specified time horizon.

---

