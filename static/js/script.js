const contactButton = document.getElementById("contact-us-button");
const popupModal = document.getElementById("popup-modal");
const closePopup = document.getElementById("close-popup");

contactButton.addEventListener("click", () => {
  popupModal.style.display = "block";
});


closePopup.addEventListener("click", () => {
  popupModal.style.display = "none";
});

window.addEventListener("click", (event) => {
  if (event.target == popupModal) {
    popupModal.style.display = "none";
  }
});
