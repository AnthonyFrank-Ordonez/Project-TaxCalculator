import customtkinter as ctk


class TaxCalculator:
    def __init__(self, percent: int):
        self.window = ctk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry('300x280')
        self.window.resizable(False, False)
        self.percent = percent

        # Labels
        self.salary_label = ctk.CTkLabel(self.window, text='Salary:', font=('...', 15))
        self.percent_label = ctk.CTkLabel(self.window, text='Percent:', font=('...', 15))
        self.tax_label = ctk.CTkLabel(self.window, text='Tax:', font=('...', 15))

        # Entries
        self.salary_entry = ctk.CTkEntry(self.window, placeholder_text='Salary', width=180)
        self.percent_entry = ctk.CTkEntry(self.window, placeholder_text='Percent', width=180)
        self.tax_entry = ctk.CTkEntry(self.window, width=180, placeholder_text='₱0')
        self.tax_entry_locked()

        # button
        self.calculate_btn = ctk.CTkButton(self.window, text='Calculate', width=180, height=35,
                                           command=self.calculate_salary)

        self.clear_btn = ctk.CTkButton(self.window, text='Clear', width=180, height=35,
                                       command=self.clear_input)

        # set up grid
        self.salary_label.grid(row=1, column=0, padx=20, pady=20)
        self.salary_entry.grid(row=1, column=1)
        self.percent_label.grid(row=2, column=0, padx=20)
        self.percent_entry.grid(row=2, column=1)
        self.tax_label.grid(row=3, column=0, pady=20)
        self.tax_entry.grid(row=3, column=1)
        self.calculate_btn.grid(row=4, column=1)
        self.clear_btn.grid(row=5, column=1, pady=15)

    def calculate_salary(self):
        """Calculate the salary with tax"""
        try:
            self.tax_entry_unlocked()
            salary: float = float(self.salary_entry.get())
            tax: float = float(self.percent_entry.get()) / self.percent

            self.tax_entry.delete(0, "end")
            calculated_salary: float = tax * salary
            self.tax_entry.insert(0, f"₱{calculated_salary:,.2f}")
            self.tax_entry_locked()

        # catch ValueError Exception if it occurs
        except ValueError:
            self.tax_entry.delete(0, "end")
            self.tax_entry.insert(0, 'INVALID INPUT')

    def clear_input(self):
        """Clear all the entries in ctk entry"""
        self.tax_entry_unlocked()
        self.salary_entry.delete(0, 'end')
        self.percent_entry.delete(0, 'end')
        self.tax_entry.delete(0, 'end')
        self.tax_entry_locked()

    def tax_entry_locked(self):
        """Locked the state of the Tax Entry"""
        self.tax_entry.configure(state=ctk.DISABLED)

    def tax_entry_unlocked(self):
        """Unlocked the state of the Tax Entry"""
        self.tax_entry.configure(state=ctk.NORMAL)

    def run_app(self):
        """Run the app"""
        self.window.mainloop()


def main():
    app = TaxCalculator(100)
    app.run_app()


if __name__ == '__main__':
    main()