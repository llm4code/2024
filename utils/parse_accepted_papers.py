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
# If its a positional paper (indicated by column "paper_type"), add a label "[Position Paper]" to the title
df["title"] = df.apply(
    lambda row: (
        f"{row['title']} 💡"
        if "position" in row["paper_type"].lower()
        else row["title"]
    ),
    axis=1,
)
df["authors"] = df["authors"].apply(
    lambda x:  ", ".join([f"<span style=\"white-space: nowrap;\">{a['first']}&nbsp;{a['last']}</span>" for a in x]) 
)

# print(df[['title', 'authors']].head())
# Add a column for position papers
# df['position_paper'] = df['title'].apply(lambda x: 'Yes' if 'Position' in x else 'No')

# Print the DataFrame as a Markdown table
print(df[["title", "authors"]].to_markdown(index=False))
