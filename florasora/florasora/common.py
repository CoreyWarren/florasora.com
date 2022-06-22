from django import template

register = template.Library()

# "What is this file?"
# common template tags to be used across various apps in this django project
# Made to reduce need to copy/paste everything.



# https://stackoverflow.com/questions/40686201/django-1-10-1-my-templatetag-is-not-a-registered-tag-library-must-be-one-of
# https://stackoverflow.com/questions/28872390/django-how-to-access-array-index-in-template-using-variable


@register.filter(name='get_by_index')
def page_types_links(l, i):
    try:
        result = l[i]
    except:
        return None
    
    return result



