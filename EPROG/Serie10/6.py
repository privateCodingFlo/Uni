from random import choice
import textwrap


# Class for generating text based on a Markov chain - Adapted to Characters for Task 6
class TextGenerator:
    def __init__(self, filename):
        self.possible_chars = dict()

        # Build the dictionary of possible character transitions from the text file
        # (c1, c2) -> [list of possible next characters]
        c1 = ""
        c2 = ""

        try:
            with open(filename, "r", encoding="utf-8") as f:
                # Read the entire text at once
                content = f.read()

                # Iterate through pairs of characters
                # We need c1, c2 initialized.
                # Strategy: Take the first two chars from content to start,
                # then iterate from the 3rd char onwards.
                if len(content) >= 2:
                    c1 = content[0]
                    c2 = content[1]

                    for i in range(2, len(content)):
                        char = content[i]
                        key = (c1, c2)

                        if key not in self.possible_chars:
                            self.possible_chars[key] = [char]
                        else:
                            self.possible_chars[key].append(char)

                        c1, c2 = c2, char
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

    # Generate text of a given character count
    def generate_text(self, char_count=300):
        if not self.possible_chars:
            return "No model trained."

        # Start with a random char pair where the first char is uppercase (to simulate sentence start)
        # or just any pair if none found.
        start_candidates = [k for k in self.possible_chars if k[0].isupper()]
        if not start_candidates:
            start_candidates = list(self.possible_chars.keys())

        c1, c2 = choice(start_candidates)
        text = c1 + c2

        for _ in range(char_count):
            key = (c1, c2)
            if key in self.possible_chars:
                next_char = choice(
                    self.possible_chars[key]
                )  # Randomly choose the next char
                text += next_char
                c1, c2 = c2, next_char
            else:
                break  # Dead end

        return textwrap.fill(text)  # Format the text


if __name__ == "__main__":
    # Using 'data.txt' from the current task
    # Adjust path if necessary, assuming script runs from 'Uni' or 'Serie10' context
    import os

    target_file = "EPROG/Serie10/data.txt"
    if not os.path.exists(target_file):
        target_file = "data.txt"  # Fallback for local run

    print(f"Trainiere Model mit {target_file}...")
    my_generator = TextGenerator(target_file)

    print("\n--- Generierter Text ---")
    print(my_generator.generate_text(500))
