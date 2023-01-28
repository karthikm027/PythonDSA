def searchInsert(nums, target):
        l = 0
        h = len(nums)-1
        while l <= h:
            print("low is ", l, " high is ", h)
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1


        return l

#print(searchInsert([-1.-3,3,9],0))

# Floyd Warshall Algorithm in python


# The number of vertices
nV = 4

INF = 999


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    print(G)
    print(distance)
    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
#floyd_warshall(G)

def sortedSquares(nums):
        h = len(nums)-1
        l = 0 
        r = [0]*(len(nums))
        print(nums)
        print(r)
        last = h
        while l <= h:
            if pow(nums[l],2) < pow(nums[h],2):
                r[last] = pow(nums[h],2)
                h -= 1
            else:
                r[last] = pow(nums[l],2)
                l += 1
            last -= 1
        return r

#print(sortedSquares([-7,-3,2,3,11]))

def rotate(nums, k):
        current = 0
        l = len(nums)
        p = k % l
        for i in range(k):
            nums[i], nums[l-p] = nums[l-p], nums[i]
            p -= 1
            current += 1
        print(nums)
        print(current)

rotate([1,2,3,4,5,6,7],3)
