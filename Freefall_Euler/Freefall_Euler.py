# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:12:48 2019

@author: Josiah
"""


import numpy as np
import matplotlib.pyplot as plt

gravity = 9.81

drag_coefficient = 1.3
air_density = 1.2
cross_section = 0.8
mass = 90
time_step = 1
time_end = 2000
initial_height = 39000


time_axis = [0]
height_axis = [initial_height]
velocity_axis = [0]

height_axis_modified = [initial_height]
velocity_axis_modified = [0]

height_axis_analytical = [initial_height]
velocity_axis_analytical = [0]

time_index = 0

EulerSelected = True
ModifiedSelected = True
AnalyticalSelected = True

resistance_constant = 0.5 * (drag_coefficient * air_density * cross_section)
    
def velocity_iteration(velocity, resistance, step):
    return velocity - step * (gravity + (resistance/mass)*(np.abs(velocity)*velocity))

def height_iteration(height, velocity, step):
    return height + step * velocity

def density_eq(height):
    return air_density * np.exp(-height/7640)
        

current_height = initial_height

while current_height > 0:
    
    time_index += 1
    time_axis.append(time_index * time_step)
    
    
    
    if EulerSelected is True:
        resistance_constant = 0.5 * (drag_coefficient * density_eq(height_axis[time_index-1]) * cross_section)
        height_axis.append(height_iteration(height_axis[time_index-1], velocity_axis[time_index-1], time_step))
        velocity_axis.append(velocity_iteration(velocity_axis[time_index-1], resistance_constant, time_step))

        current_height = height_axis[time_index]
        

        
    if ModifiedSelected is True:
        
        #height_midpoint = height_iteration(height_axis_modified[time_index-1], velocity_axis_modified[time_index-1], time_step/2)
        velocity_axis_modified.append(velocity_iteration(velocity_axis_modified[time_index-1], resistance_constant, time_step/2))
        height_axis_modified.append(height_iteration(height_axis_modified[time_index-1], velocity_axis_modified[time_index-1], time_step))
        
        current_height = height_axis_modified[time_index]
        
    if AnalyticalSelected is True:
        
        #resistance_constant = 0.5 * (drag_coefficient * density_eq(height_axis_analytical[time_index-1]) * cross_section)
        
        velocity_axis_analytical.append(- np.sqrt((mass* gravity) /resistance_constant) * np.tanh(np.sqrt(resistance_constant * gravity / mass) * time_axis[time_index]))
    
        height_axis_analytical.append(initial_height -  (mass /(2 * resistance_constant)) * np.log((np.cosh(np.sqrt((resistance_constant * gravity) / mass) * time_axis[time_index]))**2))
        
    if current_height < 0:
        height_axis[time_index] = 0



del height_axis[0]
del time_axis[-1]
del velocity_axis[-1]
del velocity_axis_analytical[-1]
del height_axis_analytical[-1]

plt.plot(time_axis, height_axis)
plt.plot(time_axis, height_axis_analytical)
plt.ylabel('Height (m)')
plt.xlabel('Time (s)')
plt.show()

plt.plot(time_axis, velocity_axis)
plt.plot(time_axis, velocity_axis_analytical)
plt.ylabel('Velocity (ms^-1)')
plt.xlabel('Time (s)')
plt.show()