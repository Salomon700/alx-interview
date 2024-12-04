
#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island
    Args:
        grid(list): list of list of integers
    Return:
        the perimeter of the island
    """

    param = 0

    for idx in range(len(grid)):
        for j in range(len(grid[idx])):
            if (grid[idx][j] == 1):
                if (idx <= 0 or grid[idx - 1][j] == 0):
                    param += 1
                if (idx >= len(grid) - 1 or grid[idx + 1][j] == 0):
                    param += 1
                if (j <= 0 or grid[idx][j - 1] == 0):
                    param += 1
                if (j >= len(grid[idx]) - 1 or grid[idx][j + 1] == 0):
                    param += 1
    return param
