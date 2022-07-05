#####################
# Prompt the user for the options

# sections
numSections = int(input("How many sections would you like for your page:\n"))
sections = ""

sectionArr = []
availableSections = ['1 - hero', '2 - z-pattern', '3 - gallery']
preBuildSections = [
    # hero 
    """     
        <!-- START HERO SECTION -->
        <div class="container container__hero">
        </div>
        <!-- END HERO SECTION -->
    """,
    # z-pattern
    """    
        <!-- START Z-PATTERN SECTION -->
        <div class="container container__z-pattern">
        </div>
        <!-- END Z-PATTERN SECTION -->
    """,
    # gallery
    """
        
        <!-- START GALLERY SECTION -->
        <div class="container container__gallery">
        </div>        
        <!-- END GALLERY SECTION -->
    """,
]


def buildSection(section):
    return preBuildSections[section]    


for n in range(1, numSections + 1):
    section = input('What type should this section be:\n{}\n'.format('\n'.join(availableSections)))
    built = False
    for s in availableSections:
        if (s[0] == section):     
            # call build section function
            sections = sections + "<div class='section section--{}'>{}</div>".format(n, buildSection(int(s[0]) - 1))
            built = True 
    if (built):
        print('section build successfully')
    else: 
        print('There was an error please retry')
        exit()


# each section can be a part, ask what each section should be!
# available section:
# - hero
# - z-pattern
# - tab component
# - gallery
# - slider
# - blank
# - form 
# - pop-up

# ask if you would like nav and footer

# make nav sticky?

# HTML code
html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <title></title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="css/style.css" rel="stylesheet">
    <link href="css/general.css" rel="stylesheet">
  </head>
  <body>
    {} 
  </body>
</html>
""".format(sections)

# CSS general
cssGeneral = """
/*
--- 01 TYPOGRAPHY SYSTEM
Font sizes: 

1 / 1.2 / 1.4 / 1.6 / 1.8 / 2 / 2.4 / 3 / 3.6 / 4.4 / 5.2 / 6.2 / 7.4 / 8.6 / 9.8

- Font weights: 
Default: 400

- Line heights:
Default: 1

--- 02 COLORS 

--- 03 IMAGES

--- 04 ICONS

--- 05 SHADOWS

--- 06 BORDER-RADIUS

--- 07 WHITESPACE

- Spacing system (px)
0.2 / 0.4 / 0.8 / 1.2 / 1.6 / 2.4 / 3.2 / 4.8 / 6.4 / 8 / 9.6 / 12.8
*/

:root {
}

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

html {
  font-size: 62.5%;
  overflow-x: hidden;
}
"""


# Css styles
cssStyles = """

"""



with open('index.html', 'w') as f:
    f.write(html)

with open('style.css', 'w') as f:
    f.write(cssGeneral)

