def unsafe_add_element(buffer, element, index):
    try:
        buffer[index] = element  # Attempt to set the value at the specified index
        return True
    except IndexError:  # Catch the error if index is out of the buffer's range
        print("Error: Attempting to access index out of range, expanding buffer...")
        while len(buffer) <= index:
            buffer.append('a')  # Expand the buffer to fit the new index
        buffer[index] = element
        return False

# Creating a fixed-size buffer (simulated)
buffer_size = 5
buffer = ['a'] * buffer_size

# Simulating an overflow attempt
index_to_access = 10
element_to_add = 'A'
result = unsafe_add_element(buffer, element_to_add, index_to_access)

print("Buffer after operation:", buffer)
print("Operation status (True for successful, False for adjusted):", result)
