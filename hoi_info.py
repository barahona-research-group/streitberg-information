import numpy as np

def shuffle_data(data, shuffle_indices):
    # Create a copy of the original data to avoid modifying the input in place.
    shuffled_data = data.copy()

    for indices in shuffle_indices:
        # Generate a random permutation for the indices.
        permutation = np.random.permutation(shuffled_data.shape[0])

        # Apply the permutation to the specified indices.
        for idx in indices:
            shuffled_data[:, idx] = shuffled_data[permutation, idx]

    return shuffled_data

# Streitberg_2 is the same as Lancaster_2 and TC_2, as they are equivalent for d=2
def Streitberg_2(X, div_func):
    X_fully_shuffled = shuffle_data(X, [[0]]) 
    p12 = div_func(X, X_fully_shuffled)
    return p12


# this is the same as Lancaster_3, as they are equivalent for d=3
def Streitberg_3(X, div_func):
    X_fully_shuffled = shuffle_data(X, [[0], [1]]) 
    p123 = div_func(X, X_fully_shuffled)
    p23 = div_func(X[:, [1, 2]], X_fully_shuffled[:, [1, 2]])
    p13 = div_func(X[:, [0, 2]], X_fully_shuffled[:, [0, 2]])
    p12 = div_func(X[:, [0, 1]], X_fully_shuffled[:, [0, 1]])
    return p123-p12-p13-p23

def TC_3(X, div_func):
    X_fully_shuffled = shuffle_data(X, [[0], [1]]) 
    p123 = div_func(X, X_fully_shuffled)
    return p123


def Streitberg_4(X, div_func):
    X_fully_shuffled = shuffle_data(X, [[0], [1], [2]])
    p1234 = div_func(X, X_fully_shuffled)
    p1p234 = div_func(X[:,[1, 2, 3]], X_fully_shuffled[:,[1, 2, 3]])
    p2p134 = div_func(X[:,[0, 2, 3]], X_fully_shuffled[:,[0, 2, 3]])
    p3p124 = div_func(X[:,[0, 1, 3]], X_fully_shuffled[:,[0, 1, 3]])
    p4p123 = div_func(X[:,[0, 1, 2]], X_fully_shuffled[:,[0, 1, 2]])
    p12p34 = div_func(shuffle_data(X, [[0, 1]]), X_fully_shuffled)
    p13p24 = div_func(shuffle_data(X, [[0, 2]]), X_fully_shuffled)
    p14p23 = div_func(shuffle_data(X, [[0, 3]]), X_fully_shuffled)
    p1p2p34 = div_func(X[:,[2, 3]], X_fully_shuffled[:,[2, 3]])
    p1p3p24 = div_func(X[:,[1, 3]], X_fully_shuffled[:,[1, 3]])
    p1p4p23 = div_func(X[:,[1, 2]], X_fully_shuffled[:,[1, 2]])
    p2p3p14 = div_func(X[:,[0, 3]], X_fully_shuffled[:,[0, 3]])
    p2p4p13 = div_func(X[:,[0, 2]], X_fully_shuffled[:,[0, 2]])
    p3p4p12 = div_func(X[:,[0, 1]], X_fully_shuffled[:,[0, 1]])

    streitberg_4 = (p1234 - (p1p234 + p2p134 + p3p124 + p4p123) - (p12p34 + p13p24 + p14p23)
                    + 2 * (p1p2p34 + p1p3p24 + p1p4p23 + p2p3p14 + p2p4p13 + p3p4p12))

    return streitberg_4

def Lancaster_4(X, div_func):
    n = X.shape[0]
    X_fully_shuffled = shuffle_data(X, [[0], [1], [2]])
    p1234 = div_func(X, X_fully_shuffled)
    
    p1p234 = div_func(X[:,[1, 2, 3]], X_fully_shuffled[:,[1, 2, 3]])
    p2p134 = div_func(X[:,[0, 2, 3]], X_fully_shuffled[:,[0, 2, 3]])
    p3p124 = div_func(X[:,[0, 1, 3]], X_fully_shuffled[:,[0, 1, 3]])
    p4p123 = div_func(X[:,[0, 1, 2]], X_fully_shuffled[:,[0, 1, 2]])
    
    p1p2p34 = div_func(X[:,[2, 3]], X_fully_shuffled[:,[2, 3]])
    p1p3p24 = div_func(X[:,[1, 3]], X_fully_shuffled[:,[1, 3]])
    p1p4p23 = div_func(X[:,[1, 2]], X_fully_shuffled[:,[1, 2]])
    p2p3p14 = div_func(X[:,[0, 3]], X_fully_shuffled[:,[0, 3]])
    p2p4p13 = div_func(X[:,[0, 2]], X_fully_shuffled[:,[0, 2]])
    p3p4p12 = div_func(X[:,[0, 1]], X_fully_shuffled[:,[0, 1]])

    Lancaster_4 = (p1234 - (p1p234 + p2p134 + p3p124 + p4p123)
                    +  (p1p2p34 + p1p3p24 + p1p4p23 + p2p3p14 + p2p4p13 + p3p4p12))

    return Lancaster_4

