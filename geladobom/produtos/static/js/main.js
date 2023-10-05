// Homepage Elements
const homeProductSvg = document.querySelectorAll("#stroke");
const homeProductLink = document.querySelectorAll("#linkTitle");
// Shop Elements
const shopSvg = document.querySelector(".shop-svg");
const shopDropdown = document.querySelector(".shop-dropdown");

// Dropdown Shop
shopSvg.addEventListener("click", (e) => {
  shopDropdown.classList.toggle("display");
  e.stopPropagation();
});

document.addEventListener("click", (e) => {
  if (!shopDropdown.contains(e.target)) {
    shopDropdown.classList.remove("display");
  }
});

// Arrow Animation
for (let svg = 0; svg < homeProductLink.length; svg++) {
  homeProductLink[svg].addEventListener("mouseover", (e) => {
    homeProductSvg[svg].classList.add("strokeHover");
    e.stopPropagation();
  });

  homeProductLink[svg].addEventListener("mouseleave", (e) => {
    homeProductSvg[svg].classList.remove("strokeHover");
    e.stopPropagation();
  });
}
