"""
Codes for the the section List-based Collections: Arrays in the second post
https://medium.com/@kousukekuzuoka/data-structure-and-algorithms-revisited-part-1-bffbcea48762
"""

def main():
    """
    Main function
    Returns:
    """
    # Create an array with same integer data type
    array = [1, 2, 3, 4, 5]

    # Print out memory location for each element
    for value in array:
        print(memory_location(value))

    # 0x106386080
    # 0x1063860a0
    # 0x1063860c0
    # 0x1063860e0
    # 0x106386100

def memory_location(value):
    """
    Return memory location in string
    Args:
        value: any value to look up memory location for
    Returns:
        str: memory location in hex string
    """
    return hex(id(value))

if __name__ == '__main__':
    main()
