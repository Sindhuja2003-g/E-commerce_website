function addToCart(productName, productPrice) {
    // Instead of pushing directly to cartItems, make an AJAX request
    fetch('/add-to-cart/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        product_name: productName,
        price: productPrice
      })
    })
    .then(response => response.json())
    .then(data => {
      // Update UI based on response (optional)
    })
    .catch(error => {
      console.error(error);
    });
  }

  function updateCartDisplay() {
    // Make an AJAX request to fetch cart items
    fetch('/get-cart-items/')
    .then(response => response.json())
    .then(data => {
      const cartContainer = document.getElementById('cart-items');
      cartContainer.innerHTML = '';
  
      data.forEach(item => {
        const itemDiv = document.createElement('div');
        itemDiv.innerHTML = `${item.product_name} - $${item.price}`;
        cartContainer.appendChild(itemDiv);
      });
    })
    .catch(error => {
      console.error(error);
    });
  }
  
  // Call updateCartDisplay() initially to display existing cart items
  updateCartDisplay();
  