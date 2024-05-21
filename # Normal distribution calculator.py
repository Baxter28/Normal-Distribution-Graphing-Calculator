                                        #**********Normal Distribution Calculator**********

import tkinter as tk
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def plot_distribution():
    
    mean = float(mean_entry.get())#mean value
    std = float(std_entry.get())#standard deviation
    lower_bound = float(lower_bound_entry.get())#upper bound
    upper_bound = float(upper_bound_entry.get())#lower bound

    # Creating the distribution curve
    data = np.linspace(mean - 4 * std, mean + 4 * std, 1000)# start and end points of array 4 standard deviations 1000 is number of values creates a smoother curve
    pdf = norm.pdf(data, loc=mean, scale=std)#probability density function

    LowerBound = norm(loc=mean, scale=std).cdf(lower_bound)#creates lower bound using scipy norm
    UpperBound = norm(loc=mean, scale=std).cdf(upper_bound)#creates upper bound
    probability_within_bounds = UpperBound - LowerBound#range between lower and upper bound

    plt.figure(figsize=(8, 6))
    plt.plot(data, pdf, color='black')#plot graph line
    plt.fill_between(data, pdf, where=(data >= lower_bound) & (data <= upper_bound), color='skyblue', alpha=0.5)#range to highlight alpha value is transparency
    plt.title('Normal Distribution PDF')
    plt.xlabel('Values')
    plt.ylabel('Probability Density')

    plt.axvline(mean, color='red', linestyle='--', label=f'Mean: {mean}')#add the lines on the graph to show points of inflection
    plt.axvline(mean - std, color='blue', linestyle='--', label=f'Mean - 1 std')
    plt.axvline(mean + std, color='blue', linestyle='--', label=f'Mean + 1 std')

    plt.legend()
    plt.show()

def calculate_probability():
    mean = float(mean_entry.get())
    std = float(std_entry.get())
    lower_bound = float(lower_bound_entry.get())
    upper_bound = float(upper_bound_entry.get())

    LowerBound = norm(loc=mean, scale=std).cdf(lower_bound)
    UpperBound = norm(loc=mean, scale=std).cdf(upper_bound)
    probability_within_bounds = UpperBound - LowerBound

    result_label.config(text=f"Probability between bounds: {probability_within_bounds:.4f}")#.4f means to display to 4dp

# Create the main window
root = tk.Tk()
root.title("Normal Distribution Probability Calculator")
root.geometry("300x300")

# Mean input
mean_label = tk.Label(root, text="Mean:")
mean_label.pack()
mean_entry = tk.Entry(root)
mean_entry.pack()

# Standard Deviation input
std_label = tk.Label(root, text="Standard Deviation:")
std_label.pack()
std_entry = tk.Entry(root)
std_entry.pack()

# Lower bound input
lower_bound_label = tk.Label(root, text="Lower Bound:")
lower_bound_label.pack()
lower_bound_entry = tk.Entry(root)
lower_bound_entry.pack()

# Upper bound input
upper_bound_label = tk.Label(root, text="Upper Bound:")
upper_bound_label.pack()
upper_bound_entry = tk.Entry(root)
upper_bound_entry.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_probability)
calculate_button.pack(pady = 10)#creates a buffer between the input boxes and button

# Plot button
plot_button = tk.Button(root, text="Plot Distribution Curve", command=plot_distribution)
plot_button.pack(pady = 10)

# Display result
result_label = tk.Label(root, text="")#displays nothing till the result is calculated
result_label.pack()

root.mainloop()

