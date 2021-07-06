from typing import Any, List, Optional
from collections import defaultdict


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    ...

    #border styles
    BORDER=dict(zip(["BAR","DASH","TOP_LEFT","TOP_MIDDLE","TOP_RIGHT","LABEL_LEFT","LABEL_MIDDLE","LABEL_RIGHT","BOTTOM_LEFT","BOTTOM_MIDDLE","BOTTOM_RIGHT"], list('│─┌┬┐├┼┤└┴┘')))
    #keep each column length
    cell_length=defaultdict(int)
    columns=len(labels) if labels else len(rows[0])
    #align setting
    align="^" if centered else "<" 

    #find max column length
    for row in rows:
        for i in range(len(row)):
            length = len(str(row[i]))
            if not cell_length.get(i) or cell_length.get(i) < length:
                cell_length[i]=length
    if labels:
        for column in range(len(labels)):
            length = len(str(labels[column]))
            if not cell_length.get(column) or cell_length.get(column) < length:
                cell_length[column]=length
    #create table top
    table=""
    
    top_line=f"{BORDER['TOP_LEFT']}" + f"{BORDER['TOP_MIDDLE']}".join([BORDER['DASH']*(cell_length[i]+2) for i in cell_length.keys()])+f"{BORDER['TOP_RIGHT']}"
    table+=top_line+"\n"

    #create table label part
    if labels:
        label_separate_line = f"{BORDER['LABEL_LEFT']}"+f"{BORDER['LABEL_MIDDLE']}".join([BORDER['DASH']*(cell_length[i]+2) for i in cell_length.keys()])+f"{BORDER['LABEL_RIGHT']}"
        label_row=f"{BORDER['BAR']}".join([' {!s:{fill}{align}{width}} '.format(labels[label_no], fill="", align=align,width=cell_length[label_no])  for label_no in range(columns)])
        table+=f"{BORDER['BAR']}"+label_row+f"{BORDER['BAR']}"+"\n"
        table+=label_separate_line+"\n"
    
    #create table data part
    line= ""
    for r in rows:
        line=f"{BORDER['BAR']}"
        for i in range(columns):
            line+=' {!s:{fill}{align}{width}} '.format(r[i], fill="", align=align,width=cell_length[i]) 
            if i< columns-1:
                line+=f"{BORDER['BAR']}"
        line+=f"{BORDER['BAR']}"+'\n'
        table+=line
    #create table bottom
    bottom_line=f"{BORDER['BOTTOM_LEFT']}" + f"{BORDER['BOTTOM_MIDDLE']}".join([BORDER['DASH']*(cell_length[i]+2) for i in cell_length.keys()])+f"{BORDER['BOTTOM_RIGHT']}"
    table+=bottom_line

    return table




