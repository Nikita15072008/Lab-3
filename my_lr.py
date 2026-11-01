import random
import tkinter as tk


def get_weights():
    all_simb = ''.join(map(chr, range(65, 91))) + '0123456789'
    return dict(zip(all_simb, range(1, 100)))

def get_block(weights, target, size=4):
    while True:
        block = ''.join(random.choices(list(weights.keys()), k=size))
        score = sum(weights[x] for x in block)
        if target[0] < score < target[1]:
            return block, score

def GUI(weights, target, c_blocks):

    def copy():
        text = used_key_label.cget('text')
        if not text:
            return
        window.clipboard_clear()
        window.clipboard_append(text)
        window.update()
        btn_copy.config(text='Copied!')
        window.after(1000, lambda: btn_copy.config(text='Copy'))

    def get_key():
        blocks, sums = zip(*[get_block(weights, target) for _ in range(c_blocks)])
        key = '-'.join(blocks)
        used_key_label.config(text=key)
        

    window = tk.Tk()
    window.title('Generator Keys')
    window.geometry('350x400')
    
    bg_img = tk.PhotoImage(file='images.png')
    window.bg_img = bg_img

    label_bg = tk.Label(window, image=bg_img)
    label_bg.place(x=0, y=0, relwidth=1, relheight=1)

    btn_guess = tk.Button(window, text='Get key', width=15, command=get_key)
    btn_guess.place(relx=0.07, rely=0.67)
    btn_copy = tk.Button(window, text='Copy', width=15, command=copy)
    btn_copy.place(relx=0.55, rely=0.67)

    used_letters_label = tk.Label(window, text='Generated key:')
    used_letters_label.place(relx=0.5, rely=0.3, anchor='center')

    used_key_label = tk.Label(window, text='no generated')
    used_key_label.place(relx=0.5, rely=0.4, anchor='center')

    window.mainloop()


if __name__ == '__main__':
    weights = get_weights()
    target = (30, 35)
    c_blocks = 3
    GUI(weights, target, c_blocks)

