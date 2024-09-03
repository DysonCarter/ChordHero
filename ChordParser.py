def extract_title(input_file):
    # Split the input by lines and return the first line as the title
    lines = input_file.strip().splitlines()
    title = lines[0].strip()
    return title

# Example usage
input_file = """
Build My Life

Intro {
    [1, 4/1, 1/3, 4/1]
}

Verse_1 {
    [1]Worthy of every [4/1]song we could ever sing
}

Chorus {
    [4 maj9]Holy, there is none one [2 7]like you,
    there is none be[1]side you. Open up my [6]eyes in wonder
}

Verse_1

Chorus

Bridge {
    [4 maj9]I will build my [5 sus]life upon your
    [6]love it is a [1/3]firm foundation.
}

Chorus
"""

title = extract_title(input_file)
print("Title:", title)
