import pandas as pd
import matplotlib.pyplot as plt
import os, inspect
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

######################################################################
## if you want to change CSV file path, please change this variable ##
######################################################################
data_path = './logs/'

def display_graph_ovarlap():
    index = lb.curselection()[0]
    index_x = lb_x.curselection()[0]
    index_y = lb_y.curselection()
    filename = lb.get(index)
    var_x = lb_x.get(index_x)
    var_y = []
    for i in index_y:
        var_y.append(lb_y.get(i))
        
    df = pd.read_csv(data_path + filename, usecols = [var_x] + var_y)

    fig = plt.figure(figsize = [12, 8])
    ax = fig.add_subplot(111)

    for j in var_y:
        ax.plot(df[var_x], df[j], marker = '.', linewidth = int(txt_linew.get()))
    ax.set_xlabel(var_x)
    ax.set_ylabel('Scatter')
    ax.legend(var_y)
    if bln_grid.get():
        ax.grid(which = 'both')
    if bln_logx.get():
        ax.set_xscale('log')
    if bln_logy.get():
        ax.set_yscale('log')

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
        
    df = pd.read_csv(data_path + filename, usecols = [var_x] + var_y)
    fig = plt.figure(figsize = [12, 8])
    cnt = 0
    ydata_length = len(var_y)
    for j in var_y:
        cnt += 1
        num_subplot = ydata_length * 100 + 10 + cnt
        ax = fig.add_subplot(num_subplot)
        ax.set_ylabel(j)

        ax.plot(df[var_x], df[j], marker = '.', linewidth = int(txt_linew.get()))
        if bln_grid.get():
            ax.grid(which = 'both')
        if bln_logx.get():
            ax.set_xscale('log')
        if bln_logy.get():
            ax.set_yscale('log')
    ax.set_xlabel(var_x)
    
    plt.show()

def insert_lb():
    index = lb.curselection()[0]
    csv_filename = lb.get(index)
    df = pd.read_csv(data_path + csv_filename)
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

def save_all_graph():
    index = lb.curselection()[0]
    index_x = lb_x.curselection()[0]
    filename = lb.get(index)
    var_x = lb_x.get(index_x)
    var_y = []        
    df = pd.read_csv(data_path + filename)
    for i in df:
        var_y.append(i)
    
    cnt = 0
    for j in var_y:
        cnt += 1
        fig = plt.figure(figsize = [12, 8])
        ax = fig.add_subplot(111)
        ax.plot(df[var_x], df[j], marker = '.', linewidth = int(txt_linew.get()))
        ax.set_xlabel(var_x)
        ax.set_ylabel(j)
        if bln_grid.get():
            ax.grid(which = 'both')
        if bln_logx.get():
            ax.set_xscale('log')
        if bln_logy.get():
            ax.set_yscale('log')
        plt.savefig(txt_save_dir.get() + 'save_' + str(cnt) + '.png')
        fig.delaxes(ax)
        plt.clf()
        plt.close()

root = tk.Tk()
root.geometry('600x700')
root.title("create graph")

## CAUTION ##
## when you make listbox, you SHOULD assign different variable to listvariable
## the function keyword refer to memory place
lb_x = tk.Listbox(root, listvariable = tk.StringVar(), width = 28, height = 15, exportselection = 0)
lb_x.configure(selectmode = 'browse')

lb_y = tk.Listbox(root, listvariable = tk.StringVar(), width = 28, height = 15, exportselection = 0)
lb_y.configure(selectmode = 'extended')

button_graph_overlap = tk.Button(root, text = 'create graph overlap', command = display_graph_ovarlap) ## plot scatter overlap

button_graph_separate = tk.Button(root, text = 'create graph separately', command = display_graph_separate) ## plot scatter line up vertival axis

listarray = os.listdir('./logs/')
txt = tk.StringVar(value = listarray)
lb = tk.Listbox(root, listvariable = txt, width = 28, height = 15, exportselection = 0)
lb.configure(selectmode = 'browse')

button = tk.Button(root, text = 'select csv file', command = insert_lb)

button_save_all = tk.Button(root, text = 'save all graph', command = save_all_graph)

bln_grid = tk.BooleanVar()
bln_grid.set(True)
chk_grid = tk.Checkbutton(root, variable = bln_grid, text = 'grid line')

bln_logx = tk.BooleanVar()
bln_logx.set(False)
chk_logx = tk.Checkbutton(root, variable = bln_logx, text = 'x log')

bln_logy = tk.BooleanVar()
bln_logy.set(False)
chk_logy = tk.Checkbutton(root, variable = bln_logy, text = 'y log')

txt_linew = tk.Entry(width = 10)
txt_linew.insert(tk.END, '0')

txt_save_dir = tk.Entry(width = 20)
txt_save_dir.insert(tk.END, './test/')

lb_x.grid(column = 1, row = 2, pady = 10, padx = 10)
lb_y.grid(column = 2, row = 2, pady = 10, padx = 10)
button_graph_overlap.grid(column = 3, row = 2, padx = 10)

lb.grid(column = 1, row = 1)
button.grid(column = 2, row = 1)
chk_logx.grid(column = 1, row = 3)
chk_logy.grid(column = 2, row = 3)
txt_linew.grid(column = 1, row = 4, pady = 10, padx = 10)
chk_grid.grid(column = 2, row = 4, pady = 10, padx = 10)
button_graph_separate.grid(column = 3, row = 4, pady = 10, padx = 10)
button_save_all.grid(column = 3, row = 5, pady = 10, padx = 10)
txt_save_dir.grid(column = 1, row = 5, pady = 10, padx = 10)

root.mainloop()
