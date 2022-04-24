function popup() {
  document.querySelector(".comp").classList.remove("hide");
}
document.querySelector(".close-modal").addEventListener("click", () => {
  document.querySelector(".comp").classList.add("hide");
});

// api
var form = document.getElementById("sheetdb-form");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  fetch(form.action, {
    method: "POST",
    body: new FormData(document.getElementById("sheetdb-form")),
  })
    .then((response) => response.json())
    .then((html) => {
      // you can put any JS code here
      window.location.reload();
    });
});
