def main():
    ingredients = []
    steps = []
    print("Welcome to my Cooking Recipie Website Generator!")
    print("What is the name of your recipie?")
    recipie_name = input()
    print("Enter a brief description of your recipie")
    recipie_desc = input()
    answer = "y"
    while answer == "y":
        print("enter an ingredient required for the recipie.")
        ingredient = input()
        ingredients.append(ingredient)
        print("another ingredient? (y/n)")
        answer = input()
    answer = "y"
    while answer == "y":
        print("enter a step required for the recipie.")
        step = input()
        steps.append(step)
        print("another step? (y/n)")
        answer = input()
    html(recipie_name, recipie_desc, ingredients, steps)
    css()


def html(recipie_name, recipie_desc, ingredients, steps):
    f = open("index.html", "w")
    f.write("""
     <!DOCTYPE html>
     <html lang="en">
     <head>
     <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>cooking website generator</title>
    <link rel="stylesheet" href="index.css">
    </head>
    <body>
     <h1>generated Recipie by python script</h1>
     <h2>%s</h2>
     <h3>%s.</h3>
    <p>Ingredients</p>
     <ul>
        """ % (recipie_name, recipie_desc))
    for i in range(len(ingredients)):
        f.write("<li>%s</li>"%(ingredients[i]))
    f.write("""
       </ul>
       <p>Directions</p>
       <ol>
       """)
    for i in range(len(steps)):
        f.write("<li>%s</li>"%(steps[i]))  
    f.write("""
       </ol>
      <button onclick="window.print()">print recipie</button>
 </body>

 </html>
     """)
    f.close()
    
def css():
    f = open("index.css", "w")
    f.write("""
html {
  height: 100%;
}
body {
    padding: 25px;
    font-size: 25px;
    text-align: center;
    align-items: center;
   
  }
  
  @media (prefers-color-scheme: dark) {
    body {
      background-color: black;
      color: white;
      background-image: linear-gradient(to bottom, #000000,#212121);
      background-attachment: fixed;
      
    }
  }
  @media (prefers-color-scheme: light) {
    body {
      background-color: white;
      color: black;
      background-image: linear-gradient(to top, #e6e9f0 , #eef1f5 );
      background-attachment: fixed;

    }
  }
ul{
    
    display: inline-block;
    text-align:left;


}
ol{
    
    display: inline-block;
    text-align:left;


}
    
    
    """)
    f.close()

if __name__ == "__main__":
    main()
