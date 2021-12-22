document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("drawer-open-button").addEventListener("click",function() {
        this.classList.toggle("drawer-open");
        document.getElementById("header-drawer-nav").classList.toggle("drawer-open");
        document.getElementById("drawer-open-mask").classList.toggle("drawer-open");
    });
});