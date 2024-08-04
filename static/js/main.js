document.addEventListener('DOMContentLoaded', function() {
    // Función para actualizar la cantidad de productos en el carrito
    const updateCartQuantity = (quantity) => {
        const cartBadge = document.querySelector('.cart-badge');
        if (cartBadge) {
            cartBadge.textContent = quantity;
        }
    };

    // Maneja el evento de clic en los botones "Añadir al carrito"
    const addToCartButtons = document.querySelectorAll('.add-to-cart-button');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', () => {
            const productId = button.dataset.productId;

            // Simulación de actualización de cantidad en el carrito
            let currentQuantity = parseInt(document.querySelector('.cart-badge').textContent) || 0;
            updateCartQuantity(currentQuantity + 1);

            // Redirige al usuario a la página de checkout
            window.location.href = `/add_to_cart/${productId}`;
        });
    });

    // Ejemplo de implementación para un filtro de productos (si es necesario)
    const productFilter = document.querySelector('#product-filter');
    if (productFilter) {
        productFilter.addEventListener('input', (event) => {
            const filterValue = event.target.value.toLowerCase();
            const products = document.querySelectorAll('.product-item');

            products.forEach(product => {
                const productName = product.querySelector('h3').textContent.toLowerCase();
                if (productName.includes(filterValue)) {
                    product.style.display = 'block';
                } else {
                    product.style.display = 'none';
                }
            });
        });
    }

    // Implementación de la funcionalidad de búsqueda
    const searchInput = document.querySelector('#search-input');
    if (searchInput) {
        searchInput.addEventListener('input', (event) => {
            const filterValue = event.target.value.toLowerCase();
            const products = document.querySelectorAll('.product-item');

            products.forEach(product => {
                const productName = product.querySelector('h3').textContent.toLowerCase();
                if (productName.includes(filterValue)) {
                    product.style.display = 'block';
                } else {
                    product.style.display = 'none';
                }
            });
        });
    }
});

function Realizar_pedido() {
    let pedido = document.getElementById('pedido');

    if (pedido.value) {
        Swal.fire("Pedido Exitoso");
    }
    else {
        Swal.fire("Llene los campos porfavor");
    }
}
