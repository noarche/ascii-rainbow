import pyperclip

def fancy_bold(text):
    bold_mapping = str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        '𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙'
        '𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳'
    )
    return text.translate(bold_mapping)

def small_caps(text):
    small_caps_mapping = str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᵠᴿˢᵀᵁᵛᵂˣʸᶻ'
        'ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ'
    )
    return text.translate(small_caps_mapping) 
















def wide_font(text):
    wide_mapping = str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'
        'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ'
    )
    return text.translate(wide_mapping)

def main():
    while True:
        user_input = input("Enter text (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        print("Choose a font style:")
        print("1. Fancy Bold")
        print("2. Small Caps")
        print("3. Wide")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            result = fancy_bold(user_input)
        elif choice == '2':
            result = small_caps(user_input)
        elif choice == '3':
            result = wide_font(user_input)
        else:
            print("Invalid choice. Please try again.")
            continue

        pyperclip.copy(result)
        print(f"Copied to the clipboard: {result}")
        print("Input something else to convert... ")

if __name__ == "__main__":
    main()
