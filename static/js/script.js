document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("nav-button").addEventListener("click",function() {
        this.classList.toggle("active");
        document.getElementById("header-drawer-nav").classList.toggle("active")
        document.getElementById("mask").classList.toggle("active")
    })
})

