'''
Sources: 
matplotlib help: https://matplotlib.org/stable/tutorials/pyplot.html
Stats: https://stackoverflow.com/questions/31455470/definition-of-standard-error-in-scipy-stats-linregress, https://docs.scipy.org/doc/scipy-1.2.3/reference/generated/scipy.stats.linregress.html
'''
import sys
import pandas as pd                 #type: ignore
import matplotlib.pyplot as plt     #type: ignore
import numpy as np                  #type: ignore
import statistics
from scipy.stats import linregress  #type: ignore

def iseven(number):
    if number % 2 == 0:
        return("even")
    else:
        return("odd")

def collatz(number):
    even = iseven(number)
    if even == "even": 
        number = number/2
        return(number)
    elif even == "odd":
        number = number * 3 + 1
        return(number)

def check_integer(number):
    try:
        number = int(number)
    except ValueError:
        return "False"
    return number

def get_number():
    while True:
        number = input("Enter a multiple (Enter stop to stop code):")
        isinteger = check_integer(number)
        if number == "stop":
            sys.exit()
        elif isinteger == "wrong input":
            print("You did not enter a number")
        else:
            number = isinteger
            return(number)

def one_number(all_numbers):
    data={} 
    iterations = 0 
    
    
    while True:
        ori_number = input("Enter a positive number: ")
        isinteger = check_integer(ori_number)
        if isinteger == "False":
            print("You did not enter a number")
        elif ori_number.lower == "exit":
            sys.exit()
        else:
            number = isinteger
            break

    while number != 1:
            data[number]= iterations
            number = collatz(number)
            iterations += 1
    
    all_numbers[iterations] = ori_number
    print(iterations)
    print(data)
    create_one(data,ori_number,iterations)

def one_multiple(all_numbers):
    data = {}
    while True:
        multiple = input("Enter multiple:")
        multiple = check_integer(multiple)
        if multiple == "False":
            print("Enter a multiple")
        else:
            break

    for number in range(multiple, multiple*1000+1, multiple): 
        iterations = 0
        ori_number = number
        iterations_count = 0
        number = collatz(number)
        while number != 1:
            number = collatz(number)
            iterations += 1
        add_dictionary(data, ori_number, iterations)
    
    numbers = list(data.keys())
    iterations_list = list(data.values()) 
    x = np.array(numbers)
    y = np.array(iterations_list)


    sorted_data = sorted_dic(data)

    mean = get_mean(data)
    median = get_median(data)
    rang = get_range(sorted_data)
    slope, intercept = intercept_slope(x,y)
    line_x, line_y = LOBF(x,y)
    r_2, r_value = r_squared(x,y)
    
    print()
    print(f"Iterations Statistics for{multiple}")
    print(f"Mean: {mean} ")
    print(f"Median: {median} ")
    print(f"Range: {rang} ")
    print(f"Equation: y = {slope:.4f}x + {intercept:.2f}")
    print(f"R-squared: {r_2:.4f}")
    print(f"Correlation coefficient (r): {r_value:.4f}")

    create_graph(numbers, iterations_list, x,y, line_x, line_y, mean, median, rang,slope, intercept, r_2, r_value)
        
def each_multiple(all_numbers,means,medians, ranges, LOBF_slope, multiple):
    data={}
    for number in range(multiple, multiple*1000+1, multiple): 
        iterations = 0
        ori_number = number
        while number != 1:
            if number in all_numbers:  
                iterations += all_numbers[number] 
                break 
            number = collatz(number)
            iterations += 1
        add_dictionary(data, ori_number, iterations)
        all_numbers[ori_number] = iterations
        
    numbers = list(data.keys())
    iterations_list = list(data.values()) 
    x = np.array(numbers)
    y = np.array(iterations_list)


    sorted_data = sorted_dic(data)

    mean = get_mean(data)
    means[multiple] = mean
    median = get_median(data)
    medians[multiple] = median
    rang = get_range(sorted_data)
    ranges[multiple] = rang
    slope, intercept = intercept_slope(x,y)
    LOBF_slope[multiple] = slope

    line_x, line_y = LOBF(x,y)
    r_2, r_value = r_squared(x,y)
    
    print()
    print(f"Iterations Statistics for{multiple}")
    print(f"Mean: {mean} ")
    print(f"Median: {median} ")
    print(f"Range: {rang} ")
    print(f"Equation: y = {slope:.4f}x + {intercept:.2f}")
    print(f"R-squared: {r_2:.4f}")
    print(f"Correlation coefficient (r): {r_value:.4f}")
    
    return all_numbers,means,medians, ranges, LOBF_slope


def add_dictionary(data_dict,number, iterations):
    data_dict[number] = iterations
    return data_dict

