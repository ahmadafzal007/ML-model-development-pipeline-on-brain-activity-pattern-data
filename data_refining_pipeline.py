input_file = "brain_activity.sql"
output_file = "Updated_brain_activity.sql"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        updated_line = line.replace("`", '"')  # Replace backticks with double quotes
        outfile.write(updated_line)

print("Backticks replaced successfully in the large file.")
