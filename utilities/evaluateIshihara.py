def evaluate_ishihara(numbers):
    # Define the Ishihara test results for different color vision deficiencies
    normal_vision = [12, 8, 6, 29, 57, 5, 3, 15, 74, 2, 6, 97, 45, 5, 7, 16, 73, 26, 42, 35]
    deuteranopia = [12, 3, 5, 70, 35, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 3]
    protanopia = [12, 3, 5, 70, 35, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 5]

    # Ensure that the number of test results matches the length of the numbers array
    if len(normal_vision) != len(numbers):
        print("Number of test results doesn't match the length of the input array.")
        return

    # Initialize classification counters
    normal_count = 0
    deuteranopia_count = 0
    protanopia_count = 0

    # Iterate through each number and classify the color vision deficiency
    for i in range(len(numbers)):
        if numbers[i] == normal_vision[i]:
            normal_count += 1
        if numbers[i] == deuteranopia[i]:
            deuteranopia_count += 1
        if numbers[i] == protanopia[i]:
            protanopia_count += 1

    # Determine the classification based on the highest count
    max_count = max(normal_count, deuteranopia_count, protanopia_count)
    if max_count == normal_count:
        return "Regular"
    elif max_count == deuteranopia_count:
        return "deu"
    elif max_count == protanopia_count:
        return "prot"