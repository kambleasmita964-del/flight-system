import tkinter as tk
from tkinter import ttk, messagebox
import random

# ---------------- FLIGHT DATA ----------------

flights = [
    {
        "flight_no": "AI101",
        "airline": "Air India",
        "from": "Pune",
        "to": "Delhi",
        "departure": "08:00 AM",
        "arrival": "10:15 AM",
        "price": 5500,
        "seats": 45
    },
    {
        "flight_no": "6E202",
        "airline": "IndiGo",
        "from": "Mumbai",
        "to": "Bangalore",
        "departure": "11:30 AM",
        "arrival": "01:15 PM",
        "price": 4200,
        "seats": 38
    },
    {
        "flight_no": "UK303",
        "airline": "Vistara",
        "from": "Delhi",
        "to": "Mumbai",
        "departure": "02:00 PM",
        "arrival": "04:10 PM",
        "price": 6100,
        "seats": 30
    },
    {
        "flight_no": "AI404",
        "airline": "Air India",
        "from": "Pune",
        "to": "Mumbai",
        "departure": "05:30 PM",
        "arrival": "06:40 PM",
        "price": 2800,
        "seats": 25
    },
    {
        "flight_no": "6E505",
        "airline": "IndiGo",
        "from": "Bangalore",
        "to": "Delhi",
        "departure": "07:00 PM",
        "arrival": "09:40 PM",
        "price": 5800,
        "seats": 42
    }
]

passengers = []
bookings = []


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("Flight Reservation System")
root.geometry("1000x650")
root.configure(bg="#eef3f8")


# ---------------- FUNCTIONS ----------------

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def home_page():
    clear_screen()

    title = tk.Label(
        root,
        text="✈ FLIGHT RESERVATION SYSTEM",
        font=("Arial", 26, "bold"),
        bg="#17365D",
        fg="white",
        pady=20
    )
    title.pack(fill="x")

    tk.Label(
        root,
        text="Welcome to Online Flight Reservation System",
        font=("Arial", 18, "bold"),
        bg="#eef3f8",
        fg="#17365D"
    ).pack(pady=35)

    tk.Label(
        root,
        text="Book your flight easily, quickly and securely.",
        font=("Arial", 13),
        bg="#eef3f8"
    ).pack(pady=5)

    button_frame = tk.Frame(root, bg="#eef3f8")
    button_frame.pack(pady=40)

    buttons = [
        ("👤 Passenger Registration", passenger_registration),
        ("✈ Flight Details", flight_details),
        ("🔎 Search Flights", search_flights),
        ("🎫 Book Flight", book_flight),
        ("📋 Booking Details", booking_details),
        ("❌ Cancel Booking", cancel_booking),
        ("ℹ About System", about_system)
    ]

    for text, command in buttons:
        tk.Button(
            button_frame,
            text=text,
            command=command,
            width=25,
            height=2,
            font=("Arial", 11, "bold"),
            bg="#1F4E78",
            fg="white",
            activebackground="#5B9BD5"
        ).pack(pady=6)

    tk.Label(
        root,
        text="© 2026 Flight Reservation System",
        font=("Arial", 10),
        bg="#eef3f8",
        fg="gray"
    ).pack(side="bottom", pady=15)


# ---------------- PASSENGER REGISTRATION ----------------

def passenger_registration():
    clear_screen()

    header("Passenger Registration")

    frame = tk.Frame(root, bg="#eef3f8")
    frame.pack(pady=30)

    labels = [
        "Full Name",
        "Age",
        "Gender",
        "Phone Number",
        "Email",
        "Address"
    ]

    entries = {}

    for i, label in enumerate(labels):
        tk.Label(
            frame,
            text=label + ":",
            font=("Arial", 12, "bold"),
            bg="#eef3f8"
        ).grid(row=i, column=0, padx=15, pady=10, sticky="w")

        if label == "Gender":
            entry = ttk.Combobox(
                frame,
                values=["Male", "Female", "Other"],
                width=27,
                state="readonly"
            )
        else:
            entry = tk.Entry(frame, width=30, font=("Arial", 11))

        entry.grid(row=i, column=1, padx=15, pady=10)
        entries[label] = entry

    def register():
        name = entries["Full Name"].get()
        age = entries["Age"].get()
        gender = entries["Gender"].get()
        phone = entries["Phone Number"].get()
        email = entries["Email"].get()
        address = entries["Address"].get()

        if not name or not age or not gender or not phone or not email:
            messagebox.showwarning(
                "Missing Information",
                "Please fill all required fields."
            )
            return

        passenger_id = "P" + str(random.randint(1000, 9999))

        passengers.append({
            "id": passenger_id,
            "name": name,
            "age": age,
            "gender": gender,
            "phone": phone,
            "email": email,
            "address": address
        })

        messagebox.showinfo(
            "Registration Successful",
            f"Passenger registered successfully!\n\nPassenger ID: {passenger_id}"
        )

        home_page()

    tk.Button(
        root,
        text="Register Passenger",
        command=register,
        width=22,
        height=2,
        bg="#1F4E78",
        fg="white",
        font=("Arial", 11, "bold")
    ).pack(pady=10)

    back_button()


