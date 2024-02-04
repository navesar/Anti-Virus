import virustotalhandler
import webbrowser
from tkinter import Label, Button, Toplevel, Tk, Checkbutton, W, ttk, Canvas, LEFT, BOTH, RIGHT, Y

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


def start_popup(window):
    popup = Toplevel(window)
    popup.title("Welcome To The Anti Virus")
    avs = Label(popup, text="Anti Virus Starting", font=("TkDefaultFont", 16))
    avs.pack(pady=10)
    sl = Label(popup, text=SHIELD_LOGO)
    sl.pack(pady=10)
    ccte = Label(popup, text="Press Ctrl+C To Exit", font=("TkDefaultFont", 12))
    ccte.pack(pady=10)
    popup.after(2000, popup.destroy)
    popup.wait_window()


def end_popup(window):  # does not work yet
    print("start ending...")
    popup = Toplevel(window)
    popup.title("Anti Virus Ending")
    ave = Label(popup, text="Anti Virus Ending...", font=("TkDefaultFont", 16))
    ave.pack(pady=10)
    sl = Label(popup, text=SHIELD_LOGO)
    sl.pack(pady=10)
    # Close the popup after 2000 milliseconds (2 seconds)
    popup.after(2000, popup.destroy)
    popup.wait_window()
    window.destroy()
    print("end ending...")

def menu(pot_threats, on_remove):
    window = Tk()
    window.config(pady=10, padx=10)
    window.title("Menu")
    pages = [pot_threats[i:i+7] for i in range(0, len(pot_threats), 7)]
    page_index = 0

    def clear_window():
        for widget in window.winfo_children():
            widget.destroy()
    
    def end_window():
        put_av_labels()
        end_label = Label(window, text="You have dealt with all pot threats!")
        end_label.grid(row=2, column=0, columnspan=3)
        ok_btn = Button(window, text="OK", command=lambda: window.destroy())
        ok_btn.grid(row=3, column=0, columnspan=3)

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
            clear_window()
            if len(pages) > 0:
                page_index = min(page_index, len(pages)-1)
                display_menu()
            else:
                end_window()

    def handle_vt(file_path):
        output = virustotalhandler.start(file_path)
        vt_window = Tk()
        vt_window.config(pady=10, padx=10)
        vt_window.title("VirusTotal Scan")
        if not output or output.get('positives') is None:
            err_label = Label(vt_window, text="There was an error trying to scan this file")
            err_label.pack()
        elif output['positives'] == 0:
            safe_label = Label(vt_window, text="According to VirusTotal this file is SAFE", fg="green")
            safe_label.pack()
        else:
            unsafe_label = Label(vt_window,
                                 text=f"VirusTotal reported {output['positives']} "
                                      f"engines found that this file might be malicious",
                                 fg="red")
            unsafe_label.pack()
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
        av_label = Label(window, text="AntiVirus", font=("TkDefaultFont", 16))
        av_label.grid(row=0, column=0, columnspan=3)

        shield_label = Label(window, text=SHIELD_LOGO)
        shield_label.grid(row=1, column=0, columnspan=3)

    def handle_next():
        nonlocal page_index
        page_index += 1
        clear_window()
        display_menu()

    def handle_prev():
        nonlocal page_index
        page_index -= 1
        clear_window()
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
                next_btn = Button(window, text="Next Page", command=handle_next)
                next_btn.grid(row=2, column=2, pady=10, sticky=W)

            if page_index > 0:
                prev_btn = Button(window, text="Prev Page", command=handle_prev)
                prev_btn.grid(row=2, column=0, pady=10, sticky=W)

            return 3

    def display_menu():
        put_av_labels()

        curr_page = pages[page_index]
        selected_files = []  # per page
        rows = []

        base_indent = nav_btns()

        for i in range(len(curr_page)):
            checkbox = Checkbutton(window, text=curr_page[i], wraplength=300,
                                   command=lambda index=i: handle_check(curr_page[index], selected_files))
            checkbox.grid(row=i + base_indent, column=0, pady=5, sticky=W)

            vt_btn = Button(window, text="VirusTotal", command=lambda index=i: handle_vt(curr_page[index]))
            vt_btn.grid(row=i + base_indent, column=2, pady=5, padx=2)

            # trust_btn = Button(window, text="Trust File", command=lambda index=i: print(f"handle_trust({curr_page[index]})"))
            # trust_btn.grid(row=i + base_indent, column=3, pady=5, padx=2)

            if displayable(curr_page[i]):
                display_button = Button(window, text="Display", command=lambda index=i: display_file(curr_page[index]))
                display_button.grid(row=i + base_indent, column=1, pady=5, padx=2)
                rows.append((curr_page[i], checkbox, display_button, vt_btn))
            else:
                rows.append((curr_page[i], checkbox, vt_btn))

        remove_btn = Button(window, text="Remove Selected Files", font=("TkDefaultFont", 13), fg="red",
                            command=lambda: handle_remove(selected_files, rows))
        remove_btn.grid(row=len(curr_page) + base_indent, column=0, pady=5, columnspan=3)

        cont_btn = Button(window, text="End Scan", font=("TkDefaultFont", 13), fg="green",
                          command=lambda: window.destroy())
        cont_btn.grid(row=len(curr_page) + base_indent + 1, column=0, pady=5, columnspan=3)

        window.wait_window()

    display_menu()
