

const shopSvg = document.querySelector(".shop-svg");
const shopDropdown = document.querySelector(".shop-dropdown");

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
