//let text = document.getElementById('id_text');
//let count = document.getElementById('count');

//text.addEventListener('keyup', e => {
//    let num = twttr.txt.getTweetLength(e.target.value) / 2;
//    count.innerHTML = num;
//    num <= 200
//        ? count.classList.remove('text-danger')
//        : count.classList.add('text-danger');
//    })
    window.onload = (() => {
        let img = document.getElementById('id_photo');
        let mainImage = document.getElementById('mainImage');
      
        img.addEventListener('change', e => {
          let reader = new FileReader();
          reader.onload = e => {
            mainImage.src = e.target.result;
          }
          reader.readAsDataURL(e.target.files[0]);
        })
      })
//onloadで画像を読み込んでから処理を実行 アロー関数定義 functionの文字を省略 {}の中に関数内容
//2つのidを入れた変数用意
//画像変更フォームにはid_photoのidが自動で設定されている
//画像変更フォームを対象としたイベントchange は内容が変更された時に発動する イベントオブジェクトe
//readerという関数作成 取得したfileobjectの内容を読み込める
//filereaderのresultプロパティはファイルの内容を返す target イベント発生元要素？？
//
//
