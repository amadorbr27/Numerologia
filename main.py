from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import webbrowser
from kivy.config import Config
from datetime import datetime

# Configurações de tamanho da tela e redimensionamento
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', True)

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
        'A': 1, 'I': 1, 'Q': 1, 'J': 1, 'Y': 1,
        'B': 2, 'K': 2, 'R': 2,
        'C': 3, 'G': 3, 'L': 3, 'S': 3,
        'D': 4, 'M': 4, 'T': 4,
        'E': 5, 'H': 5, 'N': 5,
        'U': 6, 'V': 6, 'W': 6, 'X': 6, 'Ç': 6,
        'O': 7, 'Z': 7,
        'F': 8, 'P': 8
    }
    accent_modifiers = {
        'Á': 3, 'É': 7, 'Í': 3, 'Ó': 9, 'Ú': 8,  # Acento agudo
        'À': 2, 'È': 10, 'Ì': 2, 'Ò': 14, 'Ù': 12,  # Acento grave
        'Â': 8, 'Ê': 12, 'Î': 8, 'Ô': 14, 'Û': 13,  # Acento circunflexo
        'Ã': 4, 'Ñ': 8, 'Õ': 10,                   # Til
        'Ä': 2, 'Ë': 10, 'Ï': 2, 'Ö': 14, 'Ü': 12   # Trema
    }
    # Variáveis para armazenar a soma das vogais e consoantes
    soma_vogais = 0
    soma_consoantes = 0
    details = []
    total = 0
    i = 0
    name = name.upper()

    while i < len(name):
        char = name[i]
        value = 0

        # Verifica se o caractere está na tabela principal ou se é um acento
        if char in cabalistic_table:
            value = cabalistic_table[char]
        elif char in accent_modifiers:
            # Aplicar o modificador de acento
            value = accent_modifiers[char]

        if value != 0:
            details.append(f"{char} = {value}")
            total += value
        
        i += 1

    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(digit) for digit in str(total))
    
    return total, details

def ano_pessoal(date_of_birth):
    day_month = date_of_birth[:5]  # Pegar DD/MM
    year = datetime.now().year
    day_month_year = day_month + '/' + str(year)
    return calculate_lucky_number(day_month_year)

def caminho_da_vida(date_of_birth):
    return calculate_lucky_number(date_of_birth)

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

class NumerologyApp(App):
    def build(self):
        self.title = 'Calculadora de Numerologia'
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Nome completo
        name_box = BoxLayout(orientation='vertical', size_hint=(1, None), height=80)
        name_label = Label(text='Digite o nome completo', size_hint=(1, None), height=30)
        name_box.add_widget(name_label)
        self.name_input = TextInput(multiline=False, size_hint=(1, None), height=50)
        name_box.add_widget(self.name_input)
        layout.add_widget(name_box)
        
        # Data de nascimento
        dob_box = BoxLayout(orientation='vertical', size_hint=(1, None), height=80)
        dob_label = Label(text='Digite a data de nascimento (DD/MM/AAAA)', size_hint=(1, None), height=30)
        dob_box.add_widget(dob_label)
        self.dob_input = TextInput(multiline=False, size_hint=(1, None), height=50)
        self.dob_input.bind(text=self.on_dob_text)
        dob_box.add_widget(self.dob_input)
        layout.add_widget(dob_box)

        # Botão de calcular
        self.calculate_button = Button(text='Calcular Numerologia', size_hint=(0.5, None), height=50)
        self.calculate_button.pos_hint = {'center_x': 0.5}
        self.calculate_button.bind(on_press=self.calculate_numerology)
        layout.add_widget(self.calculate_button)

        # Resultados
        self.result_label = Label(text='', size_hint=(1, 1), valign='top')
        layout.add_widget(self.result_label)

        self.link_label = Label(text='', markup=True, color=(0, 0, 1, 1), size_hint=(1, None), height=50)
        layout.add_widget(self.link_label)
        
        return layout

    def on_dob_text(self, instance, value):
        clean_value = value.replace('/', '')
        if len(clean_value) == 8:
        # Format only if it's not already formatted
            if value.count('/') < 2:
                formatted_text = f"{clean_value[:2]}/{clean_value[2:4]}/{clean_value[4:]}"
                instance.text = formatted_text
                instance.cursor = (len(formatted_text), 0)  # Move cursor to end of text
        elif len(value) > 10:
        # If user tries to enter more digits after a complete date, revert to last valid
            instance.text = f"{clean_value[:2]}/{clean_value[2:4]}/{clean_value[4:8]}"

            
    def calculate_numerology(self, instance):
        name = self.name_input.text
        date_of_birth = self.dob_input.text
        
        pythagorean_result = numerology_pythagorean(name)
        cabalistic_result, details = numerology_cabalistic(name)
        lucky_number = calculate_lucky_number(date_of_birth)
        
        detailed_result = '\n'.join(details)  # Junta todos os detalhes em um único texto
        result_message = (
            #f"Numerologia (Pitagórica): {pythagorean_result}\n"
            f"Numerologia (Cabalística): {cabalistic_result}\n"
            f"Detalhes da Cabalística: \n{detailed_result}\n"  # Exibe os detalhes de cada letra e acento
            f"Número da sorte: {lucky_number}"
        )
        
        self.result_label.text = result_message
        
        cabalistic_link = get_cabalistic_link(cabalistic_result)
        if cabalistic_link:
            self.link_label.text = f"[ref=link]O número {cabalistic_result} na Numerologia Cabalística[/ref]"
            self.link_label.bind(on_ref_press=lambda instance, ref: webbrowser.open(cabalistic_link))

if __name__ == '__main__':
    NumerologyApp().run()