def create_summary_graphs(means, medians, ranges, LOBF_slope):
    """Create graphs showing how statistics vary across different multiples"""
    
    multiples = list(means.keys())
    mean_values = list(means.values())
    median_values = list(medians.values())
    range_values = list(ranges.values())
    slope_values = list(LOBF_slope.values())
    
    # Create a figure with 4 subplots (2x2 grid)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Statistics Across Different Multiples', fontsize=16, fontweight='bold')
    
    # Graph 1: Means
    axes[0, 0].plot(multiples, mean_values, marker='o', linestyle='-', linewidth=2, markersize=8, color='blue')
    axes[0, 0].set_xlabel('Multiple', fontsize=11)
    axes[0, 0].set_ylabel('Mean Iterations', fontsize=11)
    axes[0, 0].set_title('Mean Iterations vs Multiple', fontsize=12)
    axes[0, 0].grid(True, alpha=0.3)
    
    # Graph 2: Medians
    axes[0, 1].plot(multiples, median_values, marker='s', linestyle='-', linewidth=2, markersize=8, color='green')
    axes[0, 1].set_xlabel('Multiple', fontsize=11)
    axes[0, 1].set_ylabel('Median Iterations', fontsize=11)
    axes[0, 1].set_title('Median Iterations vs Multiple', fontsize=12)
    axes[0, 1].grid(True, alpha=0.3)
    
    # Graph 3: Ranges
    axes[1, 0].plot(multiples, range_values, marker='^', linestyle='-', linewidth=2, markersize=8, color='red')
    axes[1, 0].set_xlabel('Multiple', fontsize=11)
    axes[1, 0].set_ylabel('Range', fontsize=11)
    axes[1, 0].set_title('Range vs Multiple', fontsize=12)
    axes[1, 0].grid(True, alpha=0.3)
    
    # Graph 4: LOBF Slopes
    axes[1, 1].plot(multiples, slope_values, marker='D', linestyle='-', linewidth=2, markersize=8, color='purple')
    axes[1, 1].set_xlabel('Multiple', fontsize=11)
    axes[1, 1].set_ylabel('Slope', fontsize=11)
    axes[1, 1].set_title('Line of Best Fit Slope vs Multiple', fontsize=12)
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

def create_one(data, ori_number,total_iterations):
    numbers = list(data.keys())  
    iterations_from_first = list(data.values())  

    plt.figure(figsize=(10, 6))
    plt.plot(iterations_from_first, numbers, marker='o', linestyle='-', markersize=8, label='Data points')

    plt.xlabel('Iterations from start', fontsize=12)
    plt.ylabel('Number', fontsize=12)
    plt.title(f'Collatz Sequence for {ori_number}', fontsize=14)

    plt.grid(True, alpha=0.3)
    plt.legend()

    textstr = f'Total Iterations: {total_iterations:.4f}'
    plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.show()

def create_graph(numbers, iterations_list, line_x, line_y, mean, median, rang, slope, intercept, r_2, r_value):
    plt.figure(figsize=(10, 6))
    plt.plot(numbers, iterations_list, marker='o', linestyle='', markersize=8, label='Data points')  # Changed iterations to iterations_list
    
    # Add line of best fit
    plt.plot(line_x, line_y, color='red', linestyle='--', linewidth=2, 
             label=f'Best fit: y={slope:.4f}x+{intercept:.2f}')

    # Add labels and title with R² value
    plt.xlabel('Number', fontsize=12)
    plt.ylabel('Iterations', fontsize=12)
    plt.title(f'Number vs Iterations (R² = {r_2:.4f})', fontsize=14)

    # Add grid and legend
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Add text box with statistics
    textstr = f'Slope: {slope:.4f}\nIntercept: {intercept:.2f}\nR²: {r_2:.4f}\nMean: {mean:.2f}\nMedian: {median:.2f}\nRange: {rang:.2f}'
    plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # Display the plot
    plt.show()


def sorted_dic(data):
    sorted_items = sorted(data.items(), key=lambda item: item[1])
    sorted_data = dict(sorted_items)
    return(sorted_data)

def get_mean(data):
    meanval = sum(data.values()) / len(data)
    return meanval 

def get_median(data):
    numbers = list(data.values())
    median = statistics.median(numbers)
    return median 

def get_range(data):
    first_value = list(data.values())[0]
    last_value = list(data.values())[-1]
    rang = last_value - first_value
    return rang

def r_squared(x,y):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    r_squared = r_value**2
    return r_squared, r_value

def LOBF(x,y):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    line_x = np.array([min(x), max(x)])
    line_y = slope * line_x + intercept
    return line_x, line_y

def intercept_slope(x,y):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    return intercept, slope


def main():
    all_numbers = {}
    means={}
    medians={}
    ranges={}
    LOBF_slope={}
    print()
    print("Collatz Conjecture Graphs Maker")
    print()
    print("1. Go through one number")
    print("2. Go through one multiple")
    print("3. Go through multiple multiples")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        one_number(all_numbers)
    elif choice == "2":
        one_multiple(all_numbers)
    elif choice == "4":
        sys.exit()
    elif choice == "3":
        while True:
            lower_multiple = input("Enter lower multiple: ")
            higher_multiple= input("Enter Higher Multiple: ")
            lower_multiple = check_integer(lower_multiple)
            higher_multiple = check_integer(higher_multiple)
            if lower_multiple == "False" or higher_multiple== "False":
                print("Enter a multiple for both")
            else:
                break
        
        for i in range(higher_multiple - lower_multiple + 1):
            multiple = lower_multiple + i
            all_numbers,means,medians, ranges, LOBF_slope = each_multiple(all_numbers,means,medians, ranges, LOBF_slope, multiple)
        
        create_summary_graphs(means, medians, ranges, LOBF_slope)

main()