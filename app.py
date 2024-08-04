from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo
products = {
    'celulares': [
        {'id': 1, 'name': 'Iphone 12 Pro', 'price': '$530.00', 'image': 'iphone12pro.png'},
        {'id': 2, 'name': 'Iphone 12 Pro', 'price': '$530.00', 'image': 'Iphone_12.png'},
        {'id': 3, 'name': 'Iphone 15 Pro', 'price': '$800.00', 'image': 'iphone_15.png'},
        {'id': 4, 'name': 'Samsung A15', 'price': '$200.00', 'image': 'Galaxi_A15.png'},
        {'id': 5, 'name': 'Samsung A52', 'price': '$300.00', 'image': 'Samsung-A52.png'},
        {'id': 6, 'name': 'Samsung A70', 'price': '$430.00', 'image': 'Galaxi_A70.png'},
        {'id': 7, 'name': 'Infinix 30', 'price': '$600.00', 'image': 'Infinix_30.png'},
        {'id': 8, 'name': 'Infinix Hot 11S', 'price': '$400.00', 'image': 'Infinix_Hot_11S.png'},
        {'id': 9, 'name': 'Infinix Hot 40 Pro', 'price': '$650.00', 'image': 'Infinix_Hot_40_Pro.png'},
        {'id': 10, 'name': 'Infinix Zero 3', 'price': '$700.00', 'image': 'Infinix_Zero_3.png'},
        # Añade más productos aquí
    ],
    'tablets': [
        {'id': 101, 'name': 'Tab Samsung Android 3G', 'price': '$500.00', 'image': 'Tab_Samsung_Android 3g, 4g.png'},
        {'id': 102, 'name': 'Tab Samsung NZ', 'price': '$799.00', 'image': 'Tab_Samsung_NZ.png'},
        {'id': 103, 'name': 'Ipad Pro', 'price': '$709.00', 'image': 'Ipad_Pro.png'},
        {'id': 104, 'name': 'Ipad Air 3', 'price': '$399.00', 'image': 'Ipad_Air_3.png'},
        {'id': 105, 'name': 'Ipad Pro 11 Zoll', 'price': '$399.00', 'image': 'Apple_IPad_Pro-_1_Zoll.png'},
        
        
        # Añade más productos aquí
    ],
    'laptops': [
        {'id': 201, 'name': 'Lenovo ThinkPad T14 Gen 4 Black 05', 'price': '$1299.00', 'image': 'Lenovo_ThinkPad_T14_Gen_4_Black_05.png'},
        {'id': 202, 'name': 'Dell XSP 15', 'price': '$1400.00', 'image': 'Dell_XSP_15.png'},
        {'id': 203, 'name': 'Dell Inspiron 3530', 'price': '$1200.00', 'image': 'Dell_Inspiron_3530.png'},
        {'id': 204, 'name': 'NoteBook Laptop HP', 'price': '$2000.00', 'image': 'NoteBook_Laptop_HP.png'},
        {'id': 205, 'name': 'Macbook Laptop', 'price': '$2100.00', 'image': 'Macbook_Laptop.png'},
        
         
        # Añade más productos aquí
    ],
    'accesorios': [
        {'id': 301, 'name': 'AirPods Pro', 'price': '$100.00', 'image': 'Apple_Airpods_Pro.png'},
        {'id': 302, 'name': 'Auriculares A50', 'price': '$200.00', 'image': 'Auriculares_A50.png'},
        {'id': 303, 'name': 'Set De Interfaz', 'price': '$190.00', 'image': 'Set_Interfaz.png'},
        {'id': 304, 'name': 'WebCam HP Pro', 'price': '$200.00', 'image': 'Camar_HP_Pro_Webcam.png'},
        {'id': 305, 'name': 'WebCam Laptop Asus', 'price': '$100.00', 'image': 'WebCam_Laptop_Asus.png'},
        # Añade más productos aquí
    ]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products/<category>')
def product_list(category):
    category_products = products.get(category, [])
    return render_template('product_list.html', category=category, products=category_products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    for category, items in products.items():
        for product in items:
            if product['id'] == product_id:
                return render_template('product_detail.html', product=product)
    return "Producto no encontrado", 404

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
