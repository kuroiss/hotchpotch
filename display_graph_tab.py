import pandas as pd
import matplotlib.pyplot as plt
import os, inspect
import tkinter as tk
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
    mark = '.'
    if not bln_marker.get():
        mark = ''
    for j in var_y:
        ax.plot(df[var_x], df[j], marker = mark, linewidth = int(txt_linew.get()))
    ax.set_xlabel(var_x)
    ax.set_ylabel('Scatter')
    ax.legend(var_y)
    if bln_grid.get():
        ax.grid(which = 'both')
    if bln_logx.get():
        ax.set_xscale('log')
    if bln_logy.get():
        ax.set_yscale('log')
        
    if not txt_limx_low.get() == '' and not txt_limx_upper.get() == '':
        ax.set_xlim(float(txt_limx_low.get()), float(txt_limx_upper.get()))

    if not txt_limy_low.get() == '' and not txt_limy_upper.get() == '':
        ax.set_ylim(float(txt_limy_low.get()), float(txt_limy_upper.get()))
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
    mark = '.'
    if not bln_marker.get():
        mark = ''
    for j in var_y:
        cnt += 1
        num_subplot = ydata_length * 100 + 10 + cnt
        ax = fig.add_subplot(num_subplot)
        ax.set_ylabel(j)

        ax.plot(df[var_x], df[j], marker = mark, linewidth = int(txt_linew.get()))
        if bln_grid.get():
            ax.grid(which = 'both')
        if bln_logx.get():
            ax.set_xscale('log')
        if bln_logy.get():
            ax.set_yscale('log')
        if not txt_limx_low.get() == '' and not txt_limx_upper.get() == '':
            ax.set_xlim(float(txt_limx_low.get()), float(txt_limx_upper.get()))
        if not txt_limy_low.get() == '' and not txt_limy_upper.get() == '':
            ax.set_ylim(float(txt_limy_low.get()), float(txt_limy_upper.get()))
        
    ax.set_xlabel(var_x)

    plt.show()

def update_csv_list():
    listarray = os.listdir(data_path)
    lb.delete(0, tk.END)
    for j in listarray:
        lb.insert(tk.END, j)

def insert_lb(event):
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
    lb_x.delete(0, tk.END)
    lb_y.delete(0, tk.END)
    for j in csv_header:
        lb_x.insert(tk.END, j)
        lb_y.insert(tk.END, j)

def clear_lim():
    txt_limx_low.delete(0, tk.END)
    txt_limx_upper.delete(0, tk.END)
    txt_limy_low.delete(0, tk.END)
    txt_limy_upper.delete(0, tk.END)
    
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
    mark = '.'
    if not bln_marker.get():
        mark = ''
    for j in var_y:
        cnt += 1
        fig = plt.figure(figsize = [12, 8])
        ax = fig.add_subplot(111)
        ax.plot(df[var_x], df[j], marker = mark, linewidth = int(txt_linew.get()))
        ax.set_xlabel(var_x)
        ax.set_ylabel(j)
        if bln_grid.get():
            ax.grid(which = 'both')
        if bln_logx.get():
            ax.set_xscale('log')
        if bln_logy.get():
            ax.set_yscale('log')
        if not txt_limx_low.get() == '' and not txt_limx_upper.get() == '':
            ax.set_xlim(float(txt_limx_low.get()), float(txt_limx_upper.get()))

        if not txt_limy_low.get() == '' and not txt_limy_upper.get() == '':
            ax.set_ylim(float(txt_limy_low.get()), float(txt_limy_upper.get()))
            
        plt.savefig(txt_save_dir.get() + 'save_' + str(cnt) + '.png')
        fig.delaxes(ax)
        plt.clf()
        plt.close()

root = tk.Tk()
root.geometry('600x600')
root.title("create graph")

###### create tabs #######
nb = ttk.Notebook(width = 500, height = 500)

tab_main = tk.Frame(nb)
tab_option = tk.Frame(nb)
tab_save = tk.Frame(nb)

nb.add(tab_main, text = 'main', padding = 3)
nb.add(tab_option, text = 'option', padding = 3)
nb.add(tab_save, text = 'save', padding = 3)
nb.pack(expand = 1, fill = 'both')

frame_main = tk.Frame(tab_main, pady = 10)
frame_main.pack()
frame_option = tk.Frame(tab_option, pady = 10)
frame_option.pack()
frame_save = tk.Frame(tab_save, pady = 10)
frame_save.pack()


## CAUTION ##
## when you make listbox, you SHOULD assign different variable to listvariable
## the function keyword refer to memory place
lb_x = tk.Listbox(frame_main, listvariable = tk.StringVar(), width = 28, height = 15, exportselection = 0)
lb_x.configure(selectmode = 'browse')
label_lb_x = tk.Label(frame_main, text = 'x axis')

lb_y = tk.Listbox(frame_main, listvariable = tk.StringVar(), width = 28, height = 15, exportselection = 0)
lb_y.configure(selectmode = 'extended')
label_lb_y = tk.Label(frame_main, text = 'y axis')

button_graph_overlap = tk.Button(frame_main, text = 'create graph overlap', command = display_graph_ovarlap) ## plot scatter overlap

button_graph_separate = tk.Button(frame_main, text = 'create graph separately', command = display_graph_separate) ## plot scatter line up vertival axis

button_update_csv = tk.Button(frame_main, text = 'update csv list', command = update_csv_list)

