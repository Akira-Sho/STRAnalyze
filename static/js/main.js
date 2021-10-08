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