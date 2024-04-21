// All delete buttons on the items
const deleteButtons = document.getElementsByClassName("delete-basket-item-btn");

// Prices of all items in the basket
const itemPrices = document.getElementsByClassName("basket-item-price");

// Checkout values
const subtotalValue = document.getElementById("subtotal-value");
const discountValue = document.getElementById("discount-value");
const totalValue = document.getElementById("total-value");

// Set here discount value
const discount = 5;


// Function to calculate the subtotal value
const subtotalCalculation = () => {
    let subtotal = 0;
    for (let i = 0; i < itemPrices.length; i++){
        subtotal += parseFloat(itemPrices[i].innerHTML.replace("$", ""));
    }

    return subtotal == 0 ? "$0" : "$" + subtotal.toFixed(2);
}

// Function to calculate prices
const calculatePrices = () => {
    subtotalValue.innerHTML = subtotalCalculation();
    discountValue.innerHTML = "$" + discount.toFixed(2);

    let total = parseFloat(subtotalValue.innerHTML.replace("$", "")) - parseFloat(discountValue.innerHTML.replace("$", ""));
    total = total < 0 ? 0 : total;

    totalValue.innerHTML = total == 0 ? "$0" : "$" + total.toFixed(2);
}


// Add a onclick events to the basket items
for (let i = 0; i < deleteButtons.length; i++) {
    deleteButtons[i].addEventListener("click", function () {
        const basketItem = this.parentNode;
        basketItem.parentNode.removeChild(basketItem);
        calculatePrices();
    });
}

// Calculate prices
calculatePrices();