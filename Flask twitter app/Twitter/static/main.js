const search = document.querySelector('.search')
const input = document.querySelector('.search-bar');
const search_icon = document.querySelector('.search-icon');

input.addEventListener("focus", () => {
    search.style["border"] = "1px solid #60BDF6";
    search.style["background-color"] = "white";
    search_icon.style["background-color"]="white";
})

input.addEventListener("focusout", () => {
    search.style["border"] = "1px solid white";
    search.style["background-color"]="#E6ECF0";
    search_icon.style["background-color"]="#E6ECF0";
})