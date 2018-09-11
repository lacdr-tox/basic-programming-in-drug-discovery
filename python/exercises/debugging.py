# ---
# jupyter:
#   hide_input: false
#   jupytext_format_version: '1.2'
#   jupytext_formats: ipynb,py
#   kernelspec:
#     display_name: Python [default]
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.5
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: false
#     sideBar: true
#     skip_h1_title: false
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: false
#     toc_position: {}
#     toc_section_display: true
#     toc_window_display: true
# ---

# # Let's play the lottery 
#
# because writing grant proposals just doesn't work

# There are some bugs in the code below, and you have to fix them. Run the code and have a good look at the error message. Fix the bug and run the code again. In the end, you should be able to win the lottery, if you buy enough tickets.

# +
def buy_tickets(n,nr_min=0,nr_max=1e9):
    return np.random.randint(nr_min,nr_max,size=n)

def draw_winner(nr_min=0,nr_max=1e9):
    return np.random.randint(nr_min,1e9)

def announce_results(tickets,winner):
    print("Is one of your {} tickets a winner??".format(len(tickets))
    if winner in tickets:
        print("Congratulations: you're a winner!!!!!")
    else
        print(Sorry, better luck next time...")

def play_lottery(ntickets,nr_min=0,nr_max=1e9):
    tickets = Buy_Tickets(nr_min,nr_max,ntickets)
    winner = draw_winner(nr_min,nr_max)
    announce_results(tickets,winner)

play_lottery(ntickets,0,10)