listarray = os.listdir(data_path)
txt = tk.StringVar(value = listarray)
lb = tk.Listbox(frame_main, listvariable = txt, width = 28, height = 15, exportselection = 0)
lb.configure(selectmode = 'browse')
lb.bind('<<ListboxSelect>>', insert_lb)
label_lb = tk.Label(frame_main, text = 'file list')

button_save_all = tk.Button(frame_save, text = 'save all graph', command = save_all_graph)

bln_grid = tk.BooleanVar()
bln_grid.set(True)
chk_grid = tk.Checkbutton(frame_option, variable = bln_grid, text = 'grid line')

bln_marker = tk.BooleanVar()
bln_marker.set(True)
chk_marker = tk.Checkbutton(frame_option, variable = bln_marker, text = 'marker')

bln_logx = tk.BooleanVar()
bln_logx.set(False)
chk_logx = tk.Checkbutton(frame_main, variable = bln_logx, text = 'x log')

bln_logy = tk.BooleanVar()
bln_logy.set(False)
chk_logy = tk.Checkbutton(frame_main, variable = bln_logy, text = 'y log')

txt_linew = tk.Entry(frame_option, width = 10)
txt_linew.insert(tk.END, '0')
label_txt_linew = tk.Label(frame_option, text = 'line width')

txt_save_dir = tk.Entry(frame_save, width = 60)
txt_save_dir.insert(tk.END, data_path)
label_txt_save_dir = tk.Label(frame_save, text = 'save directory path')

# txt_limx_low = tk.Entry(frame_main, width = 10)
# label_txt_limx_low = tk.Label(frame_main, text = 'lim x lower')

# txt_limx_upper = tk.Entry(frame_main, width = 10)
# label_txt_limx_upper = tk.Label(frame_main, text = 'lim x upper')

# txt_limy_low = tk.Entry(frame_main, width = 10)
# label_txt_limy_low = tk.Label(frame_main, text = 'lim y lower')

# txt_limy_upper = tk.Entry(frame_main, width = 10)
# label_txt_limy_upper = tk.Label(frame_main, text = 'lim y upper')

# button_clear_lim = tk.Button(frame_main, text = 'delete lim', command = clear_lim)

txt_limx_low = tk.Entry(frame_option, width = 10)
label_txt_limx_low = tk.Label(frame_option, text = 'lim x lower')

txt_limx_upper = tk.Entry(frame_option, width = 10)
label_txt_limx_upper = tk.Label(frame_option, text = 'lim x upper')

txt_limy_low = tk.Entry(frame_option, width = 10)
label_txt_limy_low = tk.Label(frame_option, text = 'lim y lower')

txt_limy_upper = tk.Entry(frame_option, width = 10)
label_txt_limy_upper = tk.Label(frame_option, text = 'lim y upper')

button_clear_lim = tk.Button(frame_option, text = 'delete lim', command = clear_lim)

####### main tab ######
### row 1
label_lb.grid(row = 1, column = 1, padx = 10)

### row 2
lb.grid(row = 2, column = 1, padx = 10)

button_update_csv.grid(row = 2, column = 3, padx = 10, pady = 10)

### row 3
label_lb_x.grid(row = 3, column = 1, padx = 10)
label_lb_y.grid(row = 3, column = 2, padx = 10)

### row 4
lb_x.grid(row = 4, column = 1, padx = 10)
lb_y.grid(row = 4, column = 2, padx = 10)

button_graph_overlap.grid(row = 4, column = 3, padx = 10)

### row 5
chk_logx.grid(row = 5, column = 1)
chk_logy.grid(row = 5, column = 2)

button_graph_separate.grid(row = 5, column = 3, padx = 10)

# ### row 6
# label_txt_limx_low.grid(row = 6, column = 1, pady = 10)
# txt_limx_low.grid(row = 6, column = 2, padx = 10, pady = 10)

# label_txt_limx_upper.grid(row = 6, column = 3)
# txt_limx_upper.grid(row = 6, column = 4, padx = 10)

# ### row 7
# label_txt_limy_low.grid(row = 7, column = 1)
# txt_limy_low.grid(row = 7, column = 2, padx = 10)

# label_txt_limy_upper.grid(row = 7, column = 3)
# txt_limy_upper.grid(row = 7, column = 4, padx = 10)

# button_clear_lim.grid(row = 7, column = 5, pady = 10, padx = 10)

######## option tab ######
### row 1
label_txt_linew.grid(row = 1, column = 1)
txt_linew.grid(row = 1, column = 2, padx = 10)
chk_grid.grid(row = 1, column = 3, padx = 10)
chk_marker.grid(row = 1, column = 4, padx = 10)

### row 2
label_blank_o1 = tk.Label(frame_option, text = '')
label_blank_o1.grid(row = 2)

### row 3
label_txt_limx_low.grid(row = 3, column = 1, pady = 10)
txt_limx_low.grid(row = 3, column = 2, padx = 10, pady = 10)

label_txt_limx_upper.grid(row = 3, column = 3)
txt_limx_upper.grid(row = 3, column = 4, padx = 10)

### row 4
label_txt_limy_low.grid(row = 4, column = 1)
txt_limy_low.grid(row = 4, column = 2, padx = 10)

label_txt_limy_upper.grid(row = 4, column = 3)
txt_limy_upper.grid(row = 4, column = 4, padx = 10)

button_clear_lim.grid(row = 4, column = 5, pady = 10, padx = 10)


### row 5

######## save tab ######
### row 1
label_txt_save_dir.grid(row = 1, column = 1)

### row 2
txt_save_dir.grid(row = 2, column = 1, pady = 10, padx = 10)

button_save_all.grid(row = 2, column = 3, pady = 10, padx = 20)

### row 2


root.mainloop()
