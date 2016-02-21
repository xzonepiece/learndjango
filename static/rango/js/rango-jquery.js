$(document).ready(function(){
    $("p").hover(function(){
        $(this).css('color', 'red');
    },
    function(){
        $(this).css('color', 'blue');
    });
    $('#suggestion').change(function(){
        var value, url, lower;
        value = $(this).val();
        lower_value = value.toLowerCase();
        url = '/rango/category/' + lower_value +'/';
        $("form[action='']").attr('action', url);
    });
});
