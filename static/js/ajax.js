$(document).ready(function(event){
    $(document).on('click', '#like', function(event){
        event.preventDefault();
            $.ajax({
                type: 'POST',
                url: "{% url 'timeline:like' %}",
                data: {
                    'post_pk': $(this).attr('name'),
                    'csrfmiddlewaretoken': '{{ csrf_token }}'},
                dataType: 'json',
             success: function(response){
                selector = document.getElementsByName(response.post_pk);
                if(response.liked){
                    $(selector).html("<i class='fas fa-lg fa-star star-yellow'></i>");
                }else{
                    $(selector).html("<i class='far fa-lg fa-star star-yellow'></i>");
                }
                selector2 = document.getElementsByName(response.post_pk + "-count");
                $(selector2).text(response.count);
            }
        });
    });
});

