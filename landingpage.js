const product = [
    {
        id: 0,
        image: 'Images/gg-1.jpg',
        title: 'Eat-Sleep Blak',
        price: 699,
    },
    {
        id: 1,
        image: 'Images/hh-2.jpg',
        title: 'CUSTOMIZABLE Ts-BLAK',
        price: 999,
    },
    {
        id: 2,
        image: 'Images/ee-3.jpeg',
        title: 'Born to win-BLAK ',
        price: 599,
    },
    {
        id: 3,
        image: 'Images/aa-1.png',
        title: 'PLAIN BLAK OneX',
        price: 499,
    }
];
const categories = [...new Set(product.map((item)=>
    {return item}))]
    let i=0;
document.getElementById('root').innerHTML = categories.map((item)=>
{
    var {id, image, title, price} = item;
    
    return(
        `<div class='box'>
            <div class='img-box'>
                <img class='images' src=${image}></img>
            </div>
        <div class='bottom'>
        <p>${title}</p>
        <h2>Rs. ${price}.00</h2>`+
        "<button onclick='addtocart("+(i++)+")'>Add to cart</button>"+
        `</div>
        </div>`
)
}).join('')

var cart =[];

function addtocart(a){
    cart.push({...categories[a]});
    displaycart();
}
function delElement(a){
    cart.splice(a, 1);
    displaycart();
}
// Get reference to the button element
var switchButton = document.getElementById("btn");

// Add click event listener to the button
switchButton.addEventListener("click", function() {
  // Redirect to another HTML page upon button click
  window.location.href = "payment.html";
});

function displaycart(){
    let j = 0, total=0;
    document.getElementById("count").innerHTML=cart.length;
    if(cart.length==0){
        document.getElementById('cartItem').innerHTML = "Your cart is empty";
        document.getElementById("total").innerHTML = "Rs. "+0+".00";
    }
    else{
        document.getElementById("cartItem").innerHTML = cart.map((items)=>
        {
            var {image, title, price} = items;
            total=total+price;
            document.getElementById("total").innerHTML = "Rs. "+total+".00";
            return(
                `<div class='cart-item'>
                <div class='row-img'>
                    <img class='rowimg' src=${image}>
                </div>
                <p style='font-size:12px;'>${title}</p>
                <h2 style='font-size: 15px;'>Rs. ${price}.00</h2>`+
                "<i class='fa-solid fa-trash' onclick='delElement("+ (j++) +")'></i></div>"
            );
        }).join('');
    }

    
}