def TC4(X, div_func):
    n = X.shape[0]
    X_fully_shuffled = shuffle_data(X, [[0], [1], [2]]) 
    p1234 = div_func(X, X_fully_shuffled)
    return p1234


def Streitberg_5(X, div_func):
    X_fully_shuffled = shuffle_data(X, [[0], [1], [2], [3]])
    p12345 = div_func(X, X_fully_shuffled)

    p1p2345 = div_func(X[:, [1, 2, 3, 4]], X_fully_shuffled[:, [1, 2, 3, 4]])
    p2p1345 = div_func(X[:, [0, 2, 3, 4]], X_fully_shuffled[:, [0, 2, 3, 4]])
    p3p1245 = div_func(X[:, [0, 1, 3, 4]], X_fully_shuffled[:, [0, 1, 3, 4]])
    p4p1235 = div_func(X[:, [0, 1, 2, 4]], X_fully_shuffled[:, [0, 1, 2, 4]])
    p5p1234 = div_func(X[:, [0, 1, 2, 3]], X_fully_shuffled[:, [0, 1, 2, 3]])

    p12p345 = div_func(shuffle_data(X, [[0, 1]]), X_fully_shuffled)
    p13p245 = div_func(shuffle_data(X, [[0, 2]]), X_fully_shuffled)
    p14p235 = div_func(shuffle_data(X, [[0, 3]]), X_fully_shuffled)
    p15p234 = div_func(shuffle_data(X, [[0, 4]]), X_fully_shuffled)
    p23p145 = div_func(shuffle_data(X, [[1, 2]]), X_fully_shuffled)
    p24p135 = div_func(shuffle_data(X, [[1, 3]]), X_fully_shuffled)
    p25p134 = div_func(shuffle_data(X, [[1, 4]]), X_fully_shuffled)
    p34p125 = div_func(shuffle_data(X, [[2, 3]]), X_fully_shuffled)
    p35p124 = div_func(shuffle_data(X, [[2, 4]]), X_fully_shuffled)
    p45p123 = div_func(shuffle_data(X, [[3, 4]]), X_fully_shuffled)

    X_1234 = X[:, [0, 1, 2, 3]]
    p12p34p5 = div_func(shuffle_data(X_1234, [[0, 1]]), X_fully_shuffled[:, [0, 1, 2, 3]])
    p13p24p5 = div_func(shuffle_data(X_1234, [[0, 2]]), X_fully_shuffled[:, [0, 1, 2, 3]])
    p14p23p5 = div_func(shuffle_data(X_1234, [[0, 3]]), X_fully_shuffled[:, [0, 1, 2, 3]])
    X_1235 = X[:, [0, 1, 2, 4]]
    p12p35p4 = div_func(shuffle_data(X_1235, [[0, 1]]), X_fully_shuffled[:, [0, 1, 2, 4]])
    p13p25p4 = div_func(shuffle_data(X_1235, [[0, 2]]), X_fully_shuffled[:, [0, 1, 2, 4]])
    p15p23p4 = div_func(shuffle_data(X_1235, [[0, 3]]), X_fully_shuffled[:, [0, 1, 2, 4]])
    X_1245 = X[:, [0, 1, 3, 4]]
    p12p45p3 = div_func(shuffle_data(X_1245, [[0, 1]]), X_fully_shuffled[:, [0, 1, 3, 4]])
    p14p25p3 = div_func(shuffle_data(X_1245, [[0, 2]]), X_fully_shuffled[:, [0, 1, 3, 4]])
    p15p24p3 = div_func(shuffle_data(X_1245, [[0, 3]]), X_fully_shuffled[:, [0, 1, 3, 4]])
    X_1345 = X[:, [0, 2, 3, 4]]
    p13p45p2 = div_func(shuffle_data(X_1345, [[0, 1]]), X_fully_shuffled[:, [0, 2, 3, 4]])
    p14p35p2 = div_func(shuffle_data(X_1345, [[0, 2]]), X_fully_shuffled[:, [0, 2, 3, 4]])
    p15p34p2 = div_func(shuffle_data(X_1345, [[0, 3]]), X_fully_shuffled[:, [0, 2, 3, 4]])
    X_2345 = X[:, [1, 2, 3, 4]]
    p23p45p1 = div_func(shuffle_data(X_2345, [[0, 1]]), X_fully_shuffled[:, [1, 2, 3, 4]])
    p24p35p1 = div_func(shuffle_data(X_2345, [[0, 2]]), X_fully_shuffled[:, [1, 2, 3, 4]])
    p25p34p1 = div_func(shuffle_data(X_2345, [[0, 3]]), X_fully_shuffled[:, [1, 2, 3, 4]])

    p1p2p345 = div_func(X[:, [2, 3, 4]], X_fully_shuffled[:, [2, 3, 4]])
    p1p3p245 = div_func(X[:, [1, 3, 4]], X_fully_shuffled[:, [1, 3, 4]])
    p1p4p235 = div_func(X[:, [1, 2, 4]], X_fully_shuffled[:, [1, 2, 4]])
    p1p5p234 = div_func(X[:, [1, 2, 3]], X_fully_shuffled[:, [1, 2, 3]])
    p2p3p145 = div_func(X[:, [0, 3, 4]], X_fully_shuffled[:, [0, 3, 4]])
    p2p4p135 = div_func(X[:, [0, 2, 4]], X_fully_shuffled[:, [0, 2, 4]])
    p2p5p134 = div_func(X[:, [0, 2, 3]], X_fully_shuffled[:, [0, 2, 3]])
    p3p4p125 = div_func(X[:, [0, 1, 4]], X_fully_shuffled[:, [0, 1, 4]])
    p3p5p124 = div_func(X[:, [0, 1, 3]], X_fully_shuffled[:, [0, 1, 3]])
    p4p5p123 = div_func(X[:, [0, 1, 2]], X_fully_shuffled[:, [0, 1, 2]])

    p1p2p3p45 = div_func(X[:, [3, 4]], X_fully_shuffled[:, [3, 4]])
    p1p2p4p35 = div_func(X[:, [2, 4]], X_fully_shuffled[:, [2, 4]])
    p1p2p5p34 = div_func(X[:, [2, 3]], X_fully_shuffled[:, [2, 3]])
    p1p3p4p25 = div_func(X[:, [1, 4]], X_fully_shuffled[:, [1, 4]])
    p1p3p5p24 = div_func(X[:, [1, 3]], X_fully_shuffled[:, [1, 3]])
    p1p4p5p23 = div_func(X[:, [1, 2]], X_fully_shuffled[:, [1, 2]])
    p2p3p4p15 = div_func(X[:, [0, 4]], X_fully_shuffled[:, [0, 4]])
    p2p3p5p14 = div_func(X[:, [0, 3]], X_fully_shuffled[:, [0, 3]])
    p2p4p5p13 = div_func(X[:, [0, 2]], X_fully_shuffled[:, [0, 2]])
    p3p4p5p12 = div_func(X[:, [0, 1]], X_fully_shuffled[:, [0, 1]])

    s_5 = (p12345 
            - (p1p2345 + p2p1345 + p3p1245 + p4p1235 + p5p1234)
            - (p12p345 + p13p245 + p14p235 + p15p234 + p23p145 + p24p135 + p25p134 + p34p125 + p35p124 + p45p123)
            + 2 * (p1p2p345 + p1p3p245 + p1p4p235 + p1p5p234 + p2p3p145 + p2p4p135 + p2p5p134 + p3p4p125 + p3p5p124 + p4p5p123) 
            + 2 * (p12p34p5 + p13p24p5 + p14p23p5 + p12p35p4 + p13p25p4 + p15p23p4 + p12p45p3 + p14p25p3 + p15p24p3 + p13p45p2 + p14p35p2 + p15p34p2 + p23p45p1 + p24p35p1 + p25p34p1)
            - 6 * (p1p2p3p45 + p1p2p4p35 + p1p2p5p34 + p1p3p4p25 + p1p3p5p24 + p1p4p5p23 + p2p3p4p15 + p2p3p5p14 + p2p4p5p13 + p3p4p5p12)
          )
    return s_5

    
