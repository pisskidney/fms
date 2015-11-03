$(function(){
    $('#id_name').keyup(function() {
        var site_name = $('#id_name').val();
        site_name = site_name.replace(/ /g, "");
        if (site_name != "") {

            $('#build-name-domain-options').show();


            $('#id_name').val(site_name);
            $('.build-name-url b').html(site_name);
        } else {
            $('#build-name-domain-options').hide();
        }
    });
});
