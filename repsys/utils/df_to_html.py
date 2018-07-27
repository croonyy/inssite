# encoding:utf-8
def df_to_html(df, style=None, random_id=None):
    # from IPython.display import HTML
    # import numpy as np
    import re

    df_html = df.to_html()

    # if random_id is None:
    #     random_id = 'id%d' % np.random.choice(np.arange(1000000))
    #
    # if style is None:
    #     style = """
    #     <style type="text/css">
    #     table#{random_id} {{
    #         font-family: verdana,arial,sans-serif;
    #         font-size:11px;
    #         color:#333333;
    #         border-width: 1px;
    #         border-color: #999999;
    #         # border-color: #666666;
    #         border-collapse: collapse;
    #     }}
    #     table#{random_id} th {{
    #         background:#b5cfd2;
    #         border-width: 1px;
    #         padding: 6px;
    #         border-style: solid;
    #         border-color: #ffffff;
    #         text-align:left;
    #         vertical-align:middle;
    #     }}
    #     table#{random_id} td {{
    #         background:#affbf8;
    #         # background:#ffffff;
    #         border-width: 1px;
    #         padding: 6px;
    #         border-style: solid;
    #         border-color: #ffffff;
    #     }}
    #     </style>
    #     """.format(random_id=random_id)
    # else:
    #     new_style = []
    #     s = re.sub(r'</?style>', '', style).strip()
    #     for line in s.split('\n'):
    #         line = line.strip()
    #         if not re.match(r'^table', line):
    #             line = re.sub(r'^', 'table ', line)
    #         new_style.append(line)
    #     new_style = ['<style>'] + new_style + ['</style>']
    #
    #     style = re.sub(r'table(#\S+)?', 'table#%s' % random_id, '\n'.join(new_style))

    df_html = re.sub(r'<table', r'<table id="query_table" ', df_html)

    return df_html
