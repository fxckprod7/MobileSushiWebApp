const btn_pls = document.getElementById('item-quantity-plus-btn');
const btn_mns = document.getElementById('item-quantity-minus-btn');

const quantity = document.getElementById('quantity-number');

btn_pls.addEventListener('click', () => {
    if (parseInt(quantity.innerHTML) < 9){
        quantity.innerHTML = parseInt(quantity.innerHTML) + 1;
    }
});

btn_mns.addEventListener('click', () => {
    if(parseInt(quantity.innerHTML) > 1){
        quantity.innerHTML = parseInt(quantity.innerHTML) - 1;
    }
});