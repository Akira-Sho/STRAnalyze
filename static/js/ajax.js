function likes(event, user_pk, post_pk) {
    console.log(user_pk)
    if(user_pk != "None"){
        fetch(myurl.base + 'likes/' + user_pk + '/' + post_pk, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json; charset=utf-8",
                    "X-CSRFToken": Cookies.get('csrftoken')
                },
            body: JSON.stringify({"status": "requested by javascript."})
            }
        )
        .then(response => response.json())
        .then(json => {
            // json-value
            console.log(json)
            // state of 'like'
            var is_pressed = (event.target.getAttribute("aria-pressed") === "true");
            event.target.setAttribute("aria-pressed", !is_pressed);
            // count of 'like' ±1
            var tag_span = event.target.getElementsByTagName('span')[0];
            coefficient = !is_pressed ? +1 : -1
            cnt = tag_span.innerHTML.match(/\((.+)\)/)[1]; // e.g. (3) => 3
            tag_span.innerHTML = tag_span.innerHTML.replace(cnt, parseInt(cnt) + coefficient);
        })
    } else {
        location.href=myurl.login;
    }
}

/*
関数作成 event,ユーザーpk、ポストpk
ユーザーpkを参照
if user_pkに値が入っているなら次の行の処理にすすむ、なら最後の行
feachメソッドでユーザーpk、ポストpkを取得。
    (リクエストやレスポンスなどを行えるまたはサーバー上のデータを取得できる
        通信方法はpost、コンテンツタイプはjson、js cookie libraryでcsrfトークンを取得
javascriptからのリクエストをjson文字列に変換？？？
//非同期処理 時間がかかる処理が完了する前に別の処理が実行される仕組み
thenは
response.json()は、メソッドであり、responseを完全に読み取る
引数=>{関数の本体}


*/