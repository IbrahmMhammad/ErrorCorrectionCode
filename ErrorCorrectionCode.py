def calc_parity_bits(data, r):
    n = len(data)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(data[-1 * j])
        data = data[:n-(2**i)] + str(val) + data[n-(2**i)+1:]
    return data

def detect_error(code, r):
    n = len(code)
    res = 0
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(code[-1 * j])
        res = res + val*(10**i)
    return int(str(res), 2)

# Example usage
data = '1010101'  # Your data bit string
r = 3  # Number of parity bits, depends on length of data

# Calculate parity bits and encode the data
encoded_data = calc_parity_bits(data, r)
print('Encoded Data:', encoded_data)

# Introduce an error in the encoded data (for testing)
encoded_data = encoded_data[:2] + '0' + encoded_data[3:]  # Introducing an error

# Detect and correct the error
error_position = detect_error(encoded_data, r)
print('Error Position:', error_position)