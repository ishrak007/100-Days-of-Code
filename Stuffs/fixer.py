# Open the output file
with open("requirements.txt", "r") as infile, open("requirements_cleaned.txt", "w") as outfile:
    for line in infile:
        if "@" not in line:  # Exclude lines with @ paths
            outfile.write(line)

