#Name=Kamaljeet Singh
#UID=22BCS10201
#Code of making Happiness tracker using python.
import datetime

# Initialize an empty list to store daily happiness scores
happiness_log = []

# Function to add a happiness score for the day
def log_happiness(score):
    if 1 <= score <= 10:
        entry = {
            "date": datetime.date.today().isoformat(),
            "score": score
        }
        happiness_log.append(entry)
        print(f"Happiness score of {score} logged for {entry['date']}.")
    else:
        print("Please enter a score between 1 and 10.")

# Function to view happiness logs
def view_logs():
    if happiness_log:
        print("\nHappiness Tracker Logs:")
        for entry in happiness_log:
            print(f"Date: {entry['date']}, Score: {entry['score']}")
    else:
        print("No happiness scores logged yet.")

# Function to calculate the average happiness score
def calculate_average():
    if happiness_log:
        average = sum(entry['score'] for entry in happiness_log) / len(happiness_log)
        print(f"\nAverage Happiness Score: {average:.2f}")
    else:
        print("No happiness scores available to calculate an average.")

# Menu to interact with the happiness tracker
def menu():
    while True:
        print("\nHappiness Tracker Menu:")
        print("1. Log today's happiness score")
        print("2. View happiness logs")
        print("3. Calculate average happiness score")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            try:
                score = int(input("Enter your happiness score (1-10): "))
                log_happiness(score)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '2':
            view_logs()
        elif choice == '3':
            calculate_average()
        elif choice == '4':
            print("Exiting Happiness Tracker. Have a great day!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")

# Run the menu
if __name__ == "__main__":
    menu()
