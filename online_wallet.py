import json
import hashlib
import tkinter as tk
from tkinter import messagebox
import winsound


# =========================
# COLORS
# =========================

BG = "#0B1120"
CARD = "#111827"
CARD_LIGHT = "#172033"
TEXT = "#F8FAFC"
MUTED = "#94A3B8"
GREEN = "#22C55E"
RED = "#EF4444"
BLUE = "#3B82F6"
BORDER = "#263247"


# =========================
# DATA
# =========================

categories = [
    "food",
    "transport",
    "entertainment",
    "shopping",
    "bills",
    "other"
]

balance = {
    "dollar": 100
}

transactions = []
pin_hash = None


# =========================
# SOUNDS
# =========================

def sound_success():
    winsound.MessageBeep(winsound.MB_OK)


def sound_error():
    winsound.MessageBeep(winsound.MB_ICONHAND)


def sound_warning():
    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)


def sound_click():
    winsound.Beep(700, 40)


# =========================
# SECURITY
# =========================

def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()


# =========================
# SAVE / LOAD
# =========================

def save_data():
    data = {
        "balance": balance,
        "transactions": transactions,
        "pin_hash": pin_hash
    }

    with open("wallet_data.json", "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    global balance
    global transactions
    global pin_hash

    try:
        with open("wallet_data.json", "r") as file:
            data = json.load(file)

        balance = data.get(
            "balance",
            {"dollar": 100}
        )

        transactions = data.get(
            "transactions",
            []
        )

        pin_hash = data.get(
            "pin_hash"
        )

    except FileNotFoundError:
        pin_hash = None


# =========================
# HELPERS
# =========================

def calculate_totals():

    income = 0
    expenses = 0

    for transaction in transactions:

        if transaction["type"] == "income":
            income += transaction["amount"]

        else:
            expenses += transaction["amount"]

    return income, expenses


def clear_frame(frame):

    for widget in frame.winfo_children():
        widget.destroy()


# =========================
# MAIN WINDOW
# =========================

def create_main_window():

    global window
    global balance_label
    global income_value
    global expense_value
    global recent_frame
    global amount_entry
    global category_entry

    window = tk.Tk()

    window.title("Wallet")
    window.geometry("1000x720")
    window.minsize(900, 650)
    window.configure(
        bg=BG
    )

    # =========================
    # HEADER
    # =========================

    header = tk.Frame(
        window,
        bg=BG
    )

    header.pack(
        fill="x",
        padx=45,
        pady=(30, 10)
    )

    title = tk.Label(
        header,
        text="WALLET",
        font=("Segoe UI", 28, "bold"),
        bg=BG,
        fg=TEXT
    )

    title.pack(
        side="left"
    )

    secure = tk.Label(
        header,
        text="● SECURE",
        font=("Segoe UI", 10, "bold"),
        bg=BG,
        fg=GREEN
    )

    secure.pack(
        side="right",
        pady=10
    )

    subtitle = tk.Label(
        window,
        text="Your personal finance dashboard",
        font=("Segoe UI", 11),
        bg=BG,
        fg=MUTED
    )

    subtitle.pack(
        anchor="w",
        padx=48
    )

    # =========================
    # BALANCE CARD
    # =========================

    balance_card = tk.Frame(
        window,
        bg=CARD,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    balance_card.pack(
        fill="x",
        padx=45,
        pady=25
    )

    balance_title = tk.Label(
        balance_card,
        text="CURRENT BALANCE",
        font=("Segoe UI", 10, "bold"),
        bg=CARD,
        fg=MUTED
    )

    balance_title.pack(
        anchor="w",
        padx=30,
        pady=(25, 5)
    )

    balance_label = tk.Label(
        balance_card,
        text=f"${balance['dollar']}",
        font=("Segoe UI", 38, "bold"),
        bg=CARD,
        fg=TEXT
    )

    balance_label.pack(
        anchor="w",
        padx=30
    )

    # =========================
    # INCOME / EXPENSE
    # =========================

    stats_frame = tk.Frame(
        balance_card,
        bg=CARD
    )

    stats_frame.pack(
        fill="x",
        padx=30,
        pady=(20, 25)
    )

    income, expenses = calculate_totals()

    income_box = tk.Frame(
        stats_frame,
        bg="#10251A"
    )

    income_box.pack(
        side="left",
        fill="x",
        expand=True,
        padx=(0, 8)
    )

    tk.Label(
        income_box,
        text="↑  TOTAL INCOME",
        font=("Segoe UI", 9, "bold"),
        bg="#10251A",
        fg=GREEN
    ).pack(
        anchor="w",
        padx=18,
        pady=(12, 3)
    )

    income_value = tk.Label(
        income_box,
        text=f"${income}",
        font=("Segoe UI", 18, "bold"),
        bg="#10251A",
        fg=TEXT
    )

    income_value.pack(
        anchor="w",
        padx=18,
        pady=(0, 12)
    )

    expense_box = tk.Frame(
        stats_frame,
        bg="#291315"
    )

    expense_box.pack(
        side="left",
        fill="x",
        expand=True,
        padx=(8, 0)
    )

    tk.Label(
        expense_box,
        text="↓  TOTAL EXPENSES",
        font=("Segoe UI", 9, "bold"),
        bg="#291315",
        fg=RED
    ).pack(
        anchor="w",
        padx=18,
        pady=(12, 3)
    )

    expense_value = tk.Label(
        expense_box,
        text=f"${expenses}",
        font=("Segoe UI", 18, "bold"),
        bg="#291315",
        fg=TEXT
    )

    expense_value.pack(
        anchor="w",
        padx=18,
        pady=(0, 12)
    )

    # =========================
    # QUICK ACTIONS
    # =========================

    action_frame = tk.Frame(
        window,
        bg=BG
    )

    action_frame.pack(
        fill="x",
        padx=45
    )

    tk.Label(
        action_frame,
        text="QUICK ACTIONS",
        font=("Segoe UI", 10, "bold"),
        bg=BG,
        fg=MUTED
    ).pack(
        anchor="w",
        pady=(0, 10)
    )

    input_frame = tk.Frame(
        action_frame,
        bg=BG
    )

    input_frame.pack(
        fill="x"
    )

    amount_entry = tk.Entry(
        input_frame,
        font=("Segoe UI", 12),
        bg=CARD,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat"
    )

    amount_entry.pack(
        side="left",
        fill="x",
        expand=True,
        ipady=10,
        padx=(0, 8)
    )

    amount_entry.insert(
        0,
        "Amount"
    )

    def clear_amount(event):
        if amount_entry.get() == "Amount":
            amount_entry.delete(
                0,
                tk.END
            )

    amount_entry.bind(
        "<FocusIn>",
        clear_amount
    )

    category_entry = tk.Entry(
        input_frame,
        font=("Segoe UI", 12),
        bg=CARD,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat"
    )

    category_entry.pack(
        side="left",
        fill="x",
        expand=True,
        ipady=10,
        padx=8
    )

    category_entry.insert(
        0,
        "Category"
    )

    def clear_category(event):
        if category_entry.get() == "Category":
            category_entry.delete(
                0,
                tk.END
            )

    category_entry.bind(
        "<FocusIn>",
        clear_category
    )

    income_button = tk.Button(
        input_frame,
        text="＋ Income",
        command=add_income,
        bg=GREEN,
        fg="#06100A",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        cursor="hand2"
    )

    income_button.pack(
        side="left",
        padx=8,
        ipadx=15,
        ipady=8
    )

    expense_button = tk.Button(
        input_frame,
        text="− Expense",
        command=add_expense,
        bg=RED,
        fg="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        cursor="hand2"
    )

    expense_button.pack(
        side="left",
        padx=(8, 0),
        ipadx=15,
        ipady=8
    )

    # =========================
    # LOWER AREA
    # =========================

    lower = tk.Frame(
        window,
        bg=BG
    )

    lower.pack(
        fill="both",
        expand=True,
        padx=45,
        pady=25
    )

    # =========================
    # RECENT TRANSACTIONS
    # =========================

    recent_card = tk.Frame(
        lower,
        bg=CARD,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    recent_card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 10)
    )

    recent_header = tk.Frame(
        recent_card,
        bg=CARD
    )

    recent_header.pack(
        fill="x",
        padx=20,
        pady=18
    )

    tk.Label(
        recent_header,
        text="Recent transactions",
        font=("Segoe UI", 14, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(
        side="left"
    )

    tk.Button(
        recent_header,
        text="View all",
        command=view_transactions,
        bg=CARD,
        fg=BLUE,
        activebackground=CARD,
        activeforeground=BLUE,
        relief="flat",
        cursor="hand2"
    ).pack(
        side="right"
    )

    recent_frame = tk.Frame(
        recent_card,
        bg=CARD
    )

    recent_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 20)
    )

    update_recent_transactions()

    # =========================
    # TOOLS
    # =========================

    menu_card = tk.Frame(
        lower,
        bg=CARD,
        width=230,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    menu_card.pack(
        side="right",
        fill="y"
    )

    menu_card.pack_propagate(
        False
    )

    tk.Label(
        menu_card,
        text="TOOLS",
        font=("Segoe UI", 10, "bold"),
        bg=CARD,
        fg=MUTED
    ).pack(
        anchor="w",
        padx=20,
        pady=(20, 12)
    )

    create_menu_button(
        menu_card,
        "▣  Transactions",
        view_transactions
    )

    create_menu_button(
        menu_card,
        "◈  Statistics",
        view_statistics
    )

    create_menu_button(
        menu_card,
        "⌕  Search",
        open_search
    )

    create_menu_button(
        menu_card,
        "↻  Refresh",
        refresh_dashboard
    )

    window.mainloop()


# =========================
# MENU BUTTON
# =========================

def create_menu_button(
    parent,
    text,
    command
):

    button = tk.Button(
        parent,
        text=text,
        command=lambda: (
            sound_click(),
            command()
        ),
        anchor="w",
        bg=CARD_LIGHT,
        fg=TEXT,
        activebackground=BLUE,
        activeforeground="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        cursor="hand2"
    )

    button.pack(
        fill="x",
        padx=15,
        pady=5,
        ipady=10
    )


# =========================
# DASHBOARD UPDATE
# =========================

def refresh_dashboard():

    income, expenses = calculate_totals()

    balance_label.config(
        text=f"${balance['dollar']}"
    )

    income_value.config(
        text=f"${income}"
    )

    expense_value.config(
        text=f"${expenses}"
    )

    update_recent_transactions()


def update_recent_transactions():

    clear_frame(
        recent_frame
    )

    if not transactions:

        tk.Label(
            recent_frame,
            text="No transactions yet.",
            font=("Segoe UI", 11),
            bg=CARD,
            fg=MUTED
        ).pack(
            pady=30
        )

        return

    recent = transactions[-5:]
    recent.reverse()

    for transaction in recent:

        row = tk.Frame(
            recent_frame,
            bg=CARD
        )

        row.pack(
            fill="x",
            pady=5
        )

        if transaction["type"] == "income":

            symbol = "↑"
            color = GREEN
            amount = f"+${transaction['amount']}"
            name = "Income"

        else:

            symbol = "↓"
            color = RED
            amount = f"-${transaction['amount']}"
            name = transaction[
                "category"
            ].capitalize()

        tk.Label(
            row,
            text=symbol,
            font=("Segoe UI", 16, "bold"),
            bg=CARD,
            fg=color,
            width=3
        ).pack(
            side="left"
        )

        tk.Label(
            row,
            text=name,
            font=("Segoe UI", 11, "bold"),
            bg=CARD,
            fg=TEXT
        ).pack(
            side="left"
        )

        tk.Label(
            row,
            text=amount,
            font=("Segoe UI", 11, "bold"),
            bg=CARD,
            fg=color
        ).pack(
            side="right"
        )


# =========================
# INCOME
# =========================

def add_income():

    sound_click()

    try:

        amount = int(
            amount_entry.get()
        )

        if amount <= 0:

            sound_error()

            messagebox.showerror(
                "Invalid amount",
                "Amount must be greater than 0."
            )

            return

        balance["dollar"] += amount

        transactions.append({
            "type": "income",
            "amount": amount,
            "category": "income"
        })

        save_data()

        amount_entry.delete(
            0,
            tk.END
        )

        refresh_dashboard()

        sound_success()

        messagebox.showinfo(
            "Income added",
            f"${amount} added successfully."
        )

    except ValueError:

        sound_error()

        messagebox.showerror(
            "Invalid amount",
            "Please enter a valid number."
        )


# =========================
# EXPENSE
# =========================

def add_expense():

    sound_click()

    try:

        amount = int(
            amount_entry.get()
        )

        if amount <= 0:

            sound_error()

            messagebox.showerror(
                "Invalid amount",
                "Amount must be greater than 0."
            )

            return

        if amount > balance["dollar"]:

            sound_warning()

            messagebox.showerror(
                "Insufficient funds",
                "You don't have enough money."
            )

            return

        category = (
            category_entry
            .get()
            .lower()
            .strip()
        )

        if category == "category":
            category = ""

        if category not in categories:

            sound_error()

            messagebox.showerror(
                "Invalid category",
                "Use one of:\n\n"
                + ", ".join(categories)
            )

            return

        balance["dollar"] -= amount

        transactions.append({
            "type": "expense",
            "amount": amount,
            "category": category
        })

        save_data()

        amount_entry.delete(
            0,
            tk.END
        )

        category_entry.delete(
            0,
            tk.END
        )

        refresh_dashboard()

        sound_success()

        messagebox.showinfo(
            "Expense added",
            f"${amount} spent on {category}."
        )

    except ValueError:

        sound_error()

        messagebox.showerror(
            "Invalid amount",
            "Please enter a valid number."
        )


# =========================
# TRANSACTIONS
# =========================

def view_transactions():

    sound_click()

    transaction_window = tk.Toplevel(
        window
    )

    transaction_window.title(
        "Transactions"
    )

    transaction_window.geometry(
        "650x550"
    )

    transaction_window.configure(
        bg=BG
    )

    tk.Label(
        transaction_window,
        text="Transaction History",
        font=("Segoe UI", 22, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 5)
    )

    tk.Label(
        transaction_window,
        text=f"{len(transactions)} transactions",
        font=("Segoe UI", 10),
        bg=BG,
        fg=MUTED
    ).pack(
        anchor="w",
        padx=30,
        pady=(0, 20)
    )

    listbox = tk.Listbox(
        transaction_window,
        bg=CARD,
        fg=TEXT,
        font=("Segoe UI", 11),
        relief="flat",
        selectbackground=BLUE,
        borderwidth=0
    )

    listbox.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(0, 30)
    )

    if not transactions:

        listbox.insert(
            tk.END,
            "No transactions yet."
        )

    else:

        for transaction in reversed(
            transactions
        ):

            if transaction["type"] == "income":

                text = (
                    f"  ↑  +${transaction['amount']}"
                    f"     Income"
                )

            else:

                text = (
                    f"  ↓  -${transaction['amount']}"
                    f"     "
                    f"{transaction['category'].capitalize()}"
                )

            listbox.insert(
                tk.END,
                text
            )


# =========================
# STATISTICS
# =========================

def view_statistics():

    sound_click()

    income, expenses = (
        calculate_totals()
    )

    stats_window = tk.Toplevel(
        window
    )

    stats_window.title(
        "Statistics"
    )

    stats_window.geometry(
        "550x600"
    )

    stats_window.configure(
        bg=BG
    )

    tk.Label(
        stats_window,
        text="Statistics",
        font=("Segoe UI", 24, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 20)
    )

    create_stat_card(
        stats_window,
        "TOTAL INCOME",
        f"${income}",
        GREEN
    )

    create_stat_card(
        stats_window,
        "TOTAL EXPENSES",
        f"${expenses}",
        RED
    )

    tk.Label(
        stats_window,
        text="Expenses by category",
        font=("Segoe UI", 14, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 10)
    )

    category_totals = {}

    for transaction in transactions:

        if transaction["type"] == "expense":

            category = transaction[
                "category"
            ]

            category_totals[
                category
            ] = (
                category_totals.get(
                    category,
                    0
                )
                + transaction["amount"]
            )

    for category, amount in (
        category_totals.items()
    ):

        row = tk.Frame(
            stats_window,
            bg=CARD
        )

        row.pack(
            fill="x",
            padx=30,
            pady=4
        )

        tk.Label(
            row,
            text=category.capitalize(),
            font=("Segoe UI", 11),
            bg=CARD,
            fg=TEXT
        ).pack(
            side="left",
            padx=15,
            pady=10
        )

        tk.Label(
            row,
            text=f"${amount}",
            font=("Segoe UI", 11, "bold"),
            bg=CARD,
            fg=RED
        ).pack(
            side="right",
            padx=15
        )


def create_stat_card(
    parent,
    title,
    value,
    color
):

    card = tk.Frame(
        parent,
        bg=CARD
    )

    card.pack(
        fill="x",
        padx=30,
        pady=5
    )

    tk.Label(
        card,
        text=title,
        font=("Segoe UI", 9, "bold"),
        bg=CARD,
        fg=MUTED
    ).pack(
        anchor="w",
        padx=18,
        pady=(12, 0)
    )

    tk.Label(
        card,
        text=value,
        font=("Segoe UI", 20, "bold"),
        bg=CARD,
        fg=color
    ).pack(
        anchor="w",
        padx=18,
        pady=(2, 12)
    )


# =========================
# SEARCH
# =========================

def open_search():

    sound_click()

    search_window = tk.Toplevel(
        window
    )

    search_window.title(
        "Search"
    )

    search_window.geometry(
        "600x500"
    )

    search_window.configure(
        bg=BG
    )

    tk.Label(
        search_window,
        text="Search transactions",
        font=("Segoe UI", 22, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 15)
    )

    search_entry = tk.Entry(
        search_window,
        font=("Segoe UI", 12),
        bg=CARD,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat"
    )

    search_entry.pack(
        fill="x",
        padx=30,
        ipady=10
    )

    results = tk.Listbox(
        search_window,
        bg=CARD,
        fg=TEXT,
        font=("Segoe UI", 11),
        relief="flat",
        selectbackground=BLUE
    )

    results.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=20
    )

    def search():

        sound_click()

        results.delete(
            0,
            tk.END
        )

        search_text = (
            search_entry
            .get()
            .lower()
            .strip()
        )

        for transaction in transactions:

            category = (
                transaction["category"]
                .lower()
            )

            if search_text in category:

                if transaction["type"] == "income":

                    text = (
                        f"+${transaction['amount']}"
                        f" | Income"
                    )

                else:

                    text = (
                        f"-${transaction['amount']}"
                        f" | "
                        f"{transaction['category']}"
                    )

                results.insert(
                    tk.END,
                    text
                )

        if results.size() == 0:

            results.insert(
                tk.END,
                "No transactions found."
            )

    tk.Button(
        search_window,
        text="Search",
        command=search,
        bg=BLUE,
        fg="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(
        pady=(0, 25),
        ipadx=25,
        ipady=8
    )


