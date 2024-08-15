def fancy_bold(text):
    bold_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                 '𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙'
                                 '𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳')
    return text.translate(bold_mapping)

def small_caps(text):
    small_caps_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                       'ᴬᴮᴮᴭᴮᴮᴮᴯᴰᴱᴳᴴᴵᴲᴳᴻᴼᴾᴿˢᵀᵁᵥᵂʏᵏ'
                                       'ᵃᵇᶜᵈᵉᶠᵍʜᶦʲᵏʟᵐⁿᵒᵖᵟʳˢᵗᵘᵛʷˣʸᶻ')
    return text.translate(small_caps_mapping)

def glitchy_fancy(text):
    glitchy_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                    '𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅'
                                    '𝖺𝖻𝖼𝖽𝖾𝖿𝖺𝖻𝖻𝖿𝖺𝖻𝖿𝖺𝖼𝖿𝖿')
    return text.translate(glitchy_mapping)

def italic_font(text):
    italic_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                   '𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁'
                                   '𝒶𝒷𝒸𝒹𝒺𝒻𝒼𝒽𝒾𝒿𝒦𝒻𝒽𝒾𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏')
    return text.translate(italic_mapping)

def underline_font(text):
    underline_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                      '𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭'
                                      '𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭')
    return text.translate(underline_mapping)

def script_font(text):
    script_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                   '𝒜𝒵𝒞𝒟𝒯𝒥𝒦𝒩𝒪𝒫𝒬𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵'
                                   '𝒶𝒷𝒸𝒹𝒺𝒻𝒼𝒽𝒾𝒿𝒦𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏')
    return text.translate(script_mapping)

def sans_serif_bold(text):
    sans_bold_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                       '𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭'
                                       '𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝗌𝗍𝗎𝓋𝗂𝗌𝓍𝓎𝓏')
    return text.translate(sans_bold_mapping)

def sans_serif_italic(text):
    sans_italic_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                        '𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘇'
                                        '𝒶𝒷𝒸𝒹𝒺𝒻𝒼𝒽𝒾𝒿𝒦𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏')
    return text.translate(sans_italic_mapping)

def double_struck(text):
    double_struck_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                          '𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℎ𝕀𝕁𝕂𝕃𝕄𝕹𝕺𝕻𝕼ℝ𝕾𝕿𝕌𝕍𝕎𝕏𝕐ℤ'
                                          '𝒶𝒷𝒸𝒹𝒺𝒻𝒼𝒽𝒾𝒿𝒦𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏')
    return text.translate(double_struck_mapping)

def fraktur_font(text):
    fraktur_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                     '𝔄𝔅𝔇𝔈𝔉𝔊𝔋𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔𝔕𝔖𝔗𝔘𝔙𝔚𝔛𝔜𝔞𝔟𝔠𝔻𝔼𝔽𝔾𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔷')
    return text.translate(fraktur_mapping)

def monospace_font(text):
    monospace_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                      '𝚨𝚩𝚪𝚫𝚬𝚭𝚮𝚯𝚰𝚱𝚲𝚳𝚴𝚵𝚶𝚷𝚸𝚹𝚺𝚻𝚼𝚽𝚾𝚿𝟀𝟁𝟂𝟃𝟄𝟅𝟆𝟇𝟈𝟉𝟊𝟋𝟎𝟏𝟐𝟑𝟒𝟓𝟎𝟑𝟜𝟝𝟞𝟟𝟠𝟹𝟺𝟻𝟼𝟽𝟾𝟿')
    return text.translate(monospace_mapping)

def wide_font(text):
    wide_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                 'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'
                                 'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ')
    return text.translate(wide_mapping)

def superscript_font(text):
    superscript_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                        'ᴬᴮᴯᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴻᴼᴽᴾᴿˢᵀᵁⱽᵂʸᵏ'
                                        'ᵃᵇᶜᵈᵉᶠᵍʜᶦʲᵏʟᵐⁿᵒᵖᵟʳˢᵗᵘᵛʷˣʸᶻ')
    return text.translate(superscript_mapping)

def subscript_font(text):
    subscript_mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                      'ₐₑₒₓₐₑₒₓₐₑₒₓₐₑₒₓₐₑₒₓₐₑₒₓₐₑₒₓₐₑₒₓ'
                                      'ₐₑₒₓₐₑₒₓₐₑₒₓₐₑₒₓₐₑₒₓₐₑₒₓₐₑₒₓₐₑₒₓ')
    return text.translate(subscript_mapping)

def main():
    print("Choose a font style:")
    print("1. Fancy Bold")
    print("2. Small Caps")
    print("3. Glitchy Fancy")
    print("4. Italic")
    print("5. Underline")
    print("6. Script")
    print("7. Sans-serif Bold")
    print("8. Sans-serif Italic")
    print("9. Double Struck")
    print("10. Fraktur")
    print("11. Monospace")
    print("12. Wide")
    print("13. Superscript")
    print("14. Subscript")

    choice = input("Enter the number of your choice: ")

    if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']:
        print("Invalid choice. Exiting.")
        return

    text = input("Enter the text to convert: ")

    if choice == '1':
        result = fancy_bold(text)
    elif choice == '2':
        result = small_caps(text)
    elif choice == '3':
        result = glitchy_fancy(text)
    elif choice == '4':
        result = italic_font(text)
    elif choice == '5':
        result = underline_font(text)
    elif choice == '6':
        result = script_font(text)
    elif choice == '7':
        result = sans_serif_bold(text)
    elif choice == '8':
        result = sans_serif_italic(text)
    elif choice == '9':
        result = double_struck(text)
    elif choice == '10':
        result = fraktur_font(text)
    elif choice == '11':
        result = monospace_font(text)
    elif choice == '12':
        result = wide_font(text)
    elif choice == '13':
        result = superscript_font(text)
    elif choice == '14':
        result = subscript_font(text)

    print(f"Converted text: {result}")

if __name__ == "__main__":
    main()
