class Product:
    def __init__(self, name:str, quantity:float, **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = 'unit' # options: kg, g, L, ml
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity})"


class Recipe:
    ingredients = []
    instructions = [] ####nieko nereiskia

    def add_ingredient(self, product:Product):
        self.ingredients.append(product)

    def change_ingredient_quantity(self, ingredient_id:int, new_quantity:float):
        self.ingredients[ingredient_id].quantity = new_quantity

    def remove_ingredient(self, ingredient_id:int):
        self.ingredients.pop(ingredient_id)


class Fridge:
    contents = []

    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name == product_name:
                return product_id, product
        return None, None
    
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

    def add_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name) # nenaudojamus product_id atejas is funkcijos check_product
        if product is not None:
            product.quantity += quantity
        else:
            self.contents.append(Product(name, quantity))

    def remove_product(self, name:str, quantity:float):
        pass

    def print_contents(self):
        pass

    def check_recipe(self, recipe:Recipe):
        pass


def main():
    fridge = Fridge()

while True:
    print('===[ Šaldytuvas ]===')
    print('0: Išeiti')
    print('1: Pridėti produktą')
    print('2: Išimti produktą')
    print('3: Patikrinti kiekį šaldytuve')
    print('4: Patikrinti receptą')
    print('5: Išspausdinti šaldytuvo turinį')
    pasirinkimas = input('Pasirinkimas: ')
    if pasirinkimas.startswith('0'):
        break
    elif pasirinkimas.startswith('1'):
        name = input('Produktas: ')
        quantity = float(input('Kiekis: '))
    for product in quantity:
        if product.name == name:
            if product.quantity >= quantity:
                product.quantity -= quantity
        
    