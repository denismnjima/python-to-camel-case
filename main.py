import re
def to_camel_case(text):
    def letter_to_upper(match):
        print(match)
        return match.group(0).upper()
    
    cased = re.sub(r'(?<=[-_])\w', letter_to_upper, text)
    result = cased.replace('-','').replace('_','')
    
    print(result)

to_camel_case("the_stealth_warrior")
