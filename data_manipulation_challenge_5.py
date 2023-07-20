def find_most_frequent_element(elements):
    # Function to find the most frequent element and its frequency in a list
    frequency = {}
    for element in elements:
        frequency[element] = frequency.get(element, 0) + 1

    max_frequency = max(frequency.values())
    most_frequent_elements = [element for element, freq in frequency.items() if freq == max_frequency]

    return most_frequent_elements, max_frequency

def main():
    # Challenge: Find the most frequent element and its frequency in a list
    elements = [1, 2, 3, 2, 4, 2, 5, 3, 6, 2]
    most_frequent_elements, max_frequency = find_most_frequent_element(elements)

    print("List of Elements:", elements)
    if len(most_frequent_elements) == 1:
        print(f"The most frequent element is {most_frequent_elements[0]} with frequency {max_frequency}")
    else:
        print(f"The most frequent elements are {', '.join(map(str, most_frequent_elements))} with frequency {max_frequency}")

if __name__ == "__main__":
    main()
