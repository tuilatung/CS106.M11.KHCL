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

    TIME_LIMIT = 180 # set limited time to 3 mins for each test cases
    file_out = open('result.csv', 'a')

    for item in directories:
        for sub_item in sub_folders:
            tmp = os.path.join(dir_dataset, item, sub_item, "R01000")
            for file in os.listdir(tmp):
                values, weights, capacities = read_test_cases(os.path.join(tmp, file))

                solver.Init(values, weights, capacities)
                solver.set_time_limit(TIME_LIMIT)

                start = time.time()
                computed_value = solver.Solve()
                end = time.time()

                time_cost = end - start

                total_weight = 0
                isSuccess = True
                print('Total value =', computed_value)
                for i in range(len(values)):
                    if solver.BestSolutionContains(i):
                        total_weight += weights[0][i]
                print('Total weight:', total_weight)
                test_case_name = "{}_{}".format(item, sub_item)
                
                if time_cost > TIME_LIMIT:
                    print(test_case_name + "Time limited!")
                    isSuccess = False
                    content = test_case_name + "," + str(0) + "," + str(0) + "," + str(isSuccess)
                else:
                    content = test_case_name + "," + str(computed_value) + "," + str(total_weight) + "," + str(isSuccess)
                file_out.write(content + '\n')
                break
        break       
    file_out.close()
    

if __name__ == '__main__':
    main()