# ---------------- FLIGHT DETAILS ----------------

def flight_details():
    clear_screen()

    header("Available Flight Details")

    columns = (
        "Flight No",
        "Airline",
        "From",
        "To",
        "Departure",
        "Arrival",
        "Price",
        "Seats"
    )

    tree = ttk.Treeview(
        root,
        columns=columns,
        show="headings",
        height=12
    )

    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, width=110)

    for flight in flights:
        tree.insert(
            "",
            "end",
            values=(
                flight["flight_no"],
                flight["airline"],
                flight["from"],
                flight["to"],
                flight["departure"],
                flight["arrival"],
                "₹" + str(flight["price"]),
                flight["seats"]
            )
        )

    tree.pack(pady=25)

    back_button()


# ---------------- SEARCH FLIGHTS ----------------

def search_flights():
    clear_screen()

    header("Search Flights")

    frame = tk.Frame(root, bg="#eef3f8")
    frame.pack(pady=25)

    tk.Label(
        frame,
        text="From:",
        font=("Arial", 12, "bold"),
        bg="#eef3f8"
    ).grid(row=0, column=0, padx=10)

    from_entry = ttk.Combobox(
        frame,
        values=["Pune", "Mumbai", "Delhi", "Bangalore"],
        width=20
    )
    from_entry.grid(row=0, column=1, padx=10)

    tk.Label(
        frame,
        text="To:",
        font=("Arial", 12, "bold"),
        bg="#eef3f8"
    ).grid(row=0, column=2, padx=10)

    to_entry = ttk.Combobox(
        frame,
        values=["Pune", "Mumbai", "Delhi", "Bangalore"],
        width=20
    )
    to_entry.grid(row=0, column=3, padx=10)

    result = tk.Text(
        root,
        width=100,
        height=15,
        font=("Courier New", 11)
    )
    result.pack(pady=20)

    def search():
        source = from_entry.get()
        destination = to_entry.get()

        result.delete("1.0", tk.END)

        found = False

        for flight in flights:
            if flight["from"] == source and flight["to"] == destination:
                found = True

                result.insert(
                    tk.END,
                    f"Flight No : {flight['flight_no']}\n"
                    f"Airline   : {flight['airline']}\n"
                    f"Departure : {flight['departure']}\n"
                    f"Arrival   : {flight['arrival']}\n"
                    f"Price     : ₹{flight['price']}\n"
                    f"Seats     : {flight['seats']}\n"
                    f"{'-'*70}\n"
                )

        if not found:
            result.insert(
                tk.END,
                "No flights found for the selected route."
            )

    tk.Button(
        root,
        text="Search",
        command=search,
        width=18,
        height=2,
        bg="#1F4E78",
        fg="white",
        font=("Arial", 11, "bold")
    ).pack()

    back_button()


# ---------------- BOOK FLIGHT ----------------

def book_flight():
    clear_screen()

    header("Book a Flight")

    frame = tk.Frame(root, bg="#eef3f8")
    frame.pack(pady=25)

    tk.Label(
        frame,
        text="Passenger ID:",
        font=("Arial", 12, "bold"),
        bg="#eef3f8"
    ).grid(row=0, column=0, padx=10, pady=10)

    passenger_entry = tk.Entry(frame, width=25)
    passenger_entry.grid(row=0, column=1)

    tk.Label(
        frame,
        text="Flight Number:",
        font=("Arial", 12, "bold"),
        bg="#eef3f8"
    ).grid(row=1, column=0, padx=10, pady=10)

    flight_entry = tk.Entry(frame, width=25)
    flight_entry.grid(row=1, column=1)

    tk.Label(
        frame,
        text="Travel Date:",
        font=("Arial", 12, "bold"),
        bg="#eef3f8"
    ).grid(row=2, column=0, padx=10, pady=10)

    date_entry = tk.Entry(frame, width=25)
    date_entry.grid(row=2, column=1)

    tk.Label(
        frame,
        text="Number of Seats:",
        font=("Arial", 12, "bold"),
        bg="#eef3f8"
    ).grid(row=3, column=0, padx=10, pady=10)

    seats_entry = tk.Entry(frame, width=25)
    seats_entry.grid(row=3, column=1)

    def book():

        passenger_id = passenger_entry.get()
        flight_no = flight_entry.get()
        travel_date = date_entry.get()
        seats = seats_entry.get()

        if not passenger_id or not flight_no or not travel_date or not seats:
            messagebox.showwarning(
                "Missing Information",
                "Please fill all fields."
            )
            return

        passenger = None
        flight = None

        for p in passengers:
            if p["id"] == passenger_id:
                passenger = p

        for f in flights:
            if f["flight_no"] == flight_no:
                flight = f

        if passenger is None:
            messagebox.showerror(
                "Error",
                "Passenger ID not found. Please register first."
            )
            return

        if flight is None:
            messagebox.showerror(
                "Error",
                "Flight number not found."
            )
            return

        try:
            number_of_seats = int(seats)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Number of seats must be a number."
            )
            return

        if number_of_seats <= 0:
            messagebox.showerror(
                "Error",
                "Enter a valid number of seats."
            )
            return

        if number_of_seats > flight["seats"]:
            messagebox.showerror(
                "Error",
                "Not enough seats available."
            )
            return

        flight["seats"] -= number_of_seats

        booking_id = "BK" + str(random.randint(10000, 99999))

        total_price = flight["price"] * number_of_seats

        bookings.append({
            "booking_id": booking_id,
            "passenger_id": passenger_id,
            "passenger_name": passenger["name"],
            "flight_no": flight_no,
            "airline": flight["airline"],
            "from": flight["from"],
            "to": flight["to"],
            "date": travel_date,
            "seats": number_of_seats,
            "total_price": total_price
        })

        messagebox.showinfo(
            "Booking Successful",
            f"Flight booked successfully!\n\n"
            f"Booking ID: {booking_id}\n"
            f"Passenger: {passenger['name']}\n"
            f"Flight: {flight_no}\n"
            f"Total Amount: ₹{total_price}"
        )

        home_page()

    tk.Button(
        root,
        text="Confirm Booking",
        command=book,
        width=22,
        height=2,
        bg="#1F4E78",
        fg="white",
        font=("Arial", 11, "bold")
    ).pack(pady=10)

    back_button()


