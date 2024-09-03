def extract_title(line):
    return line.strip()

def extract_section_name(line):
    # Split the line by '{' to separate the section name from the content
    section_part = line.split('{')[0].strip()
    
    # Only keep the first part before any space and replace underscores with spaces
    section_name = section_part.split()[0].replace('_', ' ')
    
    return section_name

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
