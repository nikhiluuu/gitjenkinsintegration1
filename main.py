# Python program to find circular tour for a truck

# A petrol pump has petrol and distance to next petrol pump
class petrolPump:
    def __init__(self, petrol, distance):
        self.petrol = petrol
        self.distance = distance


# The function returns starting point if there is a
# possible solution, otherwise returns -1
def printTour(arr, n):
    start = 0

    for i in range(n):

        # Identify the first petrol pump from where we
        # might get a full circular tour
        if arr[i].petrol >= arr[i].distance:
            start = i
            break

    # To store the excess petrol
    curr_petrol = 0
    for i in range(start, n):
        curr_petrol += (arr[i].petrol - arr[i].distance)

        # If at any point remaining petrol is less than 0,
        # it means that we cannot start our journey from
        # current start
        if (curr_petrol < 0):

            # We move to the next petrol pump
            i += 1

            # We try to identify the next petrol pump from
            # where we might get a full circular tour
            while (i < n):
                if (arr[i].petrol >= arr[i].distance):
                    start = i

                    # Reset rem_petrol
                    curr_petrol = 0
                    break
                i += 1

        else:
            # Move to the next petrolpump if curr_petrol is
            # >= 0
            i += 1

    ''' If remaining petrol is less than 0 while we reach the
    first petrol pump, it means no circular tour is
    possible '''
    if (curr_petrol < 0):
        return -1

    for i in range(start):
        curr_petrol += (arr[i].petrol - arr[i].distance)

        ''' If remaining petrol is less than 0 at any point
        before we reach initial start, it means no
        circular tour is possible '''
        if (curr_petrol < 0):
            return -1

    ''' If we have successfully reached intial_start, it
    means can get a circular tour from final_start, hence
    return it '''
    return start


# Driver code
arr = [petrolPump(6, 4), petrolPump(3, 6), petrolPump(7, 3)]
start = printTour(arr, len(arr))
if start == -1:
    print("No solution")
else:
    print("Start = {}".format(start))

# This code is contributed by jainlovely450
