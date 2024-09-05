def extract_title(line):
    return line.strip()

def extract_section_name(line):
    # Split the line by '{' to separate the section name from the content
    section_part = line.split('{')[0].strip()
    
    section_name = section_part.split()[0].replace('_', ' ')
    
    return section_name

def extract_section_body(section):
    lines = section.strip().split("\n")
    html_output = "<p>"  # Open paragraph once for the section body
    
    for line in lines:
        segments = line.split('[')
        for segment in segments:
            if ']' in segment:
                chord, lyric = segment.split(']', 1)
                chord_html = f'<span class="chord">{chord.strip()}</span>'
                if lyric.strip():
                    html_output += f'<span class="lyric-chord">{chord_html}<span class="lyric">{lyric.strip()}</span></span> '
                else:
                    # If no lyrics, just add the chord without the lyric span
                    html_output += f'{chord_html} '
            else:
                html_output += segment + ' '
        
        html_output += "<br>\n"
    
    html_output += "</p></div>\n" 
    
    return html_output

def parse(file):
    lines = file.strip().split("\n")
    section_storage = {}
    
    # Extract title
    title = extract_title(lines[0])
    html_output = f"<h2>{title}</h2><br>\n"
    
    section_body = ""
    section_name = ""
    
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        
        if '{' in line:
            # Extract and normalize Section Name
            section_name = extract_section_name(line)
            html_output += f"<div class='section'><h3>{section_name}</h3>\n"
        elif '}' in line:
            # Close section and extract its body
            section_html = extract_section_body(section_body)
            html_output += section_html
            # Store the section's HTML for future use using the normalized name
            section_storage[section_name] = section_html
            section_body = ""  # Reset for next section
        elif line.replace('_', ' ') in section_storage:
            # If the normalized section name is found again, reuse the stored HTML
            normalized_name = line.replace('_', ' ')
            html_output += f"<div class='section'><h3>{normalized_name}</h3>\n"
            html_output += section_storage[normalized_name]
        else:
            section_body += line + "\n"  # Collect lines for the section body
    
    return html_output



with open("test.chords", 'r') as file:
    chords_content = file.read()

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
html_output = parse(chords_content)
html_end = """
</body>
</html>
"""
    
with open("test.html", "w") as f:
    f.write(html_header)
    f.write(html_output)
    f.write(html_end)
