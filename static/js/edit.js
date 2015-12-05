$(function() {
    $(document).ready(apply_css)

    function apply_css() {
        for (i = 0; i < css.length; i++) {
            select = css[i]['select']
            attr = css[i]['attr']
            val = css[i]['val']
            $(select).css(attr, val);
        }
    }

    $('#editor *').hover(function() {
        var attr = $(this).attr('id');
        if (attr != undefined && attr != false) {
            $('.hover').removeClass('hover');
            $(this).addClass('hover');
        }


    })

});
