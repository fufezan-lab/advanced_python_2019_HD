
def find_dark_color(list_of_colors):
    """Find peaks of darkest color

    Find local minima for a given list of RGB tupel colors. 
    Intensities are defined as local minima of the sum if the 
    sum intensities of the elements in the list before and after 
    are smaller than the peak we want to determine.

    Args:
        list_of_intensities (list of floats or ints): a list of
            tupels

    Returns:
        list of floats: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)
    """
    list_of_sums = []
    list_of_minima = []
    
    for pixel in list_of_colors:
        pixel_sum = 0
        for number in pixel:
            pixel_sum += number
        
        list_of_sums.append(pixel_sum)
    
    for pos, pixel_sum in enumerate(list_of_sums):
        if pos == 0:
            continue
        if pos == len(list_of_colors)-1:
            continue
        if list_of_sums[pos-1] > pixel_sum < list_of_sums[pos+1]:
            list_of_minima.append(list_of_colors[pos])
    
    return list_of_minima
    