# =========================
# PIN SYSTEM
# =========================

def create_pin():

    global pin_hash

    pin = pin_entry.get()

    if not pin.isdigit():

        sound_error()

        messagebox.showerror(
            "Invalid PIN",
            "PIN must contain numbers only."
        )

        return

    if len(pin) < 4:

        sound_error()

        messagebox.showerror(
            "Invalid PIN",
            "PIN must contain at least 4 digits."
        )

        return

    pin_hash = hash_pin(
        pin
    )

    save_data()

    sound_success()

    messagebox.showinfo(
        "Success",
        "Your PIN has been created."
    )

    login_window.destroy()

    create_main_window()


def login():

    entered_pin = pin_entry.get()

    if hash_pin(
        entered_pin
    ) == pin_hash:

        sound_success()

        login_window.destroy()

        create_main_window()

    else:

        sound_error()

        messagebox.showerror(
            "Wrong PIN",
            "Incorrect PIN."
        )

        pin_entry.delete(
            0,
            tk.END
        )


def create_login_window():

    global login_window
    global pin_entry

    login_window = tk.Tk()

    login_window.title(
        "Wallet"
    )

    login_window.geometry(
        "430x430"
    )

    login_window.configure(
        bg=BG
    )

    tk.Label(
        login_window,
        text="W",
        font=("Segoe UI", 38, "bold"),
        bg=BLUE,
        fg="white",
        width=2,
        height=1
    ).pack(
        pady=(55, 20)
    )

    tk.Label(
        login_window,
        text="Welcome to Wallet",
        font=("Segoe UI", 22, "bold"),
        bg=BG,
        fg=TEXT
    ).pack()

    if pin_hash is None:

        text = (
            "Create a PIN to protect your wallet"
        )

        button_text = "Create PIN"

        command = create_pin

    else:

        text = (
            "Enter your PIN to continue"
        )

        button_text = "Unlock Wallet"

        command = login

    tk.Label(
        login_window,
        text=text,
        font=("Segoe UI", 11),
        bg=BG,
        fg=MUTED
    ).pack(
        pady=10
    )

    pin_entry = tk.Entry(
        login_window,
        show="●",
        font=("Segoe UI", 18),
        bg=CARD,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        justify="center"
    )

    pin_entry.pack(
        padx=80,
        fill="x",
        ipady=10,
        pady=20
    )

    tk.Button(
        login_window,
        text=button_text,
        command=command,
        bg=BLUE,
        fg="white",
        font=("Segoe UI", 11, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(
        ipadx=30,
        ipady=10
    )

    tk.Label(
        login_window,
        text="🔒 Your PIN is stored as a hash",
        font=("Segoe UI", 9),
        bg=BG,
        fg=MUTED
    ).pack(
        pady=25
    )

    pin_entry.focus()

    login_window.bind(
        "<Return>",
        lambda event: command()
    )

    login_window.mainloop()


# =========================
# START
# =========================

load_data()

create_login_window()








