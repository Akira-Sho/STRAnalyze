document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("drawer-open-button").addEventListener("click",function() {
        this.classList.toggle("drawer-open");
        document.getElementById("header-drawer-nav").classList.toggle("drawer-open");
        document.getElementById("drawer-open-mask").classList.toggle("drawer-open");
    });
});

//省略形
//document.addEventListener('DOMContentLoaded', () => {
//document.getElementById("nav-button").addEventListener("click",() => {

//使用するイベントのロード
//nav-button のidを取得して、クリックされた時の処理を付与
//クラスのactiveをオンにする
//header-r...を取得してクリックされたらactiveをオン？
//drawer-open-maskを取得してactiveをオフ？