# ---------------- BOOKING DETAILS ----------------

def booking_details():
    clear_screen()

    header("Booking Details")

    result = tk.Text(
        root,
        width=100,
        height=20,
        font=("Courier New", 11)
    )
    result.pack(pady=20)

    if not bookings:
        result.insert(
            tk.END,
            "No bookings available."
        )
    else:
        for booking in bookings:
            result.insert(
                tk.END,
                f"Booking ID   : {booking['booking_id']}\n"
                f"Passenger    : {booking['passenger_name']}\n"
                f"Flight       : {booking['flight_no']}\n"
                f"Airline      : {booking['airline']}\n"
                f"Route        : {booking['from']} → {booking['to']}\n"
                f"Travel Date  : {booking['date']}\n"
                f"Seats        : {booking['seats']}\n"
                f"Total Amount : ₹{booking['total_price']}\n"
                f"{'='*75}\n"
            )

    back_button()


# ---------------- CANCEL BOOKING ----------------

def cancel_booking():
    clear_screen()

    header("Cancel Booking")

    frame = tk.Frame(root, bg="#eef3f8")
    frame.pack(pady=40)

    tk.Label(
        frame,
        text="Enter Booking ID:",
        font=("Arial", 12, "bold"),
        bg="#eef3f8"
    ).grid(row=0, column=0, padx=10)

    booking_entry = tk.Entry(frame, width=25)
    booking_entry.grid(row=0, column=1, padx=10)

    def cancel():

        booking_id = booking_entry.get()

        for booking in bookings:

            if booking["booking_id"] == booking_id:

                for flight in flights:
                    if flight["flight_no"] == booking["flight_no"]:
                        flight["seats"] += booking["seats"]

                bookings.remove(booking)

                messagebox.showinfo(
                    "Cancelled",
                    "Booking cancelled successfully."
                )

                home_page()
                return

        messagebox.showerror(
            "Error",
            "Booking ID not found."
        )

    tk.Button(
        root,
        text="Cancel Booking",
        command=cancel,
        width=20,
        height=2,
        bg="#C00000",
        fg="white",
        font=("Arial", 11, "bold")
    ).pack(pady=20)

    back_button()


# ---------------- ABOUT SYSTEM ----------------

def about_system():
    clear_screen()

    header("About Flight Reservation System")

    text = """
FLIGHT RESERVATION SYSTEM

This project is a simple computerized flight
reservation system developed using Python and Tkinter.

Main Features:

• Passenger Registration
• Flight Information
• Search Flights
• Flight Booking
• Booking Details
• Booking Cancellation
• Seat Availability
• Automatic Booking ID
• Automatic Total Fare Calculation

Technologies Used:

• Python
• Tkinter GUI
• Basic Data Structures
• Functions
• Lists and Dictionaries

Purpose:

The system helps passengers search flights,
register their information, make reservations,
view booking information and cancel bookings easily.
"""

    tk.Label(
        root,
        text=text,
        font=("Arial", 12),
        bg="#eef3f8",
        justify="left",
        anchor="w"
    ).pack(pady=30)

    back_button()


# ---------------- HEADER ----------------

def header(title):

    tk.Label(
        root,
        text=title,
        font=("Arial", 22, "bold"),
        bg="#17365D",
        fg="white",
        pady=15
    ).pack(fill="x")


def back_button():

    tk.Button(
        root,
        text="← Back to Home",
        command=home_page,
        width=18,
        height=2,
        bg="#666666",
        fg="white",
        font=("Arial", 10, "bold")
    ).pack(pady=10)


# ---------------- START PROGRAM ----------------

home_page()

root.mainloop()