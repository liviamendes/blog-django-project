from django import template

register = template.Library()


@register.filter(name='number_comments')
def number_comments(num_comment):
    try:
        num_comment = int(num_comment)
        if num_comment == 0:
            return f'No comments'
        elif num_comment == 1:
            return f'{num_comment} comment'
        else:
            return f'{num_comment} comments'
    except:
        return f'{num_comment} comment(s)'
