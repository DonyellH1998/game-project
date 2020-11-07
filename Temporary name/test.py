import sys
import time
import textwrap

def slowprint(s):
    #Used to print text slowly
    for c in s + '\n': 
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./35)

def wrap(p):
    #Uses textwrap module to keep sentences printed out to a max of 95
    wrapper = textwrap.TextWrapper(width=95, break_long_words=False, replace_whitespace=False)
    #dedented_text = textwrap.dedent(text=p).strip()
    wrap_list = wrapper.wrap(p)

    for line in wrap_list:
        slowprint(line)

wrap('\nAs you look more closely to the ovals, you realize that they’re some kind of portal. ')
wrap('These portals are making a weird ominous sound, but at the same time, it looks like that’s your only option to get out of wherever you currently are.')