import virustotalhandler
import webbrowser
import copy
from tkinter import *
from tkinter import ttk, messagebox

SHIELD_LOGO = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

CAUTION = """                                                                                        
                                                                                        
                ░░░░                                                                    
                                                                                        
                                            ██                                          
                                          ██░░██                                        
  ░░          ░░                        ██░░░░░░██                            ░░░░      
                                      ██░░░░░░░░░░██                                    
                                      ██░░░░░░░░░░██                                    
                                    ██░░░░░░░░░░░░░░██                                  
                                  ██░░░░░░██████░░░░░░██                                
                                  ██░░░░░░██████░░░░░░██                                
                                ██░░░░░░░░██████░░░░░░░░██                              
                                ██░░░░░░░░██████░░░░░░░░██                              
                              ██░░░░░░░░░░██████░░░░░░░░░░██                            
                            ██░░░░░░░░░░░░██████░░░░░░░░░░░░██                          
                            ██░░░░░░░░░░░░██████░░░░░░░░░░░░██                          
                          ██░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░██                        
                          ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                        
                        ██░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██                      
                        ██░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██                      
                      ██░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░██                    
        ░░            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                    
                        ██████████████████████████████████████████                      
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                  ░░                                                                    
"""

TITLE_FONT = ("TkDefaultFont", 16)


def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()


def lunch(config):
    def change_config():
        clear_window(lunch_window)
        lunch_window.title("Configuration Menu")
        top_label = Label(lunch_window, text="Configuration Menu", font=TITLE_FONT)
        top_label.pack(pady=5)
        sl = Label(lunch_window, text=SHIELD_LOGO)
        sl.pack(pady=5)
        endings_btn = Button(lunch_window, text="Inspect Endings And Names", command=inspect_endings)
        endings_btn.pack(pady=5)
        check_exe_btn = Button(lunch_window, text=f"{'Disable' if config['check_exe'] else 'Enable'} "
                                                  f"execute permission check",
                               command=lambda: change_exe(check_exe_btn))
        check_exe_btn.pack(pady=5)
        lunch_btn = Button(lunch_window, text="Lunch with modified configuration",
                           command=lambda: lunch_window.destroy())
        lunch_btn.pack(pady=5)

    def change_exe(exe_btn):
        toggle = exe_btn.cget("text").split()[0]
        if toggle == "Disable":
            config["check_exe"] = False
            exe_btn.config(text="Enable execute permission check")
        else:  # toggle == Enable
            config["check_exe"] = True
            exe_btn.config(text="Disable execute permission check")

    def inspect_endings():
        clear_window(lunch_window)
        lunch_window.title("Inspect Bad Endings And Names")
        lunch_window.config(padx=10, pady=10)
        back_btn = Button(lunch_window, text="Back To Configuration Menu", command=change_config)
        back_btn.grid(row=0, column=0, columnspan=2, pady=10, sticky=W)
        endings_label = Label(lunch_window, text="Endings:")
        endings_label.grid(row=1, column=0, pady=5, sticky=W, padx=10)
        for i, ending in enumerate(default_config["bad_endings"]):
            var = IntVar()
            checkbox = Checkbutton(lunch_window, text=ending, wraplength=300, variable=var,
                                   command=lambda e=ending, v=var: handle_check(e, v.get(), "bad_endings"))
            checkbox.grid(row=i+2, column=0, pady=5, padx=10, sticky=W)
            if ending in config["bad_endings"]:
                checkbox.select()
        add_e_btn = Button(lunch_window, text="Add ending", command=lambda: add_page("ending"))
        add_e_btn.grid(row=len(default_config["bad_endings"])+2, column=0, pady=5)
        names_label = Label(lunch_window, text="Names:")
        names_label.grid(row=1, column=1, pady=5, sticky=W, padx=10)
        for i, name in enumerate(default_config["bad_names"]):
            var = IntVar()
            checkbox = Checkbutton(lunch_window, text=name, wraplength=300, variable=var,
                                   command=lambda n=name, v=var: handle_check(n, v.get(), "bad_names"))
            checkbox.grid(row=i + 2, column=1, pady=5, padx=10, sticky=W)
            if name in config["bad_names"]:
                checkbox.select()
        add_n_btn = Button(lunch_window, text="Add name", command=lambda: add_page("name"))
        add_n_btn.grid(row=len(default_config["bad_names"]) + 2, column=1, pady=5)

        def add_page(key):
            clear_window(lunch_window)
            ur_ending = Label(lunch_window, text=f"Enter your own {key} below:")
            ur_ending.pack(pady=5)
            entry = Entry(lunch_window)
            entry.pack(pady=5)
            Button(lunch_window, text=f"Add {key}",
                   command=lambda: add_ending(entry.get()) if key == "ending" else add_name(entry.get())).pack(pady=5)

        def add_ending(new_ending):
            if new_ending in default_config["bad_endings"]:
                messagebox.showinfo(title="Ending Exists", message="This ending already exists")
            elif len(new_ending) == 0 or new_ending == ".":
                messagebox.showinfo(title="Invalid Ending", message="An ending cannot be empty")
            elif len(default_config["bad_endings"]) > 15:
                messagebox.showinfo(title="Max Endings", message="Can't have more than 15 endings at a time")
            elif not ending.startswith(".") or ending.count(".") != 1:
                messagebox.showinfo(title="Invalid Ending",
                                    message="Please enter a valid ending\n"
                                            "A valid ending should only contain 1 '.' and it should be it's first char")
            elif ending != ending.lower():
                messagebox.showinfo(title="Invalid Ending", message="Please make sure your ending is all lowercase")
            else:
                default_config["bad_endings"].append(new_ending)
                config["bad_endings"].append(new_ending)
                inspect_endings()

        def add_name(new_name):
            if new_name in default_config["bad_names"]:
                messagebox.showinfo(title="File Name Exists", message="This file name already exists")
            elif len(new_name) == 0:
                messagebox.showinfo(title="Invalid File Name", message="A file name cannot be empty")
            elif len(default_config["bad_names"]) > 15:
                messagebox.showinfo(title="Max Names", message="Can't have more than 15 names at a time")
            elif " " in new_name:
                messagebox.showinfo(title="Invalid File Name", message="File name cant contain whitespace")
            else:
                default_config["bad_names"].append(new_name)
                config["bad_names"].append(new_name)
                inspect_endings()

    def handle_check(e, state, key):
        if state == 1:
            if e not in config[key]:
                config[key].append(e)
        elif e in config[key]:  # remove
            config[key].remove(e)

    default_config = copy.deepcopy(config)
    lunch_window = Tk()
    lunch_window.title("Lunch Window")
    lunch_window.config(padx=5, pady=5)
    lunch_window.minsize(width=200, height=350)
    welcome_label = Label(lunch_window, text="Welcome to the NYK Anti-Virus", font=TITLE_FONT)
    welcome_label.pack(pady=5, padx=10)
    sl = Label(lunch_window, text=SHIELD_LOGO)
    sl.pack(pady=5)
    change_config_btn = Button(lunch_window, text="Manage configuration", command=lambda: change_config())
    change_config_btn.pack(pady=5)
    lunch_btn = Button(lunch_window, text="Lunch with default configuration", command=lambda: lunch_window.destroy())
    lunch_btn.pack(pady=5)
    lunch_window.wait_window()


