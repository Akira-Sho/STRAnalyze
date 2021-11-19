document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("nav-button").addEventListener("click",function() {
        this.classList.toggle("active");
        document.getElementById("header-drawer-nav").classList.toggle("active")
        document.getElementById("mask").classList.toggle("active")
    })
})

//省略形
//document.addEventListener('DOMContentLoaded', () => {
//document.getElementById("nav-button").addEventListener("click",() => {

//使用するイベントのロード
//nav-button のidを取得して、クリックされた時の処理を付与
//クラスのactiveをオンにする
//header-r...を取得してクリックされたらactiveをオン？
//maskを取得してactiveをオフ？