# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt


class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikacja do rysowania wykresu na podtawie wprowadzonych danych")
        self.master.geometry("500x300")

        self.data_source_label = tk.Label(self.master, text="Wybierz źródło danych:")
        self.data_source_label.pack(pady=10)

        self.manual_button = tk.Button(self.master, text="Wpisz dane ręcznie", command=self.manual_input)
        self.manual_button.pack(pady=5)

        self.import_button = tk.Button(self.master, text="Zaimportuj dane", command=self.import_data)
        self.import_button.pack(pady=5)

    def manual_input(self):
        self.manual_button.pack_forget()
        self.import_button.pack_forget()
        self.data_source_label.pack_forget()

        self.x_label = tk.Label(self.master, text="Wprowadź wartości x (oddzielone przecinkami):")
        self.x_label.pack(pady=10)

        self.x_entry = tk.Entry(self.master)
        self.x_entry.pack(pady=5)

        self.y_label = tk.Label(self.master, text="Wprowadź wartości y (oddzielone przecinkami):")
        self.y_label.pack(pady=10)

        self.y_entry = tk.Entry(self.master)
        self.y_entry.pack(pady=5)

        self.plot_button = tk.Button(self.master, text="Narysuj wykres", command=self.plot_data)
        self.plot_button.pack(pady=10)

    def import_data(self):
        self.manual_button.pack_forget()
        self.import_button.pack_forget()
        self.data_source_label.pack_forget()

        self.filename = filedialog.askopenfilename(initialdir="./", title="Wybierz plik z danymi", filetypes=(("Pliki CSV", "*.csv"), ("Wszystkie pliki", "*.*")))
        self.data = np.loadtxt(self.filename, delimiter=",", skiprows=1)

        self.plot_data()

    def plot_data(self):
        if hasattr(self, "x_entry"):
            x_str = self.x_entry.get()
            y_str = self.y_entry.get()
            x = np.array([float(i.strip()) for i in x_str.split(",")])
            y = np.array([float(i.strip()) for i in y_str.split(",")])
        else:
            x = self.data[:, 0]
            y = self.data[:, 1]

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Wykres danych")

        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