def start_popup(window):
    popup = Toplevel(window)
    popup.title("Welcome To The Anti Virus")
    avs = Label(popup, text="Anti Virus Starting", font=TITLE_FONT)
    avs.pack(pady=10)
    sl = Label(popup, text=SHIELD_LOGO)
    sl.pack(pady=10)
    ccte = Label(popup, text="Press Ctrl+C To Exit", font=("TkDefaultFont", 12))
    ccte.pack(pady=10)
    popup.after(2000, popup.destroy)
    popup.wait_window()


def end_popup(window):
    popup = Toplevel(window)
    popup.title("Anti Virus Ending")
    ave = Label(popup, text="Anti Virus Ending...", font=TITLE_FONT)
    ave.pack(pady=10)
    sl = Label(popup, text=SHIELD_LOGO)
    sl.pack(pady=10)
    popup.after(2000, popup.destroy)
    popup.wait_window()
    window.destroy()


def menu(pot_threats, on_remove):
    menu_window = Tk()
    menu_window.config(pady=10, padx=10)
    menu_window.title("Menu")
    pages = [pot_threats[i:i+7] for i in range(0, len(pot_threats), 7)]
    page_index = 0

    def handle_remove(selected_f, grid_rows):
        results = on_remove(selected_f)
        if results:
            row_to_name = [row[0] for row in grid_rows]
            remove_me = []
            for j in range(len(results)):
                if results[j]:
                    remove_me.append(selected_f[j])
                    row_index = row_to_name.index(selected_f[j])
                    grid_row = grid_rows[row_index]
                    for element in grid_row[1::]:
                        element.grid_remove()
            for f in remove_me:
                selected_f.remove(f)
                pot_threats.remove(f)

            nonlocal pages, page_index
            pages = pages = [pot_threats[i:i+7] for i in range(0, len(pot_threats), 7)]
            page_index = min(page_index, len(pages)-1)
            clear_window(menu_window)
            display_menu()

    def handle_vt(file_path):
        vt_window = Tk()
        vt_window.config(pady=10, padx=10)
        vt_window.title("VirusTotal Scan")
        loading_label = Label(vt_window, text="Loading...", font=TITLE_FONT)
        loading_label.pack(pady=5)
        mtaw_label = Label(vt_window, text="This might take a while")
        mtaw_label.pack(pady=5)
        vt_window.update()
        output = virustotalhandler.start(file_path)
        clear_window(vt_window)
        if not output or output.get('positives') is None:
            err_label = Label(vt_window, text="There was an error trying to scan this file")
            err_label.pack(pady=5)
        elif output['positives'] == 0:
            safe_label = Label(vt_window, text="According to VirusTotal this file is SAFE", fg="green")
            safe_label.pack(pady=5)
        else:
            Label(vt_window, text=CAUTION).pack(pady=5)
            unsafe_label = Label(vt_window,
                                 text=f"VirusTotal reported {output['positives']} "
                                      f"engines found that this file might be malicious",
                                 fg="red")
            unsafe_label.pack(pady=5)
            url_label = ttk.Label(vt_window, text="For full VirusTotal analysis click here" , cursor="hand2",
                                  foreground="blue")
            url_label.pack()
            url_label.bind("<Button-1>", lambda event: webbrowser.open(output['permalink']))

        vt_window.wait_window()

    def handle_check(checked_path, selected_paths):
        selected_paths.append(checked_path) if checked_path not in selected_paths \
            else selected_paths.remove(checked_path)

    def display_file(file):
        try:
            with open(file, "r") as f:
                content = f.read().strip()
        except Exception as e:
            content = f"Cant read {file}.\nError: {e}"

        display_window = Tk()
        display_window.config(padx=10, pady=10)
        display_window.title(f"Displaying {file}")

        canvas = Canvas(display_window)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = ttk.Scrollbar(display_window, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        content_label = ttk.Label(frame, text=content)
        content_label.pack(pady=5)

        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        # Bind the scrollbar to the canvas
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        display_window.wait_window()

    def put_av_labels():
        av_label = Label(menu_window, text="AntiVirus", font=("TkDefaultFont", 16))
        av_label.grid(row=0, column=0, columnspan=3)

        shield_label = Label(menu_window, text=SHIELD_LOGO)
        shield_label.grid(row=1, column=0, columnspan=3)

    def handle_next():
        nonlocal page_index
        page_index += 1
        clear_window(menu_window)
        display_menu()

    def handle_prev():
        nonlocal page_index
        page_index -= 1
        clear_window(menu_window)
        display_menu()

    def displayable(file):
        try:
            with open(file, "r") as f:
                f.read(10)
                return True
        except Exception:
            return False

    def nav_btns():
        if len(pages) <= 1:
            return 2
        else:
            if page_index < len(pages)-1:
                next_btn = Button(menu_window, text="Next Page", command=handle_next)
                next_btn.grid(row=2, column=2, pady=10, sticky=W)

            if page_index > 0:
                prev_btn = Button(menu_window, text="Prev Page", command=handle_prev)
                prev_btn.grid(row=2, column=0, pady=10, sticky=W)

            return 3

    def display_menu():
        put_av_labels()

        curr_page = pages[page_index]
        selected_files = []  # per page
        rows = []

        base_indent = nav_btns()

        for i in range(len(curr_page)):
            checkbox = Checkbutton(menu_window, text=curr_page[i], wraplength=300,
                                   command=lambda index=i: handle_check(curr_page[index], selected_files))
            checkbox.grid(row=i + base_indent, column=0, pady=5, sticky=W)

            vt_btn = Button(menu_window, text="VirusTotal", command=lambda index=i: handle_vt(curr_page[index]))
            vt_btn.grid(row=i + base_indent, column=2, pady=5, padx=2)

            # trust_btn = Button(window, text="Trust File", command=lambda index=i: print(f"handle_trust({curr_page[index]})"))
            # trust_btn.grid(row=i + base_indent, column=3, pady=5, padx=2)

            if displayable(curr_page[i]):
                display_button = Button(menu_window, text="Display", command=lambda index=i: display_file(curr_page[index]))
                display_button.grid(row=i + base_indent, column=1, pady=5, padx=2)
                rows.append((curr_page[i], checkbox, display_button, vt_btn))
            else:
                rows.append((curr_page[i], checkbox, vt_btn))

        remove_btn = Button(menu_window, text="Remove Selected Files", font=("TkDefaultFont", 13), fg="red",
                            command=lambda: handle_remove(selected_files, rows))
        remove_btn.grid(row=len(curr_page) + base_indent, column=0, pady=5, columnspan=3)

        cont_btn = Button(menu_window, text="End Scan", font=("TkDefaultFont", 13), fg="green",
                          command=lambda: menu_window.destroy())
        cont_btn.grid(row=len(curr_page) + base_indent + 1, column=0, pady=5, columnspan=3)

        menu_window.wait_window()

    display_menu()
