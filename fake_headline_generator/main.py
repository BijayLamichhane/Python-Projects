import random
from datetime import datetime

subjects = [
    "A Group of Monkeys",
    "The Mayor of Kathmandu",
    "A Secret Society of Cats",
    "Time-Traveling Scientists",
    "An Army of Ducks",
    "The National Potato Association",
    "A Famous TikToker",
    "A Band of Aliens",
    "A Mysterious Old Man",
    "A Kindergarten Teacher",
    "The Local Pizza Delivery Guy",
    "A Robot From the Future"
]

sports = [
    "Cristiano Ronaldo",
    "Lionel Messi",
    "The Nepal Cricket Team",
    "An Angry Referee",
    "The Olympic Committee",
    "A Marathon Runner",
    "A Team of Wrestlers",
    "The National Volleyball Captain"
]

politics = [
    "The Prime Minister",
    "A Group of Senators",
    "An Opposition Leader",
    "The UN Secretary-General",
    "A Corrupt Politician",
    "The President of the USA",
    "A Local Mayor",
    "The Election Commission"
]

actions = [
    "launches",
    "cancels",
    "eats",
    "declares war on",
    "orders",
    "bans",
    "discovers",
    "steals",
    "invents",
    "accidentally sets fire to",
    "transforms into",
    "starts a petition against",
    "gives a speech about"
]

places_or_things = [
    "a plate of samosa",
    "the Moon",
    "all the traffic lights in the city",
    "the internet",
    "a box of chocolates",
    "the national anthem",
    "a giant rubber duck",
    "Nepal’s tallest mountain",
    "the subway system",
    "a random coconut",
    "all online exams",
    "the entire stock market",
    "a bag of chips"
]

# Map categories to actual lists
categories = {
    "subjects": subjects,
    "sports": sports,
    "politics": politics
}

data = []

while True:
    category_choice = input("\nChoose the category (subjects/sports/politics): ").strip().lower()

    if category_choice not in categories:
        print("⚠ Invalid choice! Please pick subjects, sports, or politics.")
        continue

    # Ask user if they want to add something new
    user_choice = input("\nDo you want to add something to this category? (yes/no): ").strip().lower()

    if user_choice == 'yes':
        if category_choice == 'subjects':
            additional_subject = input("\nEnter the subject: ").strip()
            subjects.append(additional_subject)
        elif category_choice == 'sports':
            additional_sports = input("\nEnter the sports: ").strip()
            sports.append(additional_sports)
        elif category_choice == 'politics':
            additional_politics = input("\nEnter the politics: ").strip()
            politics.append(additional_politics)

    # Generate headline
    subject = random.choice(categories[category_choice])
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"Breaking News: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    data.append(headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == 'no':
        break

ask_user = input("\nDo you want to save the headlines (yes/no): ").strip().lower()

if ask_user == 'yes':
    # Generate unique filename using timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"headlines_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        for line in data:
            f.write(line + "\n")

    print(f"\n✅ Headlines saved successfully in '{filename}'")

print("\nThanks for using the Fake News Headline Generator. Have a fun day!")
