import numpy as np

def generate_normal_4(d, n_samples, fac):
    mean = np.zeros(4)
    
    if fac == 22:
        cov = [[1, d, 0, 0],
               [d, 1, 0, 0],
               [0, 0, 1, d],
               [0, 0, d, 1]]
    if fac == 13:
        cov = [[1, 0, 0, 0],
               [0, 1, d, d],
               [0, d, 1, d],
               [0, d, d, 1]]
    if fac == 4:
        cov = [[1, d, d, d],
               [d, 1, d, d],
               [d, d, 1, d],
               [d, d, d, 1]]
    # Generate the multivariate normal data
    mvn_data = np.random.multivariate_normal(mean, cov, n_samples)

    return mvn_data

def generate_normal_4_check(d, n_samples, fac):
    mean = np.zeros(4)
    
    if fac == '2e':
        cov = [[1, 1, d, d],
               [1, 1, d, d],
               [d, d, 1, 1],
               [d, d, 1, 1]]
    if fac == '2s1e':
        cov = [[1, 1, d, d],
               [1, 1, d, d],
               [d, d, 1, d],
               [d, d, d, 1]]
    if fac == '4s':
        cov = [[1, d, d, d],
               [d, 1, d, d],
               [d, d, 1, d],
               [d, d, d, 1]]
    if fac == '1s1t':
        cov = [[1, 1, 1, d],
               [1, 1, 1, d],
               [1, 1, 1, d],
               [d, d, d, 1]]
    # Generate the multivariate normal data
    mvn_data = np.random.multivariate_normal(mean, cov, n_samples)

    # Generate noise
    noise = np.random.normal(0, 0.1, (n_samples, 4))

    # Add noise to the data
    data_with_noise = mvn_data + noise

    return data_with_noise

def generate_xor_4way(length, n_sample, noise_sample):
    x1 = np.random.uniform(0, length, n_sample).reshape(-1, 1)
    x2 = np.random.uniform(0, length, n_sample).reshape(-1, 1)
    x3 = np.random.uniform(0, length, n_sample).reshape(-1, 1)
    x4 = np.random.uniform(0, length, n_sample).reshape(-1, 1)
    x4[noise_sample:] = (x1[noise_sample:] + x2[noise_sample:] + x3[noise_sample:]) % 3

    data = np.hstack((x1, x2, x3, x4))

    return data

def generate_copy_4way(length, n_sample, noise_sample):
    x = np.random.uniform(0, length, n_sample).reshape(-1, 1)
    x1 = np.random.uniform(0, length, n_sample).reshape(-1, 1)
    x2 = np.random.uniform(0, length, n_sample).reshape(-1, 1)
    x3 = np.random.uniform(0, length, n_sample).reshape(-1, 1)
    x4 = np.random.uniform(0, length, n_sample).reshape(-1, 1)
    
    x1[noise_sample:] = x[noise_sample:]
    x2[noise_sample:] = x[noise_sample:]
    x3[noise_sample:] = x[noise_sample:]
    x4[noise_sample:] = x[noise_sample:]
    
    data = np.hstack((x1, x2, x3, x4))
    return data