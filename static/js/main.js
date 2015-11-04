$(function(){

    var timer_check_domain;

    function set_check_domains_timer(site_name) {
        clearTimeout(timer_check_domain);
        timer_check_domain = setTimeout(
           check_domains,
           2000
        )
    }

    function check_domains() {
        // make ajax call and see if domains are free
        var site_name = $('#id_name').val();
        site_name = site_name.replace(/ /g, "");
        $.getJSON('/api/' + site_name, function(resp) {
            $('#build-name-img-inhouse-check').hide()
            $('#build-name-img-com-check').hide()
            if (resp['inhouse'] == true) {
                $('#build-name-img-inhouse-ok').show()
                $('#build-name-img-inhouse-bad').hide()
                $('#build-name-inhouse-status').html('available')
            } else {
                $('#build-name-img-inhouse-ok').hide()
                $('#build-name-img-inhouse-bad').show()
                $('#build-name-inhouse-status').html('taken')
            }
            if (resp['com'] == true) {
                $('#build-name-img-com-ok').show()
                $('#build-name-img-com-bad').hide()
                $('#build-name-com-status').html('available')
            } else {
                $('#build-name-img-com-ok').hide()
                $('#build-name-img-com-bad').show()
                $('#build-name-com-status').html('taken')
            }
        });
    }

    $('#id_name').keyup(function() {
        var site_name = $('#id_name').val();
        site_name = site_name.replace(/ /g, "");
        if (site_name != "") {
            // set input values
            $('#build-name-domain-options').show();
            $('#id_name').val(site_name);
            $('.build-name-url b').html(site_name);
            // set gifs and disable buttons
            $('#build-name-img-inhouse-check').show()
            $('#build-name-img-inhouse-ok').hide()
            $('#build-name-img-inhouse-bad').hide()
            $('#build-name-inhouse-status').html('checking')

            $('#build-name-img-com-check').show()
            $('#build-name-img-com-ok').hide()
            $('#build-name-img-com-bad').hide()
            $('#build-name-com-status').html('checking')

            set_check_domains_timer(site_name)
        } else {
            $('#build-name-domain-options').hide();
        }
    });
});
