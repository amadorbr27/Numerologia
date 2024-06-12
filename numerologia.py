import tkinter as tk
import webbrowser

def numerology_pythagorean(name):
    pythagorean_table = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
    }
    
    name = name.upper()
    total = sum(pythagorean_table[char] for char in name if char in pythagorean_table)
    
    while total > 9 and total not in [11, 22, 33]:  # consider master numbers
        total = sum(int(digit) for digit in str(total))
    
    return total

def numerology_cabalistic(name):
    cabalistic_table = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 8, 'G': 3, 'H': 5, 'I': 1,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 7, 'P': 8, 'Q': 1, 'R': 2,
        'S': 3, 'T': 4, 'U': 6, 'V': 6, 'W': 6, 'X': 6, 'Y': 1, 'Z': 7
    }
    
    name = name.upper()
    total = sum(cabalistic_table[char] for char in name if char in cabalistic_table)
    
    while total > 9 and total not in [11, 22, 33]:  # consider master numbers
        total = sum(int(digit) for digit in str(total))
    
    return total

def calculate_lucky_number(date_of_birth):
    digits = [int(char) for char in date_of_birth if char.isdigit()]
    total = sum(digits)
    
    while total > 9 and total not in [11, 22, 33]:  # consider master numbers
        total = sum(int(digit) for digit in str(total))
    
    return total

def get_cabalistic_link(number):
    links = {
        1: "https://alquimiaoperativa.com/significado-numero-1-numerologia-cabalistica/",
        2: "https://alquimiaoperativa.com/significado-numero-2-numerologia-cabalistica/",
        3: "https://alquimiaoperativa.com/simbolismo-do-3-o-numero-do-mestre/",
        4: "https://alquimiaoperativa.com/simbolismo-4-numero-ordem/",
        5: "https://alquimiaoperativa.com/simbolismo-5-numero-poder-magia-versatilidade/",
        6: "https://alquimiaoperativa.com/simbolismo-6-numero-saude-servico-bem-estar/",
        7: "https://alquimiaoperativa.com/simbolismo-7-numero-perfeicao-divina/",
        8: "https://alquimiaoperativa.com/8-numero-poder-material-justica/",
        9: "https://alquimiaoperativa.com/misterios-significado-numero-9/",
        11: "https://alquimiaoperativa.com/simbolismo-11-numero-mestre-forca/",
        22: "https://alquimiaoperativa.com/simbolismo-alquimico-numerologico-22/",
        33: "https://alquimiaoperativa.com/33-numero-do-poder-espiritual/"
    }
    return links.get(number, "")


def calculate_numerology():
    name = entry_name.get()
    date_of_birth = entry_dob.get()
    
    pythagorean_result = numerology_pythagorean(name)
    cabalistic_result = numerology_cabalistic(name)
    lucky_number = calculate_lucky_number(date_of_birth)
    
    result_message = (
        f"Numerologia (Pitágoras): {pythagorean_result}\n"
        f"Numerologia (Cabalística): {cabalistic_result}\n"
        f"Número da sorte com base na data de nascimento: {lucky_number}"
    )
    
    result_label.config(text=result_message)
    
    cabalistic_link = get_cabalistic_link(cabalistic_result)
    if cabalistic_link:
        link_label.config(text=f"Clique aqui para saber mais sobre o número {cabalistic_result} na Numerologia Cabalística", fg="blue", cursor="hand2")
        link_label.bind("<Button-1>", lambda e: webbrowser.open_new(cabalistic_link))
    else:
        link_label.config(text="", cursor="")


# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de Numerologia")
root.geometry('500x400')  # Largura de 500 pixels e altura de 300 pixels

# Criando os elementos da interface
label_name = tk.Label(root, text="Digite o nome completo:", padx=10, pady=10, font=("Helvetica", 10))
label_name.pack()

entry_name = tk.Entry(root, width=50)
entry_name.pack()

label_dob = tk.Label(root, text="Digite a data de nascimento (DD/MM/AAAA):", padx=10, pady=20, font=("Helvetica", 10))
label_dob.pack()

entry_dob = tk.Entry(root)
entry_dob.pack()

button_calculate = tk.Button(root, text=" Calcular ", command=calculate_numerology)
button_calculate.pack(pady=20)

result_label = tk.Label(root, text="", padx=10, pady=20, wraplength=500, font=("Helvetica", 10), anchor='w', justify='left')
result_label.pack(anchor='w', padx=10, pady=10)

link_label = tk.Label(root, text="", padx=10, pady=20, font=("Helvetica", 10), anchor='w', justify='left')
link_label.pack(anchor='w', padx=10, pady=10)

# Iniciando o loop da interface
root.mainloop()