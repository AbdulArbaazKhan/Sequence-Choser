import os
from tkinter.filedialog import askdirectory
from tkinter import *

root_width = 800


def main():
    global root_width

    def rename():
        def back():
            root.destroy()
            main()

        def perform_rename():
            f = 0
            for entry in all_files[1]:
                os.rename(f"{os.getcwd()}/{all_files[0][f]}", f"{os.getcwd()}/{entry.get()}")
                f += 1
            root.destroy()
            main()

        all_files = order()
        Button(root, text="Next", command=perform_rename, fg="white", bg="black", relief=GROOVE, width=10,
               height=2, font='timesnewroman 12').place(x=0, y=592)
        Button(root, text="Back", command=back, fg="white", bg="black", relief=GROOVE, width=10,
               height=2, font='timesnewroman 12').place(x=800, y=590)

    def order():
        global root_width
        path = askdirectory()
        os.chdir(path)
        if path:
            all_files = os.listdir(path)
            file_frame = Frame(bg="black")
            c = 0
            r = 0
            all_files_entries = []
            for i in range(len(all_files)):
                variable = StringVar()
                variable.set(all_files[i])
                names = Entry(file_frame, font="timesnewroman 16", relief=RAISED, textvariable=variable, width=35,
                              borderwidth=4, fg="red", bg="black")
                names.grid(column=c, row=r, pady=4, sticky="w", padx=5)
                all_files_entries.append(variable)
                r += 1
                if i % 10 == 9:
                    root_width += 200
                    root.geometry(f"{root_width}x700")
                    c += 1
                    r = 0

            file_frame.pack(pady=50, anchor=NW)

            rename_btn.forget()
        else:
            pass
        return all_files, all_files_entries

    root = Tk()
    root.config(bg="black")
    root.title("Sequence Builder")

    root.geometry(f"{root_width}x700")
    main_label = Label(root, text="Manage Your Sequence", font="timesnewroman 20 bold")
    main_label.pack()
    rename_btn = Button(root, text="Rename Files", fg="white", bg="black", relief=GROOVE, width=12,
                        height=2, command=rename, font='timesnewroman 12')
    rename_btn.pack(pady=80)
    root.mainloop()


"""
        if path:
            all_files = os.listdir(path)
            file_frame = Frame(bg="black")
            all_files_entries = []
            c = 0
            r = 0

            print(len(all_files))

            if len(all_files) % 2 == 0:
                x = 1
                for i in range(len(all_files)):
                    if x > len(all_files) // 2:
                        c += 1
                        r = 0
                        x = 1
                    variable = StringVar()
                    variable.set(all_files[i])
                    names = Entry(file_frame, font="timesnewroman 16", relief=GROOVE, textvariable=variable, width=30,
                                  borderwidth=4, fg="white", bg="black")
                    names.grid(column=c, row=r, pady=3, sticky="w", padx=5)
                    all_files_entries.append(variable)
                    r += 1
                    x += 1
            else:
                pass
                
                
                
                
                if path:
            all_files = os.path.basename()
            file_frame = Frame(bg="black")
            all_files_entries = []
            c = 0
            r = 0
            print(len(all_files))
            for i in range(len(all_files)):
                variable = StringVar()
                variable.set(all_files[i])
                names = Entry(file_frame, font="timesnewroman 16", relief=RAISED, textvariable=variable, width=35,
                              borderwidth=4, fg="red", bg="black")
                names.grid(column=c, row=r, pady=4, sticky="w", padx=5)
                all_files_entries.append(variable)
                r += 1
                if i % 10 == 9:
                    c += 1
                    r = 0

            file_frame.pack(pady=50, anchor=N)
            Button(root, text="Next", command=rename, fg="white", bg="black", relief=GROOVE, width=10,
                   height=2, font='timesnewroman 12').place(x=0, y=592)
            Button(root, text="Back", command=back, fg="white", bg="black", relief=GROOVE, width=10,
                   height=2, font='timesnewroman 12').place(x=800, y=590)
            get_directory.forget()
        else:
            pass

"""

if __name__ == '__main__':
    main()
