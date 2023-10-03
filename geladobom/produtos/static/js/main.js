const homeProductSvg = document.querySelectorAll("#stroke");
const homeProductLink = document.querySelectorAll("#linkTitle");

const shopSvg = document.querySelector(".shop-svg");
const shopDropdown = document.querySelector(".shop-dropdown");

console.log(homeProductLink);

// Dropdown Shop
shopSvg.addEventListener("click", (e) => {
  shopDropdown.classList.toggle("display");
  e.stopPropagation();
});

document.addEventListener("click", (e) => {
  if (
    !e.target.matches(".shop-dropdown") &&
    !e.target.matches(".shop-dropdown-items")
  ) {
    shopDropdown.classList.remove("display");
  }
});

for (i in homeProductSvg) {
  homeProductLink[i].addEventListener("mouseover", (e) => {
    homeProductSvg[i].classList.add("strokeHover");
    e.stopPropagation()
  });
}

homeProductLink.addEventListener("mouseleave", (e) => {
  homeProductSvg.classList.remove("strokeHover");
});
