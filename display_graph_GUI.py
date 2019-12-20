import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math, os, inspect, pylab
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from time import sleep

def click_graph(event):
    print('event.button ...' + str(event.button))
    print('event.xdata  ... ' + str(event.xdata))
    print('event.ydata  ... ' + str(event.ydata))
    # global stat_click, x_first, x_second
    # if str(event.button) == 'MouseButton.LEFT' and stat_click == 1 : ## start
    #     stat_click = 2
    #     x_first = event.xdata
            
    # elif str(event.button) == 'MouseButton.LEFT' and stat_click == 2:
    #     x_second = event.xdata
    #     x_diff = x_second - x_first
    #     if x_diff > 0 :
    #         ax.set_xlim(x_first, x_second)
    #         print('resized.\n')
    #     else :
    #         ax.set_xlim(auto = True)
    #         print('return.\n')
    #         plt.cla()
    #         plt.show()
    #         stat_click = 1
                    
    # elif str(event.button) == 'MouseButton.RIGHT' :
    #     stat_click = 1
    #     x_first = 0
    #     x_second = 0
                        

def display_graph_ovarlap():
    index = lb.curselection()[0]
    index_x = lb_x.curselection()[0]
    index_y = lb_y.curselection()
    filename = lb.get(index)
    var_x = lb_x.get(index_x)
    var_y = []
    for i in index_y:
        var_y.append(lb_y.get(i))
        
    df = pd.read_csv('./logs/' + filename, usecols = [var_x] + var_y)

    fig = plt.figure(figsize = [12, 8])
    ax = fig.add_subplot(111)
    for j in var_y:
        ax.scatter(df[var_x], df[j], marker = '.')
    ax.set_xlabel(var_x)
    ax.set_ylabel('Scatter')
    ax.legend(var_y)
    cid = fig.canvas.mpl_connect('button_press_event', click_graph)
    plt.show()

def display_graph_separate():
    index = lb.curselection()[0]
    index_x = lb_x.curselection()[0]
    index_y = lb_y.curselection()
    filename = lb.get(index)
    var_x = lb_x.get(index_x)
    var_y = []
    for i in index_y:
        var_y.append(lb_y.get(i))
        
    df = pd.read_csv('./logs/' + filename, usecols = [var_x] + var_y)
    fig = plt.figure(figsize = [12, 8])
    cnt = 0
    ydata_length = len(var_y)
    for j in var_y:
        cnt += 1
        num_subplot = ydata_length * 100 + 10 + cnt
        ax = fig.add_subplot(num_subplot)
        ax.scatter(df[var_x], df[j], marker = '.')
        ax.set_ylabel(j)
    ax.set_xlabel(var_x)
    cid = fig.canvas.mpl_connect('button_press_event', click_graph)
    plt.show()

def insert_lb():
    index = lb.curselection()[0]
    csv_filename = lb.get(index)
    df = pd.read_csv('./logs/' + csv_filename)
    csv_header = []
    for i in df:
        csv_header.append(i)
    # print(csv_header)
    
    # header_name_path = './header_names.txt'
    # csv_header = []
    # for i in open(header_name_path):
    #     csv_header.append(i.rstrip('\n')) 
    lb_x.delete(0, END)
    lb_y.delete(0, END)
    for j in csv_header:
        lb_x.insert(END, j)
        lb_y.insert(END, j)
    
root = tk.Tk()
root.geometry('600x550')
root.title("create graph")

## CAUTION ##
## when you make listbox, you SHOULD assign different variable to listvariable
## the function keyword refer to memory place
lb_x = tk.Listbox(root, listvariable = StringVar(), width = 28, height = 15, exportselection = 0)
lb_x.configure(selectmode = 'browse')
# scrollbar_xaxis = ttk.Scrollbar(root, orient = VERTICAL, command = lb_x.yview)

lb_y = tk.Listbox(root, listvariable = StringVar(), width = 28, height = 15, exportselection = 0)
lb_y.configure(selectmode = 'extended')
# scrollbar_yaxis = ttk.Scrollbar(root, orient = VERTICAL, command = lb_y.yview)

button_graph_overlap = Button(root, text = 'create graph overlap', command = display_graph_ovarlap) ## plot scatter overlap
# button_graph.bind('<1>', display_graph_button)

button_graph_separate = Button(root, text = 'create graph separately', command = display_graph_separate) ## plot scatter line up vertival axis

listarray = os.listdir('./logs/')
txt = tk.StringVar(value = listarray)
lb = tk.Listbox(root, listvariable = txt, width = 28, height = 15, exportselection = 0)
lb.configure(selectmode = 'browse')
# lb.bind('<<ListboxSelect>>', insert_header)
# scrollbar_csv = ttk.Scrollbar(root, orient = VERTICAL, command = lb.yview)

button = ttk.Button(root, text = 'select csv file', command = insert_lb) 

lb_x.grid(column = 1, row = 2, pady = 10, padx = 10)
lb_y.grid(column = 2, row = 2, pady = 10, padx = 10)
button_graph_overlap.grid(column = 3, row = 2, padx = 10)
button_graph_separate.grid(column = 3, row = 3, pady = 10, padx = 10)

lb.grid(column = 1, row = 1)
button.grid(column = 2, row = 1)

root.mainloop()
