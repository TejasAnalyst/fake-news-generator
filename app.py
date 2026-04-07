import streamlit as st
import random
import csv

st.set_page_config(page_title="Fake News Generator", page_icon="📰")

st.title("📰 Fake News Generator")
st.write("Unlimited Fake News Generator 😎🔥")

# ================= CSV LOAD =================
data = []
try:
    with open("fake_news_data.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
except:
    st.warning("⚠ CSV file not found. Using default data.")

# ================= DATA =================
subjects = [
    "Narendra Modi", "Rahul Gandhi", "Devendra Fadnavis", "Eknath Shinde",
    "Donald Trump", "Joe Biden", "Elon Musk", "Bill Gates", "Mark Zuckerberg",
    "Jeff Bezos", "Sundar Pichai", "Satya Nadella",
    "MS Dhoni", "Virat Kohli", "Rohit Sharma", "Hardik Pandya",
    "Cristiano Ronaldo", "Lionel Messi", "Neymar",
    "Jethalal", "Babita", "Daya", "Tappu", "Popatlal",
    "A mysterious hacker", "A billionaire", "A YouTuber", "A gamer",
    "Government", "Scientists", "NASA", "ISRO", "Google", "Meta", "Amazon",
    "A robot", "An AI system", "A monkey", "A lion", "A tiger", "An alien"
]

actions = [
    "launches", "bans", "discovers", "reveals", "hacks", "wins", "eats",
    "orders", "celebrates", "dances with", "sings with", "declares war on",
    "cancels", "investigates", "exposes", "builds", "destroys",
    "creates", "leaks", "announces", "joins", "quits", "attacks",
    "supports", "criticizes", "buys", "sells", "steals", "hides",
    "finds", "tests", "improves", "develops", "copies", "designs"
]

objects = [
    "a secret AI project", "a hidden truth", "a global conspiracy",
    "a new government policy", "an alien spaceship", "a billion-dollar deal",
    "a secret mission", "a new mobile app", "a dangerous experiment",
    "a mysterious island", "a time machine", "a robot army",
    "a fake currency system", "a lost treasure", "a secret code",
    "a powerful weapon", "a futuristic city", "a space station",
    "a virtual world", "a smart device", "a surveillance system"
]

places = [
    "in India", "in USA", "in China", "in Russia", "in Dubai",
    "in Mumbai", "in Pune", "in Delhi", "in Bangalore",
    "on the Moon", "on Mars", "in a secret lab", "inside a jungle",
    "in Antarctica", "under the ocean", "in a hidden bunker",
    "inside a spaceship", "in a parallel universe"
]

times = [
    "today", "yesterday", "last night", "this morning",
    "at midnight", "during a secret meeting", "in 2026",
    "during a live stream", "while sleeping", "during an interview",
    "at a press conference", "on social media"
]

adjectives = [
    "shocking", "unexpected", "mysterious", "controversial",
    "unbelievable", "secret", "dangerous", "funny",
    "weird", "crazy", "viral", "breaking", "exclusive",
    "urgent", "rare", "hidden", "classified"
]

templates = [
    "📰 {adj} NEWS: {sub} {act} {obj} {place} {time}!",
    "🚨 BREAKING: {sub} just {act} {obj} {place} {time}!",
    "🔥 EXCLUSIVE: {sub} secretly {act} {obj} {place}!",
    "😱 ALERT: {obj} {act} by {sub} {place} {time}!",
    "📢 REPORT: {sub} involved in {obj} {place} {time}!"
]

# ================= MODE =================
mode = st.selectbox("Choose Mode", ["Mix", "CSV Only", "Random Only"])

# ================= GENERATE =================
if st.button("Generate News 🔥"):

    if mode == "CSV Only" and data:
        news = random.choice(data)
        headline = f"📰 {news['adjective'].upper()} NEWS: {news['subject']} {news['action']} {news['object']} {news['place']} {news['time']}!"

    elif mode == "Random Only":
        sub = random.choice(subjects)
        act = random.choice(actions)
        obj = random.choice(objects)
        place = random.choice(places)
        time = random.choice(times)
        adj = random.choice(adjectives)
        template = random.choice(templates)

        headline = template.format(
            adj=adj.upper(),
            sub=sub,
            act=act,
            obj=obj,
            place=place,
            time=time
        )

    else:
        if data and random.choice([True, False]):
            news = random.choice(data)
            headline = f"📰 {news['adjective'].upper()} NEWS: {news['subject']} {news['action']} {news['object']} {news['place']} {news['time']}!"
        else:
            sub = random.choice(subjects)
            act = random.choice(actions)
            obj = random.choice(objects)
            place = random.choice(places)
            time = random.choice(times)
            adj = random.choice(adjectives)
            template = random.choice(templates)

            headline = template.format(
                adj=adj.upper(),
                sub=sub,
                act=act,
                obj=obj,
                place=place,
                time=time
            )

    st.success(headline)

    # Save
    with open("generated_news.txt", "a", encoding="utf-8") as f:
        f.write(headline + "\n")
