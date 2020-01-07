import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os, inspect
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

######################################################################
## if you want to change CSV file path, please change this variable ##
######################################################################
data_path = './logs/'

# class ClickGraphActivity:
#     def __init__(self, graph):
#         self.graph = graph
#         self.graph_origin = graph
#         self.stat = 0
#         self.x_first = 0
#         self.x_second = 0
#         self.y_first = 0
#         self.y_second = 0
#         self.cid = graph.figure.canvas.mpl_connect('button_press_event', self)
        
#     def __call__(self, event):
#         print('click', event)
#         if self.stat == 0 and event.button == 1:
#             self.x_first = event.xdata
#             self.y_first = event.ydata
#             self.stat = 1
#             print('event.xdata = ' + str(event.xdata))
#             print('event.x = ' + str(event.x))

#         elif self.stat == 1 and event.button == 1:
#             self.x_second = event.xdata
#             self.y_second = event.ydata
#             self.stat = 0
#             if (self.x_second - self.x_first) > 0:
#                 self.graph.figure.delaxes(self.graph.axes)
                # ax_ = self.graph.figure.add_subplot(111)
                # ax_.set_xlim(self.x_first, self.x_second)
                # ax_.set_ylim(self.y_first, self.y_second)
                # ydata_length = len(self.graph_origin.)
                # cnt = 0
                # ax_.set_xlabel(var_x)
                # ax_.set_ylabel('Scatter')
                # ax.legend(var_y)
                # # for j in var_y:
                # #     cnt += 1
                # #     if cnt == ydata_length:
                # #         print('################## test ###################')
                # #         graph, = ax.plot(df[var_x], df[j], marker = '.', linewidth = 0)
                # #     else :
                # #         ax.plot(df[var_x], df[j], marker = '.', linewidth = 0)


                
        #     else:
        #         self.graph.figure.delaxes(self.graph.axes)
                
        #         set_xlim(auto = True)
                
        #     plt.draw()
        #     self.x_first = 0
        #     self.x_second = 0

        # elif event.button == 3:
        #     self.stat = 0
        #     self.x_first = 0
        #     self.x_second = 0
    
        
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
        
    df = pd.read_csv(data_path + filename, usecols = [var_x] + var_y)

    fig = plt.figure(figsize = [12, 8])
    ax = fig.add_subplot(111)
    # for j in var_y:
        # cnt += 1
        # ax.plot(df[var_x], df[j], marker = '.', linewidth = 0)
        # if cnt == ydata_length:
        #     print('################## test ###################')
        #     graph, = ax.plot(df[var_x], df[j], marker = '.', linewidth = 0)
        # else :
            # ax.plot(df[var_x], df[j], marker = '.', linewidth = 0)
    # # graph, = ax.plot([0], [0])
    # graph, = ax.plot(df[var_x], df[var_y[0]], marker = '.')
    # click = ClickGraphActivity(graph)
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
        
    df = pd.read_csv(data_path + filename, usecols = [var_x] + var_y)
    fig = plt.figure(figsize = [12, 8])
    cnt = 0
    ydata_length = len(var_y)
    for j in var_y:
        cnt += 1
        num_subplot = ydata_length * 100 + 10 + cnt
        ax = fig.add_subplot(num_subplot)
        ax.set_ylabel(j)
        # if cnt == ydata_length:
        #     print('test')
        #     graph, = ax.plot(df[var_x], df[j], marker = '.', linestyle = None)
        # else :
        #     ax.plot(df[var_x], df[j], marker = '.', linestyle = None)
        ax.plot(df[var_x], df[j], marker = '.', linewidth = int(txt_linew.get()))
        if bln_grid.get():
            ax.grid(which = 'both')
        if bln_logx.get():
            ax.set_xscale('log')
        if bln_logy.get():
            ax.set_yscale('log')
    ax.set_xlabel(var_x)
    # ax.can_pan()
    # graph, = ax.plot([0], [0])
    # click = ClickGraphActivity(graph)
    cid = fig.canvas.mpl_connect('button_press_event', click_graph)
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

# bln_line = tk.BooleanVar()
# bln_line.set(False)
# chk_line = tk.Checkbutton(root, variable = bln_line, text = 'line')

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
