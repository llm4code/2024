import json
import pandas as pd

# Load the JSON data
with open("llm4code2024-all-accepted-papers.json", "r") as f:
    data = json.load(f)

# Convert the data to a pandas DataFrame
print("Normalizing the data...")
df = pd.json_normalize(data)

print("Number of papers:", len(df))
# Extract the title and author names
# If it's a positional paper (indicated by column "paper_type"), add a label "[Position Paper]" to the title
df["title"] = df.apply(
    lambda row: (
        f"{row['title']} 💡"
        if "position" in row["paper_type"].lower()
        else row["title"]
    ),
    axis=1,
)
df["authors"] = df["authors"].apply(
    lambda x: ", ".join([f"<span style=\"white-space: nowrap;\">{a['first']}&nbsp;{a['last']}</span>" for a in x]) 
)

# Determine if it's a position paper
df["is_position_paper"] = df["paper_type"].apply(lambda x: "position" in x.lower())

# Sort the DataFrame: first by 'is_position_paper' to push position papers to the bottom, then alphabetically by 'title'
df = df.sort_values(by=["is_position_paper", "title"], ascending=[True, True])

# Print the DataFrame as a Markdown table
print(df[["title", "authors"]].to_markdown(index=False))
