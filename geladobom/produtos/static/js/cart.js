const updateBtns = document.getElementsByClassName("update-cart");

for (let i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    const productId = this.dataset.product;
    const action = this.dataset.action;
    const url=this.dataset.url;
    console.log("productId:", productId, "Action:", action, "URL:", url);
    updateOrder(productId, action, url);
  });
}

function updateOrder(productId, action, url) {
  fetch(url, {
    method: "POST",
    headers: {
      'Content-Type': "application/json",
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({ "productId": productId, "action": action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("Data:", data);
      location.reload()
    }); 
}
