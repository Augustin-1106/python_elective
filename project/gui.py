import tkinter as tk
from tkinter import Frame, Label, END, Entry, Text, VERTICAL, Button, messagebox  # Tkinter Python
# Module for GUI
from client import msg_queue, send
from tkinter import messagebox


def receive_id():
    new_window = tk.Toplevel(root, width=500, height=500)

    # Create a label and an entry field
    label = tk.Label(new_window, text="Enter ID:")
    entry = tk.Entry(new_window)
    label.pack()
    entry.pack()

    # Function to add the ID
    def enter_id():
        user_id = entry.get()
        send("!ID:" + user_id)
        new_window.destroy()  # Close the window after adding the id

    # Create the 'Enter ID' button
    enter_id_button = tk.Button(new_window, text="Enter ID", command=enter_id)
    enter_id_button.pack()


class MessageApp:

    def __init__(self, master):
        self.enter_text_widget = None
        self.chat_transcript_area = None
        self.join_button = None
        self.disconnect_button = None
        self.name_widget = None
        self.connectionlist = []
        self.root = master
        self.initialise_gui()

    def initialise_gui(self):
        self.root.title("Messenger")
        self.root.resizable(0, 0)

        self.display_chat_box()
        self.display_name_section()
        self.display_chat_entry_box()

        receive_id()

    def display_name_section(self):
        frame = Frame()
        Label(frame, text='To:', font=("Helvetica", 16)).pack(side='left', padx=10)
        self.name_widget = Entry(frame, width=50, borderwidth=2)
        self.name_widget.pack(side='left', anchor='e')

        self.join_button = Button(frame, text="Connect", width=10, command=self.connect_contact)
        self.join_button.pack(side='left')

        self.disconnect_button = Button(frame, text="Disconnect", width=10, command=self.disconnect_contact, state='disabled')
        self.disconnect_button.pack(side='left')

        frame.pack(side='top', anchor='nw')

    def display_chat_box(self):
        frame = tk.Frame()
        label = tk.Label(frame, text='Chat Box:', font=("Serif", 12))
        label.pack(side='top', anchor='w')

        self.chat_transcript_area = tk.Text(frame, width=60, height=10, font=("Serif", 12))  # The multi-line chat box where messages are displayed

        scrollbar = tk.Scrollbar(frame, command=self.chat_transcript_area.yview, orient=VERTICAL)
        self.chat_transcript_area.config(yscrollcommand=scrollbar.set)  # Enables the scrollbar to scroll the chat box

        self.chat_transcript_area.bind('<KeyPress>', lambda e: 'break')  # Prevents the user from typing in the chat box

        self.chat_transcript_area.pack(side='left', padx=10)

        scrollbar.pack(side='right', fill='y')
        frame.pack(side='top')

    def display_chat_entry_box(self):
        frame = Frame()
        Label(frame, text='Enter message:', font=("Serif", 12)).pack(side='top', anchor='w')
        self.enter_text_widget = Text(frame, width=60, height=3, font=("Serif", 12))

        self.enter_text_widget.pack(side='left', pady=15)
        self.enter_text_widget.bind('<Return>', self.on_enter_key_pressed)
        frame.pack(side='top')

    def disconnect_contact(self):

        self.name_widget.config(state='normal')
        self.join_button.config(state='normal')
        self.disconnect_button.config(state='disabled')

        for id in self.connectionlist:
            print("Disconnecting from " + id)
            send("!DISCONNECT:" + id)
        self.connectionlist = []

    def connect_contact(self):

        if len(self.name_widget.get()) == 0:
            messagebox.showerror("Enter TO ID", "Enter 'TO ID' to send a message")
            return

        self.connectionlist = self.name_widget.get().split(',')

        self.name_widget.config(state='disabled')
        self.join_button.config(state='disabled')
        self.disconnect_button.config(state='normal')

        for id in self.connectionlist:
            send("!CONNECT:" + id)

    def on_enter_key_pressed(self, event):
        if len(self.name_widget.get()) == 0:
            messagebox.showerror("Enter to ID", "Enter ID to send a message")
            return
        self.send_chat()
        self.clear_text()

    def clear_text(self):
        self.enter_text_widget.delete(1.0, 'end')

    def send_chat(self):
        data = self.enter_text_widget.get(1.0, 'end').strip()
        send(data)
        self.chat_transcript_area.insert('end', 'You:' + data + '\n')
        self.chat_transcript_area.yview(END)

        self.enter_text_widget.delete(1.0, 'end')
        return 'break'

    def receive_chat(self):
        while not msg_queue.empty():
            print("recive Chat")
            data = msg_queue.get()
            self.chat_transcript_area.insert('end', data + '\n')
            self.chat_transcript_area.yview(END)
        root.after(1000, self.receive_chat)

    def on_close_window(self):
        send("!DISCONNECT")
        self.root.destroy()
        exit(0)

root = tk.Tk()
gui = MessageApp(root)
gui.receive_chat()
root.protocol("WM_DELETE_WINDOW", gui.on_close_window)
root.mainloop()