def Lancaster_5(X, div_func):
    X_fully_shuffled = shuffle_data(X, [[0], [1], [2], [3]])
    p12345 = div_func(X, X_fully_shuffled)

    p1p2345 = div_func(X[:, [1, 2, 3, 4]], X_fully_shuffled[:, [1, 2, 3, 4]])
    p2p1345 = div_func(X[:, [0, 2, 3, 4]], X_fully_shuffled[:, [0, 2, 3, 4]])
    p3p1245 = div_func(X[:, [0, 1, 3, 4]], X_fully_shuffled[:, [0, 1, 3, 4]])
    p4p1235 = div_func(X[:, [0, 1, 2, 4]], X_fully_shuffled[:, [0, 1, 2, 4]])
    p5p1234 = div_func(X[:, [0, 1, 2, 3]], X_fully_shuffled[:, [0, 1, 2, 3]])

    p1p2p345 = div_func(X[:, [2, 3, 4]], X_fully_shuffled[:, [2, 3, 4]])
    p1p3p245 = div_func(X[:, [1, 3, 4]], X_fully_shuffled[:, [1, 3, 4]])
    p1p4p235 = div_func(X[:, [1, 2, 4]], X_fully_shuffled[:, [1, 2, 4]])
    p1p5p234 = div_func(X[:, [1, 2, 3]], X_fully_shuffled[:, [1, 2, 3]])
    p2p3p145 = div_func(X[:, [0, 3, 4]], X_fully_shuffled[:, [0, 3, 4]])
    p2p4p135 = div_func(X[:, [0, 2, 4]], X_fully_shuffled[:, [0, 2, 4]])
    p2p5p134 = div_func(X[:, [0, 2, 3]], X_fully_shuffled[:, [0, 2, 3]])
    p3p4p125 = div_func(X[:, [0, 1, 4]], X_fully_shuffled[:, [0, 1, 4]])
    p3p5p124 = div_func(X[:, [0, 1, 3]], X_fully_shuffled[:, [0, 1, 3]])
    p4p5p123 = div_func(X[:, [0, 1, 2]], X_fully_shuffled[:, [0, 1, 2]])

    p1p2p3p45 = div_func(X[:, [3, 4]], X_fully_shuffled[:, [3, 4]])
    p1p2p4p35 = div_func(X[:, [2, 4]], X_fully_shuffled[:, [2, 4]])
    p1p2p5p34 = div_func(X[:, [2, 3]], X_fully_shuffled[:, [2, 3]])
    p1p3p4p25 = div_func(X[:, [1, 4]], X_fully_shuffled[:, [1, 4]])
    p1p3p5p24 = div_func(X[:, [1, 3]], X_fully_shuffled[:, [1, 3]])
    p1p4p5p23 = div_func(X[:, [1, 2]], X_fully_shuffled[:, [1, 2]])
    p2p3p4p15 = div_func(X[:, [0, 4]], X_fully_shuffled[:, [0, 4]])
    p2p3p5p14 = div_func(X[:, [0, 3]], X_fully_shuffled[:, [0, 3]])
    p2p4p5p13 = div_func(X[:, [0, 2]], X_fully_shuffled[:, [0, 2]])
    p3p4p5p12 = div_func(X[:, [0, 1]], X_fully_shuffled[:, [0, 1]])

    Lancaster_5 = (p12345 - (p1p2345 + p2p1345 + p3p1245 + p4p1235 + p5p1234)
                     + (p1p2p345 + p1p3p245 + p1p4p235 + p1p5p234 + p2p3p145 + p2p4p135 + p2p5p134 + p3p4p125 + p3p5p124 + p4p5p123)
                        - (p1p2p3p45 + p1p2p4p35 + p1p2p5p34 + p1p3p4p25 + p1p3p5p24 + p1p4p5p23 + p2p3p4p15 + p2p3p5p14 + p2p4p5p13 + p3p4p5p12))

    return Lancaster_5


def TC_5(X, div_func):
    X_fully_shuffled = shuffle_data(X, [[0], [1], [2], [3]]) 
    p12345 = div_func(X, X_fully_shuffled)
    return p12345                 