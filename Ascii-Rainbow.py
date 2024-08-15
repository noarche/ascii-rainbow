import pyfiglet
from termcolor import colored
import textwrap

def generate_ascii_art(text, font):
    return pyfiglet.figlet_format(text, font=font)

def apply_rainbow_gradient(text, wrap=False):
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
    reset_code = '\033[0m'
    color_index = 0
    colored_text = ""
    
    if wrap:
        text = textwrap.fill(text, width=80)

    for char in text:
        if char.strip():
            colored_text += colors[color_index % len(colors)] + char + reset_code
            color_index += 1
        else:
            colored_text += char
    
    return colored_text

def save_to_file(text, colored_text):
    first_word = text.split()[0]  # Extract the first word from the input text
    filename = f"{first_word}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(colored_text)
    print(f"Text with color codes saved to {filename}")

def save_html_file(text, fonts):
    first_word = text.split()[0]  # Extract the first word from the input text
    html_filename = f"{first_word}_All-ASCII-Fonts.html"
    with open(html_filename, "w", encoding="utf-8") as html_file:
        html_file.write("<html><body>\n")
        for font in fonts:
            ascii_art = generate_ascii_art(text, font)
            html_file.write(f"<pre>{ascii_art}</pre>\n")
            html_file.write(f'<button onclick="copyToClipboard(\'{font}\')">Copy {font}</button>\n')
        html_file.write('''
        <script>
            function copyToClipboard(fontName) {
                const art = document.querySelector(`pre:contains('${fontName}')`).innerText;
                navigator.clipboard.writeText(art);
                alert(`Copied ${fontName} ASCII art!`);
            }
        </script>\n''')
        html_file.write("</body></html>")
    print(f"HTML file saved to {html_filename}")

def main():
    try:
        while True:
            text = input("Enter the text: ")

            # Display all ASCII art styles and generate HTML
            fonts = pyfiglet.FigletFont.getFonts()
            save_html_file(text, fonts)

            print("\nAll ASCII fonts have been saved to an HTML file. Choose an option:")
            print("1. Convert to ASCII art")
            print("2. Colorize plain text")
            choice = int(input("\nEnter the number of the option you want: "))

            if choice == 1:
                # Display font style options
                print("\nChoose an ASCII art style:")
                for i, font in enumerate(fonts, start=1):
                    print(f"{i}. {font}")
                
                # Get user choice
                style_choice = int(input("\nEnter the number of the style you want: "))
                if 1 <= style_choice <= len(fonts):
                    selected_font = fonts[style_choice - 1]
                else:
                    print("Invalid choice. Defaulting to 'slant'.")
                    selected_font = "slant"

                # Generate ASCII art with selected style
                ascii_art = generate_ascii_art(text, selected_font)
                colored_art = apply_rainbow_gradient(ascii_art)

                # Display and save
                print("\nRainbow ASCII Art with Color Codes:\n")
                print(colored_art)
                
                save_to_file(text, colored_art)

            elif choice == 2:
                # Colorize plain text
                colored_text = apply_rainbow_gradient(text, wrap=True)

                # Display and save
                print("\nRainbow Colored Text with Color Codes:\n")
                print(colored_text)
                
                save_to_file(text, colored_text)
            else:
                print("Invalid choice. Please select 1 or 2.")
            
            print("\n--- Operation completed successfully ---\n")
    
    except KeyboardInterrupt:
        print("\n\nThank you for using the text colorizer! Goodbye.")

if __name__ == "__main__":
    main()
