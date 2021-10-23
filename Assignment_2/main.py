from ortools.algorithms import pywrapknapsack_solver
import os
import time


directories = [
    "00Uncorrelated",
    "01WeaklyCorrelated",
    "02StronglyCorrelated",
    "03InverseStronglyCorrelated",
    "04AlmostStronglyCorrelated",
    "05SubsetSum",
    "06UncorrelatedWithSimilarWeights",
    "07SpannerUncorrelated",
    "08SpannerWeaklyCorrelated",
    "09SpannerStronglyCorrelated",
    "10MultipleStronglyCorrelated",
    "11ProfitCeiling",
    "12Circle"
    ]

sub_folders = [
    "n00050",
    "n00100",
    "n00500",
    "n01000",
    "n05000"
]

dir_dataset = os.path.join("e:\CS106.M11.KHCL\Assignment_2", "kplib")

def read_test_cases(path_file):
    path_file = str(path_file).replace("\\", "/")
    values = []
    weights = [[]]
    capacities = []

    lines = open(path_file, 'r').readlines()

    n = int(lines[1])
    capacities.append(int(lines[2]))

    for i in range(4, 4 + n):
        a, b = [int(x) for x in lines[i].split()]
        values.append(a)
        weights[0].append(b)
    return values, weights, capacities

def main():
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')
    # values = [
    #     360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
    #     78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
    #     87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
    #     312
    # ]
    # weights = [[
    #     7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
    #     42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
    #     3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13
    # ]]
    # capacities = [850]

    TIME_LIMIT = 180 # set limited time to 3 mins for each test cases

    for item in directories:
        for sub_item in sub_folders:
            tmp = os.path.join(dir_dataset, item, sub_item, "R01000")
            for file in os.listdir(tmp):
                values, weights, capacities = read_test_cases(file)

                solver.Init(values, weights, capacities)
                solver.set_time_limit(TIME_LIMIT)

                start = time.time()
                computed_value = solver.Solve()
                end = time.time()

                time_cost = end - start

                # packed_items = []
                # packed_weights = []
                total_weight = 0
                isSuccess = True
                print('Total value =', computed_value)
                for i in range(len(values)):
                    if solver.BestSolutionContains(i):
                        # packed_items.append(i)
                        # packed_weights.append(weights[0][i])
                        total_weight += weights[0][i]
                print('Total weight:', total_weight)
                # print('Packed items:', packed_items)
                # print('Packed_weights:', packed_weights)
                test_case_name = "{}_{}".format(item, sub_item)
                file_out = open('result.csv', 'w')
                if time_cost > TIME_LIMIT:
                    print("Time limited!")
                    isSuccess = False
                file_out.writelines(test_case_name + "," + str(computed_value) + "," + str(total_weight) + "," + str(isSuccess))
                break
            break
        break


    

if __name__ == '__main__':
    main()