def extract_title(line):
    return line.strip()

def extract_section_name(line):
    # Split the line by '{' to separate the section name from the content
    section_part = line.split('{')[0].strip()
    
    # Only keep the first part before any space and replace underscores with spaces
    section_name = section_part.split()[0].replace('_', ' ')
    
    return section_name

def extract_section_body(section):
    lines = section.strip().split("\n")
    html_output = "<p>"
    
    for line in lines:
        segments = line.split('[')
        for segment in segments:
            if ']' in segment:
                chord, lyric = segment.split(']', 1)
                html_output += f'<span class="lyric-chord"><span class="chord">{chord.strip()}</span><span class="lyric">{lyric.strip()}</span></span> '
            else:
                html_output += segment + ' '  # Add any part without chords
        
        html_output += "<br>\n" 
    
    html_output += "</p>\n"
    
    return html_output

def parse(file):
    lines = file.strip().split("\n")
    
    # Extract title
    title = extract_title(lines[0])
    html_output = f"<h2>{title}</h2>\n"
    
    section_body = ""
    
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        
        if '{' in line:
            # Extract Section Name
            section_name = extract_section_name(line)
            html_output += f"<h3>{section_name}</h3>\n"
        elif '}' in line:
            # Close section and extract its body
            html_output += extract_section_body(section_body)
            section_body = ""  # Reset for next section
        else:
            section_body += line + "\n"  # Collect lines for the section body
    
    return html_output

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

html_header = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Chords</title>
</head>
<body>
"""
html_output = parse(input_file)
html_end = """
</body>
</html>
"""
    
with open("test.html", "w") as f:
    f.write(html_header)
    f.write(html_output)
    f.write(html_end)
