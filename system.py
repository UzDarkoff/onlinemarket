from classes import *
class Store:
    def __init__(self):
        self.products = [
            Product(1, "Telefon", 3000000),
            Product(2, "Noutbuk", 8000000),
            Product(3, "Soat", 500000),
            Product(4, "Kitob", 70000),
        ]
        self.cart = Cart()
        self.order = Order()

    def show_products(self):
        print("Mahsulotlar:")
        for product in self.products:
            print(f"{product.name}-{product.price}so'm")


def run():
    store = Store()

    while True:
        print("\n1. Mahsulotlarni ko'rish")
        print("2. Savatchaga qo'shish")
        print("3. Savatchani ko'rish")
        print("4. Savatchadan mahsulotni olib tashlash")
        print("5. Buyurtma berish")
        print("6. Chiqish")

        choice = input("Tanlovingiz: ")
        if choice == "1":
            store.show_products()
        elif choice == "2":
            product_id = int(input("Mahsulot ID: "))
            quantity = int(input("Miqdori: "))
            product = next((p for p in store.products if p.product_id == product_id), None)
            if product:
                store.cart.add_to_cart(product, quantity)
                print(f"{product.name} savatchaga qo'shildi.")
            else:
                print("Mahsulot topilmadi.")
        elif choice == "3":
            print(store.cart.view_cart())
        elif choice == "4":
            product_id = int(input("Olib tashlamoqchi bo'lgan mahsulot ID: "))
            store.cart.remove_from_cart(product_id)
            print("Mahsulot savatchadan olib tashlandi.")
        elif choice == "5":
            print(store.order.place_order(store.cart))
        elif choice == "6":
            print("Chiqib ketildi.")
            break
        else:
            print("Noto'g'ri tanlov.